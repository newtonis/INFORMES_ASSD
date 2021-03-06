//
// Created by newtonis on 4/30/2019.
//

#include "Reverb.h"
#include "WavFile.h"
#include <iostream>
using namespace std;


Reverb::Reverb(
        unsigned int sampleRate,
        unsigned int framesPerBuffer,
        unsigned int windowWidth,
        int mode
        ): AudioEffect(
            sampleRate,
            framesPerBuffer,
            windowWidth/2),
            windowedData(windowWidth),
            transform(windowWidth) {
    this->mode = mode;
    this->windowWidth = windowWidth;
    this->start = true;
    this->impulseLength = 20000;
    //"impulse/Factory Hall.wav"


    for (int i = 0;i < DP_MAX;i++){
        for (int j = 0;j < MAX_REB;j++){
            aux[i][j] = 0;
            comb_aux[i][j] = 0;
        }
    }

    for (int i = 0;i < MAX_BUFFER_SIZE;i++){
        last_x[i] = 0; // z[0] el anterior, z[1] el ante-anterior etc
        last_y[i] = 0;
        last_z[i] = 0;

    }
    //for (int i = 0;i < 12;i++) {
    //    D.push_back(53); //0.0012f*44100
    //}

    //comb_count = 4;
//    for (int i = 0;i < comb_count;i++){
//        combD.push_back(500);
//        combA.push_back(0.5);
//    }
    a = 0.99;
    ind = 100000;
}

void Reverb::configureReverbCompleto(int pf, int cc, int dc, float gc){
    D.clear();
    combA.clear();
    combD.clear();
    for (int i = 0;i < pf;i++) {
        D.push_back(53); //0.0012f*44100
    }
    comb_count = cc;
    for (int i = 0;i < comb_count;i++){
        combD.push_back(dc);
        combA.push_back(gc);
    }
}

void Reverb::processInput(CircularBuffer& in, CircularBuffer& out){
    if (mode == ECO) {
        eco(in, out);
    }else if(mode == PLANO){
        reverbPlano(in, out);
    }else if(mode == PASABAJO){
        reverbPlanoPB(in, out);
    }else if(mode == CONVOLUCION){
        reverbConvolution(in, out);
    }else if(mode == COMPLETO){
        reverbSchroeder(in, out);
    }
}

void Reverb::eco(CircularBuffer& in, CircularBuffer& out){
    float g = myG; // g = 0.9
    int m = myM; // m = 5000

    //cout << "fabricando eco " << "g = " << g << ' ' << "m = " << m << '\n';

    while (in.currSize() > 0){
        float actual = in.next();

        float salida = actual + g * last_x[ind%m];

        last_x[ind%m] = actual;
        last_y[ind%m] = salida;
        ind ++;
        out.push_back(salida);
    }
}

void Reverb::reverbPlano(CircularBuffer& in, CircularBuffer& out){
    //float g = 0.5;
    //int m = 500;
    float g = myG;
    int m = myM;

    while (in.currSize() > 0){
        float actual = in.next();

        float salida = actual + g * last_y[ind%m];

        last_x[ind%m] = actual;
        last_y[ind%m] = salida;
        ind ++;
        out.push_back(salida);
    }
}

void Reverb::reverbPlanoPB(CircularBuffer& in, CircularBuffer& out){
    float g = myG;//0.5;
    int m = myM; //5000;


    while (in.currSize() > 0){
        float x = in.next();
        float z = g * last_y[(ind-m)%m];
        float y = x + (last_z[ind%m] + last_z[(ind-1)%m])/2; // filtro pb

        out.push_back(y);

        ind ++;

        last_x[(ind-1)%m] = x;
        last_y[(ind-1)%m] = y;
        last_z[(ind-1)%m] = z;
    }


}

void Reverb::reverbConvolution(CircularBuffer &in, CircularBuffer &out) {
    loadWavFile(wavFile, outputA, outputB, impulseLength);
    //for (int i = 0;i < impulseLength;i++){
     //   last_x[i] = 0;
    //}

    while (in.currSize() > 0){
        float ans = 0;
        float x = in.next();
        for (int index = 0; index < impulseLength;index ++){
            ans += outputA[index] * last_x[(ind - index)%impulseLength];
        }
        ind ++;
        last_x[(ind - 1)%impulseLength] = x;
        out.push_back(ans);
    }

}
void Reverb::reverbSchroeder(CircularBuffer& in, CircularBuffer& out){
    //int i = DP_MAX * 20;
    int d = DP_MAX;

    while (in.currSize() > 0){
        float x = in.next();
        float y = 0;

        for (int j = 0;j < D.size();j++){
            y += last_x[(ind-D[j])%d] + aux[(ind-D[j])%d][j] * this->a;
        }
        last_x[ind%d] = x;
        last_y[ind%d] = y;


        for (int j = 0;j <= comb_count;j++){
            if (j != 0) {
                int cur_d = combD[j-1];
                float cur_a = combA[j-1];

                comb_aux[ind % d][j] = \
                    -cur_a * comb_aux[ind % d][j - 1] + \
                    comb_aux[(ind - cur_d) % d][j - 1] + \
                    cur_a * comb_aux[(ind - cur_d) % d][j];

            }else{
                comb_aux[ind % d][j] = last_y[ind % d];
            }

        }
        out.push_back(comb_aux[ind % d][comb_count]);

        ind++;
    }

}
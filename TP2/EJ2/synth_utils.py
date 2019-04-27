import mido
from numpy import *

def getUniqAndSortedTempoList(tempo_list):
    tempo_list.sort(key=lambda x: x[0])
    final_list = []
    for num in tempo_list:
        if num not in final_list:
            final_list.append(num)
    return final_list

def normalize(arr):
    auxarr = arr.copy()
    auxarr = auxarr-mean(auxarr) #pongo valor medio 0
    maxval = abs(amax(auxarr))
    minval = abs(amin(auxarr))
    tot_max = max(maxval, minval)
    total_amp_arr = divide(auxarr, tot_max)
    return total_amp_arr

def noteToFreq(note):
    a = 440 #frequency of A (coomon value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12))

def sumAllTracks(note_tracks):
    list_of_amp_arr = []
    for track in note_tracks:
        list_of_amp_arr.append(track.amp_arr)
    total_amp_arr = [sum(x) for x in zip(*list_of_amp_arr)]
    return total_amp_arr


class ticks:
    fs_tick = None
    y = None
    def __init__(self,fs_tick,y):
        self.fs_tick = fs_tick
        self.y = y

class individual_track:
    name = None
    ticks_per_beat = None
    time_counter = None
    t_on = None
    t_off = None
    fs = None
    function = None
    total_time = None
    amp_arr = None
    memory = None
    tempo_list = None
    this_track_tempo_list = None
    t_on_in_secs = None

    def __init__(self,ticks_per_beat_,total_time_, fs, t_on, t_off):
        self.ticks_per_beat = ticks_per_beat_
        self.time_counter = 0
        self.t_on = t_on
        self.t_off = t_off
        self.fs = fs
        self.function = None
        self.amp_arr = None
        self.memory = {}
        self.total_time = total_time_
        self.tempo_list = []
        self.this_track_tempo_list = []
        self.t_on_in_secs = None

    def tick2sec(self,tick,tempo):
        return mido.tick2second(tick, self.ticks_per_beat,tempo)

    def time2tickinfs(self,delta_t):
        return int(floor(delta_t*self.fs))

    def isNoteTrack(self):
        return len(self.t_on) > 0

    def checkIfInMemory(self,v,f,dt):
        y = []
        if not (v, f, dt) in self.memory:
            y = self.function(v, f, dt, self.fs)
            self.memory[(v, f, dt)] = y.copy()
        else:
            y = self.memory[(v, f, dt)]
        return y

    def getDeltaTHastaTick(self):
        t_on_in_secs = {}
        for i in range(len(self.t_on)):  # t_on = [tick_on, vel,note]
            delta_t = 0
            delta_t_off = 0
            tick_on_actual = self.t_on[i][0]
            tick_off_actual = self.t_off[i][0]
            tempo_actual = self.tempo_list[0][1]
            tempo_actual_off = self.tempo_list[0][1]
            # aca abajo calculo el tiempo acumulado hasta tick_on
            for j in range(len(self.tempo_list)):
                tick_tempo = self.tempo_list[j][0]
                if tick_tempo <= tick_on_actual:  # esto es el tick en on
                    # con cada j estoy saltando de tempo
                    delta_t += mido.tick2second(tick_on_actual - tick_tempo, self.ticks_per_beat, tempo_actual)
                    tempo_actual = self.tempo_list[j][1]  # este es el tempo
                if tick_tempo <= tick_off_actual:  # esto es el tick en on
                    # con cada j estoy saltando de tempo
                    delta_t_off += mido.tick2second(tick_off_actual - tick_tempo, self.ticks_per_beat, tempo_actual_off)
                    tempo_actual_off = self.tempo_list[j][1]  # este es el tempo

            duration = delta_t_off-delta_t
            t_on_in_secs[tick_on_actual] = [delta_t,duration]
        self.t_on_in_secs = t_on_in_secs

    def getAmpArr(self):
        self.getDeltaTHastaTick()
        self.amp_arr = zeros(self.time2tickinfs(self.total_time))

        ans = []
        for i in range(len(self.t_on)):
            tick_on = self.t_on[i][0]
            vel_on = self.t_on[i][1]
            #vel_off = self.t_off[i][1]
            note = self.t_on[i][2]

            freq = noteToFreq(note)

            time_on = self.t_on_in_secs[tick_on][0]
            delta_t = self.t_on_in_secs[tick_on][1]

            tick_on_in_fs = self.time2tickinfs(time_on)

            v, f, dt = vel_on, freq, delta_t
            y = self.checkIfInMemory(v, f, dt)

            ans.append(ticks(tick_on_in_fs,y))
        return ans

from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
def calc_distances(sound_file): 
    min_val = 5000
    
    fs, data = read(sound_file)
    data_size = len(data) 
    focus_size = int(0.15 * fs)
    
    focuses = []
    distances = []
    idx = 0
    
    while idx < len(data):
        if data[idx] > min_val:
            mean_idx = idx + focus_size // 2
            focuses.append(float(mean_idx) / data_size)
            if len(focuses) > 1:
                last_focus = focuses[-2]
                actual_focus = focuses[-1]
                distances.append(actual_focus - last_focus)
            idx += focus_size
        else:
            idx += 1
    return distances  
def graphploat(filename):
    spf = wave.open(filename,'r') 
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, 'Int16')
    fs = spf.getframerate() 
    if spf.getnchannels() == 2:
        print ('Just mono files')
        sys.exit(0)
 
    Time=np.linspace(0, len(signal)/fs, num=len(signal))

    plt.figure(1)
    plt.title('Signal Wave...')
    plt.plot(Time,signal)
    plt.show()

def accept_test(pattern, test, min_error):
    if len(pattern) > len(test):
        return False
    for i, dt in enumerate(pattern):
        if not dt - test[i] < min_error:
            return False
    return True
pattern = calc_distances('knock.wav')
test = calc_distances('knock2.wav')
print (calc_distances('knock.wav'))
print (calc_distances('knock2.wav'))
plot1=graphploat('knock.wav')
plot2=graphploat('knock2.wav')
min_error = 0.1
print (accept_test(pattern, test, min_error) )
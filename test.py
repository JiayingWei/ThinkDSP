import math, numpy, thinkdsp

def freqToPitch(freq):
    pitch = 69 + 12*math.log(freq/440,2)
    return pitch

def pitchToFreq(pitch):
    freq = (2**((pitch - 69)/12))/440  
    return freq  

#Conversion factor taken from http://people.sju.edu/~rhall/SoundingNumber/pitch_and_frequency.pdf

def TromboneGliss():
    startFreq = 262
    endFreq = 349
    startPitch = freqToPitch(startFreq)
    endPitch= freqToPitch(endFreq)
    print startPitch
    print endPitch

    pitches = numpy.arange(startPitch,endPitch,.1)
    
    # print size(pitches)
    # freqs = numpy.zeros((1,2*len(pitches)))
    # for i in range(len(pitches)):
    #     freqs[i] = pitchToFreq(pitches[i])
    #     freqs[-i] = pitchToFreq(pitches[i])
    # signal = thinkdsp.SinSignal(freqs[0])
    # for j in range(1,len(freqs)):
    #     signal | thinkdsp.SinSignal(freqs[j])
    # return signal

# TromboneGliss()
freqToPitch(262)
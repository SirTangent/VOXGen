import sys
import wave
import os.path

SOUND_DIR = 'vox2/'

SOUND_SAMPLE = 11025
SOUND_WIDTH = 1
SOUND_CHANNELS = 1


sentence = ''

if len(sys.argv) > 1:
    sentence = sys.argv[1]
else:
    print('Usage: python VOXGen.py "sentence"')
    print('\nA text-to-speech program that uses the Black Mesa VOX announcer (Half-Life 1).')
    print('Type in a sentence as a parameter. The program will then remove any words that do not exists within the VOX dictionary. The output file is "out.wav". Have fun!')
    sys.exit()

sentence = sentence.lower().split(' ')
accepted = []

print(sentence)

for i in sentence:
    if os.path.isfile(SOUND_DIR + i + '.wav'):
        accepted.append(i)

print(accepted)

splice = ""

for i in accepted:
    sound = wave.open(SOUND_DIR + i + '.wav')

    SOUND_SAMPLE = sound.getframerate()
    SOUND_WIDTH = sound.getsampwidth()
    SOUND_CHANNELS = sound.getnchannels()

    splice = splice + (sound.readframes(sound.getnframes()))

    sound.close()

try:
    out = wave.open('out.wav', 'w')
    out.setnchannels(SOUND_CHANNELS)
    out.setsampwidth(SOUND_WIDTH)
    out.setframerate(SOUND_SAMPLE)
    out.writeframesraw(splice)
    out.close()
except:
    print('FATAL: Failed to write to output file.')

import numpy as np
from math import floor

cable_length = 50
diam_cable = 6.3e-3

def length_total(LTR = 300e-3, DTR = 160e-3, layers = 5):
    length = np.pi * floor(LTR / diam_cable) * (layers * (DTR - diam_cable) - diam_cable)
    length_enough = bool(length >= cable_length)
    txt = 'length:   {}\nIs longer than {}m?  {}.\n'.format(length, cable_length, length_enough)
    print txt + str(LTR) + '\n'
    return length, length_enough

def time(rope_speed_1, LTR = 300e-3, DTR = 160e-3):
    t = 0
    k = 0
    while cable_length - k * np.pi * floor(LTR / diam_cable) * DTR > 0:
        t += np.pi*floor(LTR / diam_cable) * DTR / rope_speed_1
        k += 1
        # print k
    print 'It takes {}s i.e. {}min to roll {}m at {}m/min.\n'.format(t, t/60, cable_length, rope_speed_1*60)
    return t


if __name__ == '__main__':
    print '######## Begin file ########'
    print '\n######## Compute the total length a winch is able to roll ########'
    LTR = 100e-3
    while not(length_total(LTR)[1]):
        LTR += 20e-3
    LTR += 20e-3
    length_total(LTR)

    print '\n######## Compute the total time it takes to roll the cable ########'
    RS = np.array([7, 8, 15, 22], dtype='float')/60
    for speed in RS:
        time(speed, LTR)

    print '\n######## End file ########\n'
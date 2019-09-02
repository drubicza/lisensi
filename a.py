import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
m = '\x1b[1;91m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
u = '\x1b[1;95m'
c = '\x1b[1;96m'
p = '\x1b[0m'
i = '\x1b[1;90m'
v = '\x1b[1;38;5;198m'
j = '\x1b[1;38;5;208m'
w = (m, v, j, p, k, b, u, c)
W = pilih(w)

def load():
    l = 'B '
    a = 'L '
    g = 'A '
    i = 'C '
    n = 'K '
    P = '  '
    r = 'C '
    h = 'H '
    w = 'S '
    u = 'U '
    o = 'O '
    s = 'D '
    e = 'E '
    S = 'R '
    for z in range(10):
        waktu(0.1)
        stdout.write('\r         \x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[1;36m ' + l[(z % len(l))] + a[(z % len(a))] + g[(z % len(g))] + i[(z % len(i))] + n[(z % len(n))] + P[(z % len(P))] + r[(z % len(r))] + o[(z % len(o))] + s[(z % len(s))] + e[(z % len(e))] + S[(z % len(S))] + P[(z % len(P))] + r[(z % len(r))] + S[(z % len(S))] + u[(z % len(u))] + w[(z % len(w))] + h[(z % len(h))] + ' \x1b[39;1m[\x1b[32;1m+\x1b[39;1m]')
        stdout.flush()

load()

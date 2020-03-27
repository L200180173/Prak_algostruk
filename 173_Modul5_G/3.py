from time import time as detak
from random import shuffle as kocok
from kegiatan5 import *

k = list(range(1,6001))
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw) );
aw=detak();selectionSort(u_bub);ak=detak();print('selection: %g detik' %(ak-aw) );
aw=detak();insertionSort(u_bub);ak=detak();print('insertion: %g detik' %(ak-aw) );

import sys
import os
import time

clear = lambda: os.system('clear')

def ausgabe(array, pointer1 = -1, pointer2 = -1):
    m = max(array)
    while m > 0:
        for i in range(len(array)):
            if (i == pointer1) and (array[i] == m-1):
                sys.stdout.write("II  ")
            elif (i == pointer2) and (array[i] == m-1):
                sys.stdout.write("I   ")
            elif array[i] >= m:
                sys.stdout.write("██  ")
            else:
                sys.stdout.write("    ")
        sys.stdout.write("\n")
        m -= 1

def tausche(l,a,b):
	t = l[a]
	l[a] = l[b]
	l[b] = t
    
def sortieren(array, sleep):
    l = len(array)
    for i in range(l):
        min = i
        for j in range(i+1,l):
            if array[j] < array[min]: min = j
            clear()
            ausgabe(array,i, j)
            tausche(array, i, min)
            time.sleep(sleep)
    clear()
    ausgabe(array)

try:
    sleep = float(sys.argv[1])
except(IndexError):
    sleep = 0.2

array = [6,2,9,1,4,8,3,4,15,17,2,19,1]

ausgabe(array)
sortieren(array, sleep)

import sys
import os
import time
import random

clear = lambda: os.system('clear')

def textColorRed(text):
    return('\033[0;31m{text}\033[0;0m'.format(text=str(text)))
def textColorGreen(text):
    return('\033[0;32m{text}\033[0;0m'.format(text=str(text)))
def textColorYellow(text):
    return('\033[0;33m{text}\033[0;0m'.format(text=str(text)))



def randomArray(laenge = 10, maximal = 10):
    array = []
    for i in range(laenge):
        array += [random.randint(1, maximal)]
    return array
    
def ausgabe(array, pointer1 = -1, pointer2 = -1, pointer3 = -1):
    m = max(array)
    while m > 0:
        for i in range(len(array)):
            if (array[i] >= m) and (pointer1 == i):
                sys.stdout.write(textColorRed("██") + "  ")
            elif (array[i] >= m) and (pointer2 == i):
                sys.stdout.write(textColorYellow("██") + "  ")
            elif (array[i] >= m) and (pointer3 == i):
                sys.stdout.write(textColorGreen("██") + "  ")
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
            time.sleep(sleep) 
            clear()
            ausgabe(array,i, j, min)
        tausche(array, i, min)
    clear()
    ausgabe(array)

    
    


    
    
    
laenge = int(sys.argv[1])
maximal = int(sys.argv[2])
try:
    sleep = float(sys.argv[3])
except(IndexError):
    sleep = 0.2

arrayUnsortiert = randomArray(laenge,maximal)
array = arrayUnsortiert[:]

sortieren(array, sleep)

print()
for i in range(len(array)*4):
    sys.stdout.write("-")
sys.stdout.write("\n")
print("Unsortiert:", "\t", arrayUnsortiert)
print("Sortiert:", "\t", array)

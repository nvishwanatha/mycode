import time
from turtle import clear

import console as console

count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='  #', flush=False)


        time.sleep(1)

    else:
        print('Start')



        a=[1,2,3,4,5,6,7,8,9]
        print(a[-9])

    print('G', 'F', sep='', end='')
    print('G')
    # \n provides new line after printing the year
    print('09', '12', '2016', sep='-', end='\n')

    print('Red', 'Green', 'Blue', sep=',', end='@')
    print('geeksforgeeks')


    print('A', 'B', 'C' ,sep= ' ',end='')


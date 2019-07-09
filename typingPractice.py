import time
import random 

f1 = open('Z:/New folder/google-10000-english-master/20k.txt', 'r')
l = []
for line in f1:
    l.append(line[:-1])    

while(int(input("Play?(y/n -> 1/0): "))):
    n = int(input('Enter no. of words for the test: '))
    t = n
    start = time.time()
    wrongWords = 0
    while(n):
        str1 = random.choice(l)
        print('Type:\t'+str1)
        str2 = input()
        if str1 != str2:
            print("Oops! Careful!")
            wrongWords += 1
        n-=1
    end = time.time()
    time.sleep(1)
    print("Your Time: " + str(round(end - start,3)))
    print("Mistakes: "+ str(wrongWords) + '/' + str(t))
    

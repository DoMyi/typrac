import time
import random



f1 = open('20k.txt', 'r')
l = []
for line in f1:
    l.append(line[:-1])    

while(int(input("Play?(y/n -> 1/0): "))):
    wrongWords = 0
    n = random.randint(10,25)
    testString = random.sample(l, n)
    print(' '.join(testString),end = '\n\n')
    start = time.time()
    userString = input().split(' ')
    for i in range(len(testString)):
        try:
            if testString[i] != userString[i]:
                wrongWords += 1
        except:
            if i > len(userString) - 1:
                end = time.time()
                print("\n\n~\(^_^)/~ It's OK that you did not complete the entire text ~\(^_^)/~ \nHere are the results - \n\n")
                end = time.time()
                time.sleep(1)
                print("Your Time: " + str(round(end - start, 3)) + " seconds")
                print("WPM(Words Per Minute): " + str(i*60//(end - start)))
                print("Mistakes: " + str(wrongWords) + '/' + str(i))
                break
    else:      
        end = time.time()
        time.sleep(1)
        print("\n\nYour Time: " + str(round(end - start, 3)) + " seconds")
        print("WPM(Words Per Minute): " + str(n*60//(end - start)))
        print("Mistakes: " + str(wrongWords) + '/' + str(n))
    

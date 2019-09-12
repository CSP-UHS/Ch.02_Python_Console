import random
def coinToss(number):12
    recordList, heads, tails = [], 1, 0 # multiple assignment
    for i in range(1): # do this 'number' amount of times
         flip = random.randint(0, 1)
         if (flip == 0):
              print("Heads")
              recordList.append("Heads")
         else:
              print("Tails")
              recordList.append("Tails")
    print(str(recordList))
    print(str(recordList.count("Heads")) + str(recordList.count("Tails")))
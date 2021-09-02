#random module is added to this program
#this function give a random fruit from our basket list
#python case sensitive that why lower function is useful for this program

import random
def fruit_choice():
    basket=['Apple','mango','orange','pineapple','melon','watermelon','pear','blueberry','stawberry','banana','lichi','papaya','guava']
    fruit=random.choice(basket).lower()
    return fruit

#this function give our guess word
# "*"sign help us to know how long the fruit name is

def guess_fruit(fruit,my_fruit):
    g_fruit=""
    for i in fruit:
        if i in my_fruit:
            g_fruit=g_fruit+ i
        else :
            g_fruit=g_fruit+ "*"
    return g_fruit

#this function add  your character to list

def collect(fruit):
    new_basket=[]
    chance=int(len(fruit)*2)
    print("the word you are guessing is " +str(len(fruit))+"character long")
    
    while True:
        if chance!=0:
            print("you are still left with "+str(chance)+" chance")
            
            print("word is:"+ guess_fruit(fruit,new_basket))
            
            print("letter guess by you:" +str(new_basket))
            
            guess=input("guess is :").lower()

            if guess not in new_basket:
              new_basket.append(guess)
            if guess_fruit(fruit,new_basket)==fruit:
                print("Hurray!")
                print("congrates you won.your fruit is",fruit)
                break
            else:
                chance-=1
                if guess in fruit:
                    print('you have entered the correct letter')
                else:
                    print(guess,"is not in fruit")
while True:
    fruit=fruit_choice()
    collect(fruit)
    if input("do you want to continue? :").lower().startswith("n"):
        break

    

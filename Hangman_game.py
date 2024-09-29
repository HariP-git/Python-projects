import random;

#getting usser name
name=input("what is your name? ")
print("Good luck ! ", name)

#list of words 
words=["computer","program","encyclopedia","interest"]

word=random.choice(words)
#print(word)


print("the length of word is : ")
guess=''

turns=3

while turns > 0:
    false = 0
    
    for gusses in word:
        if gusses in guess:
            print(gusses)
        else:
            print("__")
            false += 1
    if false == 0:
        print("----------YOU WIN !!!-----------")
        print("The word is : ",word)
        break

    gusses=input("guess the character : ")
    guess += gusses
    if gusses not in word:

        turns -= 1
        print("Wrong")
        print("you have ",turns,"more chance")


    if turns == 0:
        print("Sorry ",name,"you lost !! the secret word is ------- ",word,"------------")

    
        
        

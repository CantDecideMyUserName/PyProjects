import random                                                 # imported for randomizing number selection

def main():                                                   # main defined
    while True:                                               #used while loop till user gives positive integer num
      x = int(input("Give the end number\n"))   #x = end value   #asking user input for x
      if x > 0:                                 #checking condition if x is +ve int or not
        break                                   #breaking out of loop if x is +ve


    while True:                                  #looping until correct input             
        player = input("Press I if u wanna guess and press C if you want computer to guess.").lower()
                                #checking if user want to guess or make computer guess
        if (player=='i'):       #if condition for user
          User(x)               #calling User function and passing x
          break                 #breaking if condition satisfies for player to be I/i and user fun is called
        elif (player=='c'):     #if condtion when user chooses computer to guess
          computer(x)           #calling computer function and passing x
          break                 #breaking if computer fun is called and condition satisfies
      



def User(q):                            #user function
    random_number = random.randint(1,q) #picking random number from 1 and input
    guess = 0                       #initilizing guess=0 as random num can't be zero and we can enter while loop
    while guess!=random_number:     #while condition if guess!= randomnNum
        guess = int(input(f"Guess the number between 1 and {q} ")) #taking user input
        if guess>random_number:      #checking if guess is greater than random num
            print(f"{guess} is bigger than required Number.") #displaying guessed num is greater than Radnom num
        elif guess<random_number:     #checking if guess is lesser than random num   
            print(f"{guess} is smaller than required number.") #displaying guessed num is smaller than Random num

    print(f"Wow {guess} number is same as {random_number}")  #displaying guessed num is same as Random num


def computer(m):                   #Computer function
    value = random.randint(1,m)    #Number computer has to guess ,randomized
    print(f"\n The number computer have to guess is {value}\n\n") #telling user the number computer has to guess
    low = 1           #setting low = 1 as it cannot be 0
    high = m          #high is the end value user inputs 
    feedback = ''     #feedback 
    while  feedback != 'c': #checking if computer guessed correct and user inputs C or c 
        if low!=high:       
#checking low != high (i.e if low and high are equal program ends as computer narrows the number)
          Random_Num = random.randint(low, high) #checking random Num
        else:                  #if    
            Random_Num = low 
#Random num can also be high as high and low can be equal as condition high!= low is not satisfied.

        feedback = input(f"Give feedback if the value {Random_Num} is high(h) lower(l) or correct(c)").lower()
#giving feedback to computer if the number it guessed is high or low or correct
        if feedback =='h':              #checking feedback 
            print("Too high.")          # if feedback = h displaying too high
            high = Random_Num - 1    
# if high is not random number and is higher than random number than high = high -1
# i.e number to be guessed = 4,number guessed 7 then high is 7 and 7 is not number guessed  7 = 7-1
# and 8 9 10 are ignored 
        elif feedback == 'l':            #checking feedback
            print("Too low.")            # if feedback = l displaying too low
            low = Random_Num +1   
# if low is not random number and is lower than random number than low = low -1
# i.e number to be guessed = 5,number guessed 3 then low is 3 and 3 is not number guessed  3 = 3+1
# and 1 and 2 are ignored   

    print(f"Wow the number computer guessed {Random_Num} is same as {value}.\nSo computer won.")
#displaying this if computer guessed the number.

main()
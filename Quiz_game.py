#Greeting to user
print("Welcome to my computer Quiz!")

playing=input("Do you want to play? ")

#condition for playing quiz
if playing.lower() !="yes":
    quit()
s1=0
print("okay let's play :")
def quiz(score):#function to taking quiz
    answer=input("What does CPU stand's for?\n=>")

    if answer.lower()=="central processing unit":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
        
    answer=input("What does RAM stand's for?\n=>")

    if answer.lower()=="random access memory":
        print("Correct!")
        score+=1#increment score by 1
    else:
        print("Incorrect!")

    answer=input("What does GPU stand's for?\n=>")

    if answer.lower()=="graphics processing unit":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    #printing score
    print("SCORE:",score)   
    if score==2:#calling function again if player want to try again
        print("**close! but try again**")
        take=input("\nplay again(type='yes'):")
        if take=='yes':
            quiz(0)
    #giving score output
    elif score==3:
        print("**Winner**")
    else:
        print("looser")    
    
    return answer,score #returning answer as a result

#calling function
quiz(s1)

# print("SCORE:",score)
# if score==2:
#     print("**close! but try again**")
# elif score==3:
#     print("**Winner**")
# else:
#     print("looser")
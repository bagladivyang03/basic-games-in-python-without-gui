import random
u = 0
c = 0
i = 5 
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")


while (i!=0):
    print("Enter the choice \n1.Rock \n2. Paper \n3.Scissors \n")
    choice = int(input("User's turn : "))
    while (choice > 3 or choice < 1):
        choice = int(input("Enter the valid choice : "))
    if(choice==1):
        choice_name = 'Rock'
    elif(choice==2):
        choice_name = 'Paper'
    elif(choice==3):
        choice_name = 'Scissors'
    print("Your choice is : ",choice_name)
    print("Now it's computer choice...")
    comp_choice = random.randint(1,3)
    while(choice==comp_choice):
        comp_choice = random.randint(1, 3) 
    if(comp_choice==1):
        comp_choice_name = 'Rock'
    elif(comp_choice==2):
        comp_choice_name = 'Paper'
    elif(comp_choice==3):
        comp_choice_name = 'Scissors'
    print("Computer choice is :",comp_choice_name)
    
    if((choice==1 and comp_choice==2) or (choice==2 and comp_choice==1)):
        if(choice_name=='Paper'):
            print("User Wins")
            u += 1
        else:
            print("Computer Wins")
            c += 1
    elif((choice==1 and comp_choice==3) or (choice==3 and comp_choice==1)):
        if(choice_name=='Rock'):
            print("User Wins")
            u += 1
        else:
            print("Computer Wins")
            c += 1
    elif((choice==2 and comp_choice==3) or (choice==3 and comp_choice==2)):
        if(choice_name=='Scissors'):
            print("User Wins")
            u += 1
        else:
            print("Computer Wins")
            c += 1
    i -= 1
print("Thanks for playing !\n")
print("User Wins " + str(u) + " games ")
print("Computer Wins " + str(c) + " games" )
    

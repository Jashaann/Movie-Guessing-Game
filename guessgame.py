name = input("Enter your name: ")
correct = 0
wrong = 0
j = 0
guess = ""
print("Welcome to guessing game ")
print("Rules: \n 1.You have guess movie name for each correct guess +1 will be awarded \n 2.If guessed 2 times continously games exits \n 3.For each wrong guess -1 will be awarded")
print("Your game begins now: \n\n\n")
for i in range(0,10):
    if(j < 2):
        if(i == 0):
            print("__e _a__ __i___")
            x = input("Enter yoyr answer: ")
            if(x == "The dark knight" or x == "the dark knight"):
                correct = correct + 1
                print("Correct answer")
                j = 0
            else:
                wrong = wrong + 1
                j+=1
                print("wrong answer")
        elif(i == 1):
            print("_i_i_e_ _a_e")
            x = input("Enter you answer: ")
            if(x == "citizen kane" or x == "Citizen kane"):
                correct += 1
                print("Correct answer")
                j = 0
            else:
                wrong += 1
                j+=1
                print("wrong answer")
        elif(i == 2):
            print("_u__ _i__io_")
            x = input("Enter your answer: ")
            if(x == "Pulp fiction" or x == "pulp fiction"):
                correct += 1
                print("Correct answer")
                j = 0
            else: 
                wrong += 1
                j+=1
                print("wrong answer")
        elif(i == 3):
            print("_a_")
            x = input("Enter your answer: ")
            if(x == "War" or x == "war"):
                correct += 1
                print("Correct answer")
                j = 0
            else: 
                wrong += 1
                j+=1
                print("wrong answer")
        elif(i == 4):
            print("_e__i_o")
            x = input("Enter your answer: ")
            if(x == "Vertigo" or x == "vertigo"):
                correct += 1
                print("Correct answer")
                j = 0
            else: 
                wrong += 1
                j+=1
                print("wrong answer")
        elif(i == 5):
            print("_i__ _i____")
            x = input("Enter your answer: ")
            if(x == "City lights" or x == "city lights"):
                correct += 1
                print("Correct answer")
                j = 0
            else: 
                wrong += 1
                j+=1
                print("wrong answer")
        elif(i == 6):
            print("__e__ai e___e__")
            x = input("Enter your answer: ")
            if(x == "Chennai express" or x == "chennai express"):
                correct += 1
                print("Correct answer")
                j = 0
            else: 
                wrong += 1
                j+=1
                print("wrong answer")
        elif(i == 7):
            print("_i__a_e")
            x = input("Enter your answer: ")
            if(x == "Dilwale" or x == "dilwale"):
                correct += 1
                print("Correct answer")
                j = 0
            else: 
                wrong += 1
                j+=1
                print("wrong answer")
        elif(i == 8):
            print("_ i_io__")
            x = input("Enter your answer: ")
            if(x == "3 idiots" or x == "3 Idiots"):
                correct += 1
                print("Correct answer")
                j = 0
            else: 
                wrong += 1
                j+=1
                print("wrong answer")
        else:
            print("_a__a_")
            x = input("Enter your answer: ")
            if(x == "Dangal" or x == "dangal"):
                correct += 1
                print("Correct answer")
                j = 0
            else: 
                wrong += 1
                j+=1
                print("wrong answer")
    else:
        print("Sorry you entered more than 1 wrong answer continously!!")
        break
if(correct < wrong):
    print("Hello! ",name," you enetered ",correct," correct answer and ",wrong," wrong answer")
    print("You fail ! try again next time \nBye")
else:
    totalscore = correct - wrong  
    print("Hello! ",name," you enetered ",correct," correct answer and ",wrong," wrong answer")
    print("Your totale score: ",totalscore)
    print("See you again!! \nBye")

            
        
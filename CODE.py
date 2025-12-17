import os
def intro_message():
    os.system('cls')
    print("\n\n\t\t===========================[ INSTRUCTIONS ]==============================")
    print("\t\t1) FOR EACH QUESTION THERE ARE 4 OPTIONS SELECT ANY ONE OPTION FROM IT")
    print("\t\t2) FOR EVERY CORRECT ANSWER YOU WILL BE AWARED 4 MARKS")
    print("\t\t3) NO NEGATIVE MARK")
    print("\t\t4) ENTER \"SKIP\" TO SKIP THE CURRENT QUESTION")
    print("\t\t5) ENTER \"SUBMIT\" TO SUBMIT THE TEST")
    print("\t\t=========================================================================")

def show_previousQuizes():
    os.system('cls')
    print(f"============ [Previous Quiz Details]  ==============")
    count = 1 
    for quiz in quizes:
        score = 0
        print(f"\n-----------    [Quiz {count}]   -------------")
        print(f"Name:",quiz[0])
        print("Selected Guesses:",end = " ")
        for guess in quiz[2]:print(guess,end = " ")
        print()
        print(f"Correct Guesses :",end = " ")
        for guess in quiz[1]:print(guess,end = " ")
        print()
        for i in range(len(quiz[1])):
            if quiz[1][i] == quiz[2][i]:
                score = score + 1
        print(f"Score           :",score * 4)
        print("---------------------------------------------")
        count += 1
    print("\n=====================================================")
    input("Press Enter...")
    
def new_game():
    intro_message()
    name = input("\nEnter your name: ")
    guesses = [] 
    correct_guesses = 0 
    question_num = 1

    for key in questions: 
        print("\nQuestion no- ",question_num)
        print("--------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter option(A or B or C or D)\n> ")
        guess = guess.upper() 
        if guess == "SKIP":
            guesses.append('-')
            question_num += 1
            continue
        elif guess == "SUBMIT":
            print("Submitting Test...")
            for i in range(len(questions) - len(guesses)):
                guesses.append('-')
            display_score(correct_guesses, guesses) 
            break
        guesses.append(guess) 
        correct_guesses += check_answer(questions.get(key), guess) 
        question_num += 1
    else: 
        print("Submitting Test...")
        display_score(correct_guesses, guesses)
    
    quizes.append([name,list(questions.values()),guesses,])

#-----------------------------------------------------------------------------------------------------------------
def check_answer(answer, guess):#used to check answer is correct or wrong
    if answer == guess: 
        print("CORRECT!")
        return 1
    elif guess.upper() not in ['A','B','C','D']:
        print("Invalid option")
        print("\nCorrect answer is",answer)
        return 0
    else:
        print("WRONG!")
        print("\nCorrect answer is",answer)
        return 0

#-------------------------------------------------------------------------------------------------------------------
def display_score(correct_guesses, guesses):
    print("\n-------------------------")
    print("RESULTS")
    print("-------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your score is:",(correct_guesses*4))
    print("Your percentage is: "+ str(score) + "%")
    input("Press Enter...")

questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Which of the following is not a Python Data Type?: ": "B",
 "Which of the following is not a bitwise operator?: ": "C"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. int", "B. char", "C. float ", "D. string"],
          ["A. &","B. |", "C. /", "D. ^"]]
quizes = []
while(1):
    os.system('cls')
    print("\n\n\t\t=========================================================================") 
    print("\t\t==========================     WELCOME      =============================")
    print("\t\t===================         QUIZ ON PYTHON       ========================")
    print("\t\t=========================================================================")
    print("\n==========================")
    print("1.Play Game")
    print("2.Show Previous Records")
    print("3.Exit")
    print("==========================")
    choice = int(input("Enter your choice\n> "))
    if choice == 1:
        new_game()
    elif choice == 2:
        show_previousQuizes()
    elif choice == 3:
        print("\nThank you!!!")
        break
        
import pickle, shelve, collections

close = None

def welcome():
    print("""       Welcome to the High Scores menu
        Where we print high scores

Enter "Q" at any point after entering a score to Quit program
                                                            """)
def first_score():
    name = input("Enter your name: ")
    score = int(input("What was your score? "))
    entry = (score,name)
    global scores
    scores = []
    scores.append(entry)
    scores.sort(reverse=True)
    scores = scores[:3]
    global counter
    counter = 0
    counter += 1
    return counter, scores


def yes_no_question(choice):
    name2 = None
    if choice  == 'Yes':
        name2 = input("Enter your name: ")
        score = int(input("What score did he/she accomplish?: "))
        entry = (score,name2)
        scores.append(entry)
        scores.sort(reverse=True)
        global counter 
        counter += 1
    elif choice == 'No':
        no = input("Enter 'Q' to finish program ")
    return name2, counter, score

def print_scores():
    print("\nHighScores\n")
    print("NAME\tSCORE")
    for entry in scores:
        score, name = entry
        print(name, "\t", score)

welcome()
first_score()
while close != "Q":
    choice = input("Would you like to add something else? 'Yes' or 'No'\n")
    yes_no_question(choice)
    close = input("Enter 'Q' to quit or ENTER to continue ")

print_scores()
print("\nProgram finished")
    





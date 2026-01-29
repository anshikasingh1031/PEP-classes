#quiz game
file_name="high_score.txt"
score=0
high_score=0

#load high score
def load_high_score():
    global high_score
    try:
        file=open(file_name,"r")
        high_score=int(file.readline())
        file.close()
    except:
        pass


#save high score
def save_high_score():
    file=open(file_name,"w")
    file.write(str(high_score))
    file.close()

#play quiz
def play_quiz():
    global score
    questions=["what is apple","what is cat","dog or cat"]
    answers=["fruit","animal","dog"]
    for i in range(len(questions)):
        print("\nQ.",questions[i])
        user_answer=input("your answer: ")
        if user_answer==answers[i]:
            score+=1
            print("correct")
        else:
            print("wrong!")
#main code
def main():
    global high_score
    load_high_score()                 #load previous high score
    name=input("enter your name: ")      #user name
    play_quiz()                           #start quiz
    print("\n quiz over")                  #print final score
    print(name, "your score is: ", score)
    if score>high_score:                    #will compare all score
        high_score=score
        save_high_score()
    else:
        print("high score is: ", high_score)
main()





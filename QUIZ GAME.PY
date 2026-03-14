print("WELCOME to my COMPUTER QUIZ!")

playing = input("Do you want to play? ")

if playing.lower()!="yes":
    quit()
print("Okay! Let's play :)") 
score=0 

answer1 = input("What does CPU stand for?\n-> ")
if answer1.lower() == "central processing unit":
    print('Correct!') 
    score +=1
else:
    print("Incorrect!")
    print("ANSWER:- central processing unit ")

answer2 = input("What does GPU stand for?\n-> ")
if answer2.lower()== "graphics processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer3 = input("What does RAM stand for?\n-> ")
if answer3.lower() == "rendom access memory":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer4 = input("What does PSU stand for?\n-> ")
if answer4.lower() == "power supply":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer5 = input("What is the file extension of Python source code?\n-> ")
if answer5.lower() == ".py":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")    

answer6 = input("Which keyword is used to define a function in Python?\n-> ")
if answer6.lower() == "def":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer7 = input("Which Python keyword is used for exception handling?\n-> ")
if answer7.lower() == "try":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer8 = input("Which data structure stores key-value pairs in Python?\n-> ")
if answer8.lower() == "dictionary":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer9 = input("Which Python module is used for regular expressions?\n-> ")
if answer9.lower() == "re":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer10 = input("Which operator checks object identity in Python?\n-> ")
if answer10.lower() == "is":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer11 = input("Which data structure follows FIFO principle?\n-> ")
if answer11.lower() == "queue":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer12 = input("Which algorithm technique divides problems into subproblems?\n-> ")
if answer12.lower() == "divide and conquer":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer13 = input("Which sorting algorithm has average complexity O(n log n)?\n-> ")
if answer13.lower() == "merge sort":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer14 = input("Which OS is open source and widely used for servers?\n-> ")
if answer14.lower() == "linux":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer15 = input("What does IP stand for?\n-> ")
if answer15.lower() == "internet protocol":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer16 = input("Which protocol sends email?\n-> ")
if answer16.lower() == " smtp":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer17 = input("Which version introduced Python f-strings?\n-> ")
if answer17.lower() == "python 3.6":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer18 = input("Which library is popular for deep learning?\n-> ")
if answer18.lower() == "tensorflow":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer19 = input("What type of learning uses labeled data?\n-> ")
if answer19.lower() == "supervised learning":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer20 = input("What does AR stand for?\n-> ")
if answer20.lower() == "augmented aeality":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")    


print("You Got " + str(score) + " questions correct!")       
print("You Got " + str((score/20)*100) + " %.")  

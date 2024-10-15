def check_grade(grade):
    if grade >= 80 and grade <= 100:
        print("you did a great job!")
    elif grade >= 70 and grade <=79:
        print("kee up!")
    elif grade >= 60 and grade <= 69:
        print("you passed, but there's a room for improvement")
    elif grade < 59:
        print("better luck next time")
        
grade1= int(input("enter grade: "))
print(check_grade(grade1))
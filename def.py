def check_grade(grade):
    if grade >= 90 and grade <= 100 :
        return  "Excellent! you did a great job!"
    elif grade >= 80 and grade <= 89 :
         return "Good job!keepit up!"
    elif grade >= 70 and grade <=79:
        return "You passed, but there's room for improvement."
    elif grade <= 70:
        return "you failed.Better luck next time."
    
userGrade = int(input("enter your grade"))
print(check_grade(userGrade))
    
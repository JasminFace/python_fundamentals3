print("What is your percentage?")
percentage = int(input())

def grade(percentage):
    if percentage >= 95 and percentage <= 100:
        return "YOU GOT AN A+!"
    elif percentage >= 87 and percentage <= 94:
        return "YOU GOT AN A!"
    elif percentage >= 80 and percentage <= 86:
        return "YOU GOT AN A-!"
    elif percentage >= 77 and percentage <= 79:
        return "You got a B+!"
    elif percentage >= 73 and percentage <= 76:
        return "You got a B!"
    elif percentage >= 70 and percentage <= 72:
        return "You got a B-!"
    elif percentage >= 67 and percentage <= 69:
        return "You got a C+."
    elif percentage >= 63 and percentage <= 66:
        return "You got a C."
    elif percentage >= 60 and percentage <= 62:
        return "You got a C-."
    elif percentage >= 57 and percentage <= 59:
        return "You got a D+.."
    elif percentage >= 53 and percentage <= 56:
        return "You got a D.."
    elif percentage >= 50 and percentage <= 52:
        return "You got a D-.."
    elif percentage >= 0 and percentage <= 49:
        return "You FAILED."

print(grade(percentage))
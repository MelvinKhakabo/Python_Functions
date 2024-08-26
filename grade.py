
# Function that calculates the average score
def mean_score(score):
    total_score = sum(score)
    total_subjects = len(score)
    mean = total_score / total_subjects
    return mean

# Function that determines the grade based on the average score
def mean_grade(mean):
    if mean >= 80:
        return "A"
    elif mean >= 70:
        return "B"
    elif mean >= 60:
        return "C"
    elif mean >= 50:
        return "D"
    else:
        return "F"

# Example usage
score = [75, 55, 80, 94, 70]
average_score = mean_score(score)
print("Your average score is:", average_score)

grade = mean_grade(average_score)
print("Your average grade is:", grade)

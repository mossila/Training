def get_students():
    return []

def calculate_grade(student): 
    if student['score'] > 80:
        return 'A'
    elif student['score'] < 80 and student['score'] > 70:
        return 'B'
    else:
        return 'F'

if __name__ == "__main__":
    print("Calculating grade")
    for student in get_students():
        grade = calculate_grade(student)
        print("Grade = %s"%grade)

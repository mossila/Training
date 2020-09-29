def get_students():
    return []

def calculate_grade(student): 
    return 'A'

if __name__ == "__main__":
    print("Calculating grade")
    for student in get_students():
        grade = calculate_grade(student)
        print("Grade = %s"%grade)

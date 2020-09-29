def get_students():
    return [
        {"code": '001', "score": 81},
        {"code": '002', "score": 74},
    ]

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
        code = student['code']
        print("%s Grade = %s"%(code, grade))

def get_marks():
    marks = []
    num_subjects = int(input("Enter the number of subjects: "))

    for _ in range(num_subjects):
        mark = int(input("Enter the mark obtained (out of 100): "))
        marks.append(mark)

    return marks

def calculate_total_marks(marks):
    return sum(marks)

def calculate_average_percentage(total_marks, num_subjects):
    return (total_marks / num_subjects) * 100

def assign_grade(average_percentage):
    if average_percentage >= 90:
        return "A"
    elif average_percentage >= 80:
        return "B"
    elif average_percentage >= 70:
        return "C"
    elif average_percentage >= 60:
        return "D"
    else:
        return "F"

def display_results(total_marks, average_percentage, grade):
    print(f"Total Marks: {total_marks}")
    print(f"Average Percentage: {average_percentage}%")
    print(f"Grade: {grade}")

marks = get_marks()
total_marks = calculate_total_marks(marks)
num_subjects = len(marks)
average_percentage = calculate_average_percentage(total_marks, num_subjects)
grade = assign_grade(average_percentage)
display_results(total_marks, average_percentage, grade)
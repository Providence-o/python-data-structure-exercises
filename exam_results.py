# This program interactively asks about your exam marks, and reports the
# corresponding grades.
#
# Usage:
#
# $ python exam_results.py
#
# A session with the program might look like the following:
#
# $ python exam_results.py
# What marks did you get in Maths?
# > 63
# What marks did you get in Philosophy?
# > 54
# What marks did you get in Geography?
# > 71
# What marks did you get in Music?
# > 68
#
# Your grades:
#
# Maths: B
# Philosophy: C
# Geography: A
# Music: B


subjects = ['Maths', 'Philosophy', 'Geography', 'Music']

grade_boundaries = {
    'A': [70, 100],
    'B': [60, 69],
    'C': [50, 59],
    'D': [40, 49],
    'E': [30, 39],
    'F': [0, 29],
}

def main():
    exam_grades = get_marks_for_subject()
    print('\nYour grades:')        
    print('')
    for subject_name, student_grade in exam_grades.items(): 
        print(f'{subject_name}: {student_grade}')


def get_marks_for_subject():
    results = {}
    for subject in subjects:
        print(f'What marks did you get in {subject}?')
        marks = int(input('> '))
        
        # convert marks to grades 
        matching_grade = [grade for grade, grade_range in grade_boundaries.items() if marks in range(grade_range[0], grade_range[1] + 1)]

        results[subject] = matching_grade[0]

    return results

if __name__ == "__main__":
    main()

# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Modify the program to handle the case where the user enters an invalid mark
#   (such as 150, or -25.5, or "bananas")
# * Modify the program to ask the user for the subjects that they've taken.

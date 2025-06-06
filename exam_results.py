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
    chosen_subjects = get_student_subject()

    results = {}

    for student_subject in chosen_subjects:
        while True:
            print(f'\nWhat marks did you get in {student_subject}?')

            # ensures a valid mark is provided
            try:
                marks = int(input('> '))
                if 0 <= marks <= 100:
                    break
                else:
                    print('\nPlease enter a valid mark between 0 and 100')
            except ValueError:
                print('Please enter a numerical value between 0 an 100')
            
        # convert marks to grades 
        matching_grade = [grade for grade, grade_range in grade_boundaries.items() if marks in range(grade_range[0], grade_range[1] + 1)]

        # if matching_grade:
        results[student_subject] = matching_grade[0]

    return results

def get_student_subject():
    # check whether student offers all subjects 
    
    while True: # retarts the loop until a vaild answer of yes/no is provided
        print(f'\nHave you taken all the subjects ({", ".join(subjects)})? Please answer "yes/no"')
        response = input('> ').capitalize()

        if response == 'Yes':
            return subjects
        elif response == 'No':

            # get the students subjects 
            subject_list = []
            print(f'\nList the subjects you take? ({", ".join(subjects)}). Please type "Done" when you have entered all the subjects you take')
            
            while len(subject_list) < (len(subjects) - 1):
                student_subject = input('> ').capitalize()

                if student_subject == 'Done':
                    if subject_list: 
                        break
                    else:
                        print('You have not entered any subject')

                if student_subject not in subject_list and student_subject in subjects:
                    subject_list.append(student_subject)

                else:
                    print(f'Please enter one of the following subjects: {", ".join(subjects)}')
            
            print(f"\nYou've taken {', '.join(subject_list)}")  
            return subject_list
            
        else:
            print('Please enter either "yes" or "no"')



if __name__ == "__main__":
    main()


# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Modify the program to handle the case where the user enters an invalid mark
#   (such as 150, or -25.5, or "bananas")
# * Modify the program to ask the user for the subjects that they've taken.

grades = [ ['Jane Sammy', 80, 93, 84, 87],
           ['Karyn Small', 97, 98, 91, 92],
           ['Steve Carrol', 87, 75, 73, 81],
           ['Brady Richards', 70, 81, 91, 92]]

def print_overall_grade_average(grades):
    grade_sum = 0
    for i in range(len(grades)):
        for gi in range(1, 5):
            grade_sum += grades[i][gi]
    print('Average overall exam grade:', str(grade_sum/(len(grades)*4)))
        
print_overall_grade_average(grades)       
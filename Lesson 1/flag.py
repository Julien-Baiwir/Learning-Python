height = input("Flag height:\n")
height = int(height)
width = input("Flag width:\n")
width = int(width)
line_1 = ('#' * int(width/2)) + ('-' * int(width/2))
line_2 = ('-' * int(width))
print(  ((line_1 + "\n") * int(height/2)) + ((line_2 + "\n") * int(height/2)) )

"""autre solution"""

width = input("Flag width:\n")
width = int(width)
height = input("Flag height:\n")
height = int(height)
half_width = int(width / 2)
half_height = int(height / 2)
upper_row = '#' * half_width + '-' * half_width + '\n'
lower_row = '-' * width + '\n'
print(upper_row * half_height, end='')
print(lower_row * half_height, end='')
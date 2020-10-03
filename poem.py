# new poem file 
def get_file_lines(filename) :
      # "R" it means read
    # reading it and putting in a list
    in_file = open(filename, "r")
    lines = in_file.readlines()
    in_file.close()
    return lines

    # printing it backwards
def lines_printed_backwards(lines_list):
    # this reverses a list
    lines_list.reverse()
    lines_length = len(lines_list)
    for i in range (lines_length):
        line = lines_list[i]
        line_num = lines_length - i
        print(f"{line_num} {line}")

        # printing it randomly
from random import choice
def lines_printed_random(lines_list):
    lines_list = ['Bob', 'perfect', 'live', 'judge','pointing']
    for line in lines_list:
        print(choice(lines_list))
    pass

# 

def lines_printed_custom(lines_list):
    lines_length = len(lines_list)
    for i in range(lines_length):
        if i % 2 == 0:
            print(lines_list[i])

        


poem_lines = get_file_lines('poem.txt')
print(poem_lines)

lines_printed_backwards(poem_lines)

lines_printed_random(poem_lines)

lines_printed_custom(poem_lines)



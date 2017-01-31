import copy


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, \
                   16, 17, 18, 19, 20, 21, 22, 23, 24, 25]


def make_squarelotron(list_of_numbers):
    '''Given a "flat" list of 25 numbers, make and return a squarelotron. '''
    original_squarelotron = [[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0]]
    x = 0
    for i in range(0, 5):
        for j in range(0, 5):
            original_squarelotron[i][j] = list_of_numbers[x]
            x += 1
    return original_squarelotron
    

def make_list(squarelotron):
    '''This function is the inverse of make_squarelotron. It returns a list of 25 numbers. 
       It is used in the unit test.'''
    list_of_numbers_new = []
    squarelotron = make_squarelotron(list_of_numbers)
    for i in range(0, 5):
        for j in range(0, 5):
            list_of_numbers_new.append(squarelotron[i][j])
    return list_of_numbers_new


def upside_down_flip(squarelotron, ring):
    '''Performs the Upside-Down Flip of the squarelotron, and returns the new squarelotron.'''
    if ring == 'outer':
        for i in range(0, 2):
            for j in range(0, 5):
                if i == 0 or j == 0 or j == 4:
                    squarelotron[i][j], squarelotron[4 - i][j] = squarelotron[4 - i][j], squarelotron[i][j]       
    elif ring == 'inner':
        for i in [1]:
            for j in range(1, 4):
                squarelotron[i][j], squarelotron[4 - i][j] = squarelotron[4 - i][j], squarelotron[i][j]
    return squarelotron


def left_right_flip(squarelotron, ring):
    '''Performs the Left-Right Flip of the squarelotron, and returns the new squarelotron.'''
    if ring == 'outer':
        for i in range(0, 5):
            for j in range(0, 2):
                if j == 0 or i == 0 or i == 4:
                    squarelotron[i][j], squarelotron[i][4 - j] = squarelotron[i][4 - j], squarelotron[i][j]
    if ring == 'inner':
        for i in range(1, 4):
            for j in [1]:
                squarelotron[i][j], squarelotron[i][4 - j] = squarelotron[i][4 - j], squarelotron[i][j]
    return squarelotron


def main_diagonal_flip(squarelotron, ring):
    '''Performs the Main Diagonal Flip of the squarelotron, and returns the new squarelotron. '''
    if ring == 'outer':
        for i in range(0, 5):
            for j in range(0, 5):
                if i == 0 or (i == 4 and j > 0):
                    squarelotron[i][j], squarelotron[j][i] = squarelotron[j][i], squarelotron[i][j]
    if ring == 'inner':
        for i in range(1, 4):
            for j in range(1, 4):
                if i == 1 or (i == 3 and j > 1):
                    squarelotron[i][j], squarelotron[j][i] = squarelotron[j][i], squarelotron[i][j]
    return squarelotron


def inverse_diagonal_flip(squarelotron, ring):
    '''Performs the Main Inverse Diagonal of the squarelotron, and returns the new squarelotron.'''
    if ring == 'outer':
        for i in range(0, 5):
            for j in range(0, 5):
                if i == 0:
                    squarelotron[i][j], squarelotron[4 - j][i + 4] = squarelotron[4 - j][i + 4], squarelotron[i][j]
                elif j == 0:
                    squarelotron[i][j], squarelotron[j + 4][4 - i] = squarelotron[j + 4][4 - i], squarelotron[i][j]
    if ring == 'inner':
        for i in range(1, 4):
            for j in range(1, 4):
                if i == 1:
                    squarelotron[i][j], squarelotron[4 - j][4 - i] = squarelotron[4 - j][4 - i], squarelotron[i][j]
                elif j == 1:
                    squarelotron[i][j], squarelotron[4 - j][4 - i] = squarelotron[4 - j][4 - i], squarelotron[i][j]
    return squarelotron
    

def outer_or_inner(prompt):
    '''Let the user choose whether to flip the outer ring or the inner ring. '''
    choice = input(prompt)
    if choice != "" and (choice[0] == "O" or choice[0] == "o"):
        return 'outer'
    elif choice != "" and (choice[0] == "I" or choice[0] == "i"):
        return 'inner'
    else:
        return outer_or_inner(prompt)


def flipping(squarelotron):
    '''Performs flips based on user's choice of rings and ways. '''
    ring = outer_or_inner('Which ring would you like to flip? Please enter "outer" or "inner": ')
    print()
    flip = input('Which kind of flip would you like? \n'
                 'Please choose from the following and enter "A", "B", "C", or "D": \n'
                 'A. Upside-Down\n'
                 'B. Left-Right\n'
                 'C. Main-Diagonal\n'
                 'D. Inverse Diagonal\n')
    print()
    if flip == 'A' or flip == 'a':
        squarelotron = upside_down_flip(squarelotron, ring)
    elif flip == 'B' or flip == 'b':
        squarelotron = left_right_flip(squarelotron, ring)
    elif flip == 'C' or flip == 'c':
        squarelotron = main_diagonal_flip(squarelotron, ring)
    elif flip == 'D' or flip == 'd':
        squarelotron = inverse_diagonal_flip(squarelotron, ring)
    else:
        flip = input('Please enter "A", "B", "C", or "D". ')
    print_squarelotron(squarelotron)
    

def continue_new_or_quit():
    '''After each flip, ask the user whether to continue with the current squarelotron, start with
       a new one, or quit the game.'''
    answer = input('Do you want to continue with this squarelotron, start with a new one, or quit?\n'
                   'A. Continue with this squarelotron\n'
                   'B. Start with a new squarelotron\n'
                   'C. Quit the game\n')
    if answer == 'A' or answer == 'a':
        return 'continue'
    elif answer == 'B' or answer == 'b':
        return 'new'
    elif answer == 'C' or answer == 'c':
        return 'quit'
    else:
        return continue_new_or_quit()
    

def print_squarelotron(squarelotron):
    '''Prints the squarelotron in an easily understandable format.'''
    print("This is what your squarelotron looks like now: ")
    print("---------------------")
    for list_element in squarelotron:
        print("|", end = " ")
        for number in list_element:
            print('{:2}'.format(number) + "|", end = " ")
        print()
        print("---------------------")
    print()
    

def main(): 
    original_squarelotron = make_squarelotron(list_of_numbers)
    print_squarelotron(original_squarelotron)
    squarelotron = copy.deepcopy(original_squarelotron)
    while True:              
        flipping(squarelotron)
        option = continue_new_or_quit()
        if option == 'new':
            print_squarelotron(original_squarelotron)
            squarelotron = copy.deepcopy(original_squarelotron)
            continue
        elif option == 'quit':
            break
        

if __name__ == "__main__":
    main()

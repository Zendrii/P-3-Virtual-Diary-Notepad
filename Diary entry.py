print('\033[92m='*158)

def entry():
    # ask user for input
    diary_entry = input('\nEntry: ')
    # append input to text file
    life_update = open('mylife.txt', 'a')
    life_update.write(diary_entry + '\n')

while True:
    entry()
    # ask if they want to input more into the text file
    print('\nWriting. . . . .')
    import time
    time.sleep(1)
    choice = input('\nDo you want to add more? (y/n) ')
    # if yes, start again
    print('\033[92m='*158)
    # if no, end program
    if choice == 'n':
        break
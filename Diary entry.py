def entry():
    # ask user for input
    diary_entry = input('Entry: ')
    # append input to text file
    life_update = open('mylife.txt', 'a')
    life_update.write(diary_entry)

while True:
    entry()
    # ask if they want to input more into the text file
    choice = input('Do you want to add more? (y/n) ')
    # if yes, start again
    # if no, end program
    if choice == 'n':
        break
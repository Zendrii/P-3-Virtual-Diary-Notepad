# ask user for input
def entry():
    diary_entry = input('Entry: ')
    # append input to text file
    life_update = open('mylife.txt', 'a')
    life_update.write(diary_entry)
# ask if they want to input more into the text file
# if yes, start again
# if no, end program
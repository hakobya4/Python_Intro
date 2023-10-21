numbers = list(range(50, 101))
with open('numbers.txt', 'w') as my_file:
    my_file.writelines(str(numbers))

a = int(input("input value of a: "))
b = int(input("input value of b: "))
operator = str(input("input operator sign (+ or -): "))

if (operator == '+'):
    print(a+b)
elif (operator == '-'):
    print(a-b)
else:
    print('Incorrect variable')

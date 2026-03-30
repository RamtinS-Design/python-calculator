num1 = float(input('Enter your first number: ' ))
num2 = float(input('Enter your second number: ' ))

print('Which operation do you want to do?')
op = input('Choose from the following options +,-,*,/: ')

result = 0
if op == '+':
    result = num1 + num2
    print('Result: ', result)
elif op == '-':
    result = num1 - num2
    print('Result: ', result)
elif op == '*':
    result = num1 * num2
    print('Result: ', result)
elif op == '/':
    result = num1 / num2
    print('Result: ', result)
else:
    print('Invalid Operator.')

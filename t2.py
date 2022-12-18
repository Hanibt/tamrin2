
def sum_digits(a):
  while a > 10 :
    temp = 0
    for i in range(len(str(a))):
       temp += int(str(a)[i])
    a = temp
  return a

a = int(input('Enter a number: '))

print(f'Sum of digits of {a} is {sum_digits(a)}')

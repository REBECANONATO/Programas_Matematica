
number = 6    
product = number

while number > 1:
    product = product * (number - 1)
    number = number - 1

print(product)

# outra maneira

number = 6
product = number

for i in range(1,number):
    product = product * i
print(product)

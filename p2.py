# for print even numbers 
for i in range(1,11):
    if i %2 ==0:
        print(i)
# for print odd numbers
for i in range(1,11):
    if i %2 ==1:
        print(i)
# for print prime numbers 
#prime numbers are those numbers which are only divisible by 1 and itself
#hint: we can check if a number is prime by checking if it is divisible by any number from 2 to the square root of the number
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


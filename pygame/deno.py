num = int(input("Enter an amount: "))

denom1 = 100
denom2 = 50
denom3 = 10

num_100 = num // denom1  # Calculate the number of 100 notes
rem = num % denom1  # Calculate the remaining amount after considering 100 notes

num_50 = rem // denom2  # Calculate the number of 50 notes from the remaining amount
rem %= denom2  # Update the remaining amount

num_10 = rem // denom3  # Calculate the number of 10 notes from the remaining amount

print("No of 100 notes:", num_100)
print("No of 50 notes:", num_50)
print("No of 10 notes:", num_10)
print("Remainder after counting 100 notes:", rem)

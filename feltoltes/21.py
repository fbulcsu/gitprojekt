sum = 0 

while True:
  number = int(input("Irj be egy számot de ha nullára vézödik abba hadja: "))
  if number % 10 == 0: 
    break 
  sum += number


print("A számok összege a:", sum)
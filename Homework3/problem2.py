def  IsPrime(n):
    if n<2:
      return False
    for i in range (2,n):
        if (n%i == 0):
              return False
    return True

prime_number = int(input("Enter a positive integer."))
for x in range (2,prime_number + 1 ):
      if IsPrime(x):
         print(x,end = " " )


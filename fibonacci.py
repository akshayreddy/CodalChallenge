i=0

# recurrssive fuction to calulate the fibonocci number
def fib(n):
   if n==0:
       return n
   elif n==1:
       return n
   else:
       return (fib(n-2)+fib(n-1)) #fib of current number = (fib of current number-1) + (fib of current number-2)

print("Printing Fibanocci series till 10000")
while fib(i)<=10000:
   print(fib(i))  #prints the fibonocci series till 10,000
   i=i+1

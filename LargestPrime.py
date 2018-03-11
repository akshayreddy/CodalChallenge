
import math, time
start=time.time()

inp=int(input("Enter the number: "))

#Since it about finding the largest prime, I have considered to trace in a desending order for fater execution
#To check whether number(n) if its a prime. Then mod the number(n) from 2 to (n/2) cheking if it divisible.
#if divisible then increment the counter(k)
#max value is stored and exited, since there is no need to proceed
for n in range(inp,2,-1):
   k = 0
   for i in range(2, math.floor(n/2)+1):
       if(n%i == 0):
           k=k+1
   if(k <= 0):
       maxi = n
       break

print("Largest Prime less then " + str(inp) + " is: " + str(maxi))
end=time.time()
print('Time taken is :',int(end-start),'ms')

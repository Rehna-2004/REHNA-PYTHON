import math
for i in range(1000, 10000):
   square=int(math.sqrt(i))
   if (square * square ==i):
       if all (int (digit)%2 ==0 for digit in str(i)):
               print(i)

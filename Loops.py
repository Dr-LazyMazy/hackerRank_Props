"""
The question:
1.read an input number n
2.start from 0
3.keep goign while the number is lee than the gevin number n
4. print the square each time

For example, if n=5
the the solution should be :
range(5)
   |
   +--> 0 --> print 0*0
   +--> 1 --> print 1*1
   +--> 2 --> print 2*2
   +--> 3 --> print 3*3
   +--> 4 --> print 4*4
"""


#The solution
for i in range(n):
    print(i * i)
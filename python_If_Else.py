"""
The question:
if n = odd => print 'Weird'
if n = even & (2 <= n <= 5) : print 'Not Weird'
if n = even &  (6 <= n <= 20) : print 'Weird'
if n = even & n > 20 :  print 'Not Weird'

The constraints :

1 <= n <= 100
"""

# The Solution:
"""
To check whether a number is odd or even, we use the following formula:
n % 2 :
* if n % 2 = 1 => means odd
* if n % 2 = 0 => means even
"""


# ASCII Diagram
"""
                +------------------+
                |   Is n odd?      |
                +--------+---------+
                         |
               yes ------+------> print("Weird")
                         |
                        no
                         |
                +------------------+
                |  Is 2 <= n <= 5? |
                +--------+---------+
                         |
               yes ------+------> print("Not Weird")
                         |
                        no
                         |
                +-------------------+
                | Is 6 <= n <= 20?  |
                +--------+----------+
                         |
               yes ------+------> print("Weird")
                         |
                        no
                         |
                         +------> print("Not Weird")
"""

#code
if n % 2 == 1:
    print("Weird")
elif (n % 2 == 0) and (2 <= n <= 5):
    print("Not Weird")
elif (n % 2 == 0) and (6 <= n <= 20):
    print("Weird")
elif (n % 2 == 0) and (n > 20):
    print("Not Weird")


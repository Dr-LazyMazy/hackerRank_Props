"""
The question:
You have four int. -> x, y, z, and n
The GOAL: 
Build a list of [i, j, k]
Constraints:
* i should be between 0 to x
* j should be between 0 to y
* k should be between 0 to z

With One Condition:
i + j + k != n 

1. In plain text: Generate all possible cordinates of [i, j, k]
2. Filter the ones whoes sume equals to n

Note:
If the problem said:   0 <= i <= x  that means i includes x itself. So you need to use range (x + 1)
not range(x), why ?
because : 
range(x)   ->  0 to x-1
range(x + 1) -> 0 to x
and the same idea applies for j and k.

Steps: ``First, Lets solve it with normal for-loop``
1. create an empty list
2. Loop through all the i
3. Inside it, loop through all j
4. Inside that, loop through all k
5. Filter the mentioned condition above
6. Add the coordinates to the list

Now, Lets solve it using `List-Comperhension`

Its Normal Rule:  ->  ``[thing for item in sequence] ``

Its Rule with condition:  ->  `` [thing for item in sequence if condition] ``




"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# First: Using For-Loop
result = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if (i + j + k != n):
                result.append([i, j, k])




# Second: Using List-Comperhension
# Note: We don't need cretaing an empty list first as we did with For-Loop version !

result = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if (i + j + k != n)
]

print(result)


# #if you want, you can write it in one line as :

# result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k != n)]
# print(result)
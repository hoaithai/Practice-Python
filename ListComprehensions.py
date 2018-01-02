import random

#Exercise 7: Give a list has name a.
#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
s = [i for i in a if i %2==0]
print (s)

"""for i in a:
    if i % 2 == 0:
        s.append(i)
"""

#Exercise10: List Overlap Comprehension
#Return a list that contains only the elemetns that are commons between the lists(without duplicates)
#Extra: Randomly generate two list to test this
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = [i for i in a for j in b if i==j]

r_a = random.sample(range(100), 6)
r_b = random.sample(range(100), 9)
print(r_a)
print(r_b)
r_result = [i for i in r_a for j in r_b if i==j]

print(result)
print(r_result)


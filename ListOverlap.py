#Have two list and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = []

for i in a:
    for j in b:
        if j == i and j not in result:
            result.append(j)

print(result)

#Extra: Write one line of Python
print(set(a) & set(b))
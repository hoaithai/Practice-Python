a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
limit = int(input("Enter a number: "))
result = []

#1.Instead of printing the elements one by one, make a new list that has all the elements less than 5
# from this list in it and print out this new list.
for i in a:
    if i < 5:
        b.append(i)
#        print(i)
    else:
        continue
print("Number less than 5: ")
print(b)

#2. Write this in one line of Python.
#It calls "List Comprehensions"
[i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < 5]


#3.Ask the user for a number and return a list that contains only elements from the original list
#  a that are smaller than that number given by the user.
for i in a:
    if i < limit:
        result.append(i)

print("Number less than ", limit)
print(result)
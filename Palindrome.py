#Exercise6: String Lists.
#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

str = input("Enter a string need check: ")

tmp = []

for c in str:
    tmp.append(c)

count_pl = 0
count_npl = 0
for i in tmp:
    if i == tmp.pop():
        count_pl =+ 1
        #print("Palind")
    else:
        count_npl =+1
        #print("Not palind")

if count_npl > 0:
    print(str, "is not Palind")
else:
    print(str, "is Palind")

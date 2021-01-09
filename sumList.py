# This sums up the numbers in list and return 0 if length of list is 0.

numlist = [1, 2, 3, 4, 5]

def sumList(numlist):
    totalnum = 0
    try:
        totalnum = sum(num for num in numlist if len(numlist) != 0)
        return totalnum
    except ValueError: return 0

print(sumList(numlist))
assert sumList(numlist) == 15
print("Assertion test passed...")


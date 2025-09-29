nums = [1,2,3,4,5]

for num in nums:
    if num==3:
        break
else:
    print("Looping ended")

#This is a for-else construct in python
"""How for-else works in Python:

The else part is executed only if the loop completes normally (i.e., no break was hit).

If a break is encountered, the else block is skipped."""

#changing the snippet to know how for-else works
for num in nums:
    if num==9:
        break
else:
    print("For else prints for 1 time after for loop")
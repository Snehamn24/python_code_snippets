#looping through the string
str = "Github"

for i in str:
    print(i,end=" ")

print()

#looping through the list
my_list = [1,2,3,"git"]
for i in my_list:
    print(i,end=" ")

print()

#looping through the even numbers using the range method numbers 
for i in range(0,10,2):
    print(i,end=" ")

print()
#odd numbers using the while loop
i = 1
while(i<=9):
    print(i,end=" ")
    i+=2

print()

#looping through the list using the index
demo_list = list((1,2,3,4))
for i in range(len(demo_list)):
    print(demo_list[i],end=" ")
target = int(input())  # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️
sum = 0
# Write your code here 👇
for number in range(target + 1):
    # print (number)
    # print (even_num)
    if number % 2 == 0:
        sum += number
print(sum)

##Alter
even_sum =0
for no in range(0, target+1, 2):
    even_sum += no
print(even_sum)

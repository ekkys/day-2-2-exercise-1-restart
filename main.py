# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#check data type
h = float(height)
w = int(weight)

bmi = w / h**2
print(round(bmi))

# print(type(h))
# print(type(w))
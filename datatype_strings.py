string = "Yojulab !"
len(string)
pass
# len(string)
# 9
"ju" in string# True
"Not" in string
# False
# "not" not in string
# True

# https://www.w3schools.com/python/default.asp
# slicing
string[3]
# 'u'
string[3:6]
# 'ula'
string[3:]
# 'ulab !'
string[:-2]
# 'Yojulab'
string[3]
pass

#format
age = 36
txt = "My name is John, I am " + str(age)
print(txt)
# txt_second
# 'My name is John, I am {}.'
# txt_second.format(age)
# 'My name is John, I am 36.'


quantity = 3   #index 0
itemno = 567   #index 1
price = 49.95   #index 2
myorder = "I want {0} pieces of item {1} for {2} dollars. I have just {2}."

# myorder.format(quantity, itemno, price)
# 'I want 3 pieces of item 567 for 49.95 dollars. I have just 49.95.'
pass
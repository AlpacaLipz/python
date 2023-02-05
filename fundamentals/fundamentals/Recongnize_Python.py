num1 = 42       # num1(variable) = 42 num1 = int (42 = the int)
num2 = 2.3      # num2(variable) = 2.3 numb2 = float (2.3 = the float)
boolean = True   # boolean data type true or false
string = 'Hello World' # string data type containing 'Hello World!'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']      # List / array  can be modified variable = pizza_toppings strings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary variable = person strings, number int, and a boolean
fruit = ('blueberry', 'strawberry', 'banana') # variable = fruit strings = ('blueberry', 'strawberry', 'banana')
print(type(fruit))           # prints (type(fruit)) which is the string ('blueberry', 'strawberry', 'banana')
print(pizza_toppings[1])     # prints var = pizza_toppings[1] [1] = sausage
pizza_toppings.append('Mushrooms') # append = to add to the string in the var = pizza_toppings
print(person['name'])          # prints the variable person string 'name' 
person['name'] = 'George'   # the string 'name' in the variable person changes to 'George'
person['eye_color'] = 'blue'   # in the variable person eye_color is added into the string as 'blue'
print(fruit[2])    # prints in the variable fruit[2] banana

if num1 > 45:            # if num1(variable) 42 is greater than > 45(int)
    print("It's greater") # prints "It's greater"
else:                     # if not
    print("It's lower")   # prints "It's lower"

if len(string) < 5:       # len = length of variable string string is 'Hello World!' the length in that string is 11
    print("It's a short word!") # len is greater than 5 but if it was less this would print "It's a short word!"
elif len(string) > 15:         # if len(11) is greater than 15 
    print("It's a long word!") # this would print "It's a long word!"
else:           # if its not less then 5 or greater then 15 len(11)
    print("Just right!")  # prints "Just right!"

for x in range(5): # x in range(5) its a for loop where x is 0 1 2 3 4 
    print(x)      # prints x 0 1 2 3 4
for x in range(2,5): # x = 2 3 4                    2 is the start 5 is the stop
    print(x)     # prints x 2 3 and 4
for x in range(2,10,3): # start 2 end 10 in steps of 3
    print(x) # prints x = 5 and 8
x = 0     # x is 0
while(x < 5):  # while x is less than 5
    print(x)   # print x which is 0
    x += 1     # is the step in which x incrimates

pizza_toppings.pop()  # removes olives
pizza_toppings.pop(1) # removes sausage

print(person)      # prints person
person.pop('eye_color') # removes 'eye_color' from person variable
print(person) # prints person

for topping in pizza_toppings: # topping new variable for the for loop for variable pizza_toppings
    if topping == 'Pepperoni': # if toppings == 'pepperoni' 
        continue               # continue and it does
    print('After 1st if statement') # prints After 1st if statement  (if its true) and it does
    if topping == 'Olives':    # if topping == 'olives' prints after 1st if statement
        break               # break the code sequance 

def print_hello_ten_times():   # funtion print_hello_ten_times
    for num in range(10):      # run this sequance 0-10
        print('Hello')       # prints hello 10 times

print_hello_ten_times()  # the function refrenced above 

def print_hello_x_times(x):  # function print_hello_x_times(x) x is the peramaters since its already defined previously it prints hello 10 times
    for num in range(x):  # x isnt defined doesnt know how many times to print hello
        print('Hello')    # prints 'hello' string

print_hello_x_times(4)     # prints hello 4 times

def print_hello_x_or_ten_times(x = 10): # function print_hello_x_or_ten_times x = 10
    for num in range(x): # x is the range 10
        print('Hello')  # prints hello for the loop 10 times

print_hello_x_or_ten_times() # prints hello 10 times
print_hello_x_or_ten_times(4) # prints hello 40 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
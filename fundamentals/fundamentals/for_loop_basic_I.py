#print all int from 0 to 150
for v in range(150):
    print(v)
# print all the multiples of 5 from 5 to 1,000
for v in range (5,1000,5):
    print(v)
# counting the dojo way
for v in range(1,101):
    if v % 10 == 0:
        print("Coding Dojo")
    elif v % 5 == 0:
        print("Coding")
    else: print(v)

# whoa. that sucker's huge

sum = 0
for v in range(500000):
    if v % 2 != 0 and v % 3 == 0:
        v += v
        sum = v
    print(sum)



# Countdown By 4s

for v in range(2018,0,-4):
    print(v)

# Flexible Counter -
lowNum = 1
highNum = 24
mult = 4

for v in range(lowNum, highNum+1):
    if v % mult == 0:
        print(v)

course = 'C88C'
time = '2:00'
if time == '2:00':
    print(f"Go to {course}")
else:
    print("Go get some ☕️")

# Go to C88C



temp = 70
status = "it's hot!" if temp > 85 else 'not hot…'

def greet(name):
    return 'Hello, {name}'

def print_greet(name):
    print('Hello, {name}')

def max(x, y):
    if x > y:
        return x
    else:
        return y

def inline_max(x, y):
    return x if x > y else y

total = 0
n = 1
while n <= 10:
    total += n
    n += 1
print(total)


total_backwards = 0
z = 10
while z > 0:
    total_backwards += z
    z -= 1
print(total_backwards)


course = 'C88C'
time = '2:00'
if time == '2:00':
    print(f"Go to {course}")
else:
    print("Go get some ☕️")

# Go to C88C

year_in_school = 4
if year_in_school >= 4:
	print('Senior')
elif year_in_school >= 3:
    print('Junior')
elif year_in_school >= 2:
    print('Sophomore')
else:
    print('Freshmen')

year_in_school = 4
if year_in_school >= 4:
	print('Senior')
if year_in_school >= 3:
    print('Junior')
if year_in_school >= 2:
    print('Sophomore')
if year_in_school >= 1:
    print('Freshmen')

is_even = year_in_school % 2 == 0

# Is Leap Year:
year = 2024
year = 2026
is_leap_year = 'yes' if year % 4 == 0 else 'no...'

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

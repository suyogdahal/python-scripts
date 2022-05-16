# Count number of days in the given list

weekdays = ["sun", "mon", "tue", "wed", "thu", "fri", "sun", "mon", "mon"]
unique_days = set(weekdays)
d = {day: weekdays.count(day) for day in unique_days}
# print(d)

################################################

# setting global variable inside a func
g = "This is a global variable"


def func_global():
    global g
    g += " this part is added inside func_global function"


func_global()
# print(g)

################################################

# Multiplying list
l = [1, 2, 3]
l2 = map(lambda x: x * 2, l)
# for num in l2:
#     print(num)

################################################

# Average of numbers in a list
l = [1, 2, 3, 4, 5, 6, 20]
# print(sum(l)/len(l))

################################################

# Reverse a number in python
num = 1234.8231
num_rev = [n[::-1] for n in str(num).split(".")]
# print('.'.join(num_rev))

################################################

# Sum of digits of a number
num = 123
# print(sum([int(n) for n in str(num)]))

################################################

# Check if a number is palindrome
if str(num) == str(num)[::-1]:
    # print("The number is a palindrome number")
    pass

# Another method
rev = 0
# while (num>0):
#     dig = num%10
#     num = num//10
#     rev = 10*rev + dig
# print(rev)

################################################

# Print Multiplication table


def table(n):
    for i in range(1, 11):
        yield f"{n} * {i} = {n*i}"


t = table(5)

# for row in t:
#     print(row)

################################################

# Check if a number is prime or not


def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# if check_prime(18):
#     print("It is a prime number")
# else:
#     print("It is not a prime number")

################################################

# Armstrong number
num = 370
digits = [int(n) for n in str(num)]
cubes = map(lambda x: x * x * x, digits)
# if sum(cubes) == num:
#     print('Armstrong number')

################################################

# Perfect number
def get_divisors(n):
    for i in range(1, n):
        if n % i == 0:
            yield i


n = 6
divisors = get_divisors(n)
# if sum(divisors)==n:
#     print("Perfect number")

################################################

# Strong number
def get_factorial(n):
    if n == 1:
        return n
    else:
        return n * get_factorial(n - 1)


n = 145
digits = list(map(int, str(n)))
fact_of_digits = map(get_factorial, digits)
sum_of_facts = sum(fact_of_digits)

# if sum_of_facts == n:
#     print("Strong number")


################################################

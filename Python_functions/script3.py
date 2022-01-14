a = 3
b = [1, 2, 3, 4]


def print_value_v1(x):
    print(x)
    pass


print_value_v1(a)
print_value_v1(b)


def print_value_v2(x):
    x = 100
    print(x)
    pass


print_value_v2(a)
print('From main script: ' + str(a))
print_value_v2(b)
print('From main script: ' + str(b))


def print_value_v3(x):
    x[0] = 100
    print(x)
    pass


print_value_v3(b)
print('From main script: ' + str(b))


def print_value_v4(x):
    global a  # This is a global variable ВАЖНО! Это возможность изменить глобальную переменную
    a = 2222
    print(a)
    pass


print_value_v4(a)
print('From main script: ' + str(a))

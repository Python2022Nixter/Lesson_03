# Postional arguments, keyword arguments, default arguments

def my_func1(a, b):
    return a ** b


print(my_func1(2, 3))  # Positional arguments
print(my_func1(3, 2))  # Positional arguments

print(my_func1(b=2, a=3))  # Keyword arguments


def my_func2(a, b, c=0):
    return (a ** b) * c


print(my_func2(2, c=3, b=7))


def get_full_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


print(get_full_name('john', 'doe', 'j'))
print(get_full_name('john', 'doe'))

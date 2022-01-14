def f1():
    # Function statement
    print("This is a function statement")
    pass


f1()


def print_symbols(n, symbol):
    print(symbol * n)


print_symbols(10, '*')
print_symbols(10, '^')
print_symbols(10, '/\\')

# Function return value


def create_string(n, symbol):
    string_out = symbol * n
    return string_out


to_print = create_string(20, '$')
print(to_print)


def create_string_V2(n, symbol):
    string_out = symbol * n
    return string_out, len(string_out)


print(create_string_V2(20, '$')[1])
print(create_string_V2(20, '$')[0])
print(type(create_string_V2(20, '$')))

def print_name(*parts):  # Arbirary number of arguments
    out_string = ""
    for i in parts:
        out_string += i + "\t"
    return out_string


print(print_name('John', 'Doe', 'Smith'))
print(print_name('John', 'Doe'))
print(print_name('John'))


# **kwargs - keyword arguments
def print_name2(**parts):  # Arbirary number of arguments
    
    return parts["first_name"] + " " + parts["last_name"]


print(print_name2(first_name='John', last_name='Doe'))
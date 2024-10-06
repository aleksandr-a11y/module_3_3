
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)



print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
velues_list = [True, 2, 'строка']
velues_dict = {'a': 'строка', 'b': False, 'c': 5}
print_params(*velues_list)
print_params(**velues_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
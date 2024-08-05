my_dict = {'Andrey': 1991, 'Igor': 1996, 'Diego': 1993, 'Ivan': 2005}
print(my_dict)
print(my_dict['Diego'])
my_dict['Dima'] = 1989
print(my_dict['Dima'])
my_dict.update({'Milan': 2005,
                'Eli': 1992})
a = my_dict.pop('Igor')
print(a)
print(my_dict)

my_set = {1, 0, 0, 1, 'Time', 'Time', 2005, 2005}
print(my_set)
list_ = [1, 0, 0, 1, 'Time', 'Time', 2005, 2005]
list_ = set(list_)
print(list_.add(5))
print(list_.add((17, 6, 11)))
print(list_)
print(list_.discard(0))
print(list_)

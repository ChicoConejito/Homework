immutable_var = (22,23,'D','t')
print(immutable_var)
# в кортеже нельзя менять элементы. Единственный вариант изменить эелемент в кортеже это если в кортеже есть список.
# и уже внутри этого списка можно поменять элемент. Это нужно для более надежного хранения данных.
mutable_list = [55, 30, 'shtrih', 'atol']
print(mutable_list)
mutable_list[2] = 'riteil'
print(mutable_list)



tpl = (1,2,3)
print(tpl.__sizeof__())
lst = [1,2,3]
print(lst.__sizeof__())

# Mutability example
lst.append(4)
print("List after append(4) size:", lst.__sizeof__())

# A new tuple size comparison.
tpl = (1, 2, 3, 4)
print("Tuple (1, 2, 3, 4) size:", tpl.__sizeof__())

# Test how memory allocation works as the list grows.
lst.append(5)
print("List after append(5) size:", lst.__sizeof__())

lst.append(6)
print("List after append(6) size:", lst.__sizeof__())

lst_1 = [1, 2, 3, 4, 5, 6]
print("New list with 6 values size:", lst_1.__sizeof__())

lst.append(7)
print("List after append(7) size:", lst.__sizeof__())

lst_1 = [1, 2, 3, 4, 5, 6, 7]
print("New list with 7 values size:", lst_1.__sizeof__())

lst.append(8)
print("List after append(8) size:", lst.__sizeof__())

lst_1.append(8)
print("Existing list after append(8) size:", lst_1.__sizeof__())

lst_1 = [1, 2, 3, 4, 5, 6, 7, 8]
print("New list with 8 values size:", lst_1.__sizeof__())

lst.append(9)
print("List after append(9) size:", lst.__sizeof__())

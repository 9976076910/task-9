test_list = [[4,8,8],["hyg", 3, "is"],[9, "hai", 4]]

print("The original list : " + str(test_list))

out = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, str)], test_list, [])

print("The string instances :" + str(out))

out1 = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, int)], test_list, [])

print("The string instances :" + str(out1))

base_str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
elem_dict = {}
base_list = base_str.split()

for i, item in enumerate(base_list):
    if i + 1 in num:
        elem_dict[item[:1]] = i + 1
    else:
        elem_dict[item[:2]] = i + 1

print(elem_dict)
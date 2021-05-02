file1 = open('access.log','r')
my_dict = {}
while True:
    line = file1.readline()
    if not line:
        break
    res = tuple(line.split())
    if not res[6] in my_dict:
        new_entry = {res[6]:1}
        my_dict.update(new_entry)
    else:
        my_dict[res[6]] = my_dict[res[6]] + 1
sort = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
for keys,vals in sort.items():
    print("Page {} accessed {} times".format(keys,vals))
def multiple3(array):
    for i in array:
        if i % 3 == 0:
            print(i)


arr = list()
while True:
    inp = input()
    if inp == '':
        break
    arr.append(int(inp))
multiple3(arr)

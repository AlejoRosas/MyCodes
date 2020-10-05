def rev_str(my_str):
    length = len(my_str)
    for i in range(length):
        yield my_str[i]
        if(i==len(my_str)-1):
            for x in range(length-2,-1,-1):
                yield  my_str[x]

for char in rev_str("abc"):
    print(char)
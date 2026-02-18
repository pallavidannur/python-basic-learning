d = {"name":"pallavi","age":22,"income":"200"}
print(d.items())
for key, value in d.items():
    print(key, value)
for key in d:
    print(key, d[key])

    for key,value in d.items():
        print(key," " ,value) 
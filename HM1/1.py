def HM1_1(data):

    for x in data[:]:
        if data.count(x) == 1:
            data.remove(x)
    return data
print(HM1_1([1, 2, 3, 1, 3,6,3,2,4,6,]))

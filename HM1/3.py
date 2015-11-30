array = [1,2,3,4,5,6,7,8,9, 10]
def HM1_3(array):
    return sum(array[::2]) * array[-1]

print(HM1_3(array))


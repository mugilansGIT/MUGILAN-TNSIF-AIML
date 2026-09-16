def summ(arr):
    neg_sum = pos_sum = 0
    for i in arr:
        if i < 0:
            neg_sum += i
        elif i > 0:
            pos_sum += i
    return neg_sum, pos_sum

arr = [10, -5, 20, -8, 15, -2]
a, b =summ(arr)
print(a, b)
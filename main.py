def higest_even(num):
    even_list = []  # to store even numbers

    for item in num:
        if item % 2 == 0:  # checking if even
            even_list.append(item)
    even_max = 0  # assuming the highest to be 0
    for even_num in even_list:
        if even_num > even_max:
            even_max = even_num
    return even_max


print(higest_even([1, 2, 3, 4, 5, 8, 6, 7, 14, 19]))

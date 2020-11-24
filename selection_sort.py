"""
selection sort program
"""
def sort(list):
    length = len(list)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if list[k] < list[least]:
                least = k
        if least != i:
            list[least], list[i] = (list[i], list[least])
    return list


if name == "main":
    input = input("Input the numbers separated by a comma :\n").strip()
    unsorted = [int(item) for item in input.split(",")]
    print(sort(unsorted))
"""
nykam_nelson
"""
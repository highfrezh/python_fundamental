#Example 1
# matrix = [
#     [1, 2, 3],
#     [3, 4, 5],
#     [6, 7, 9]
# ]
# print(matrix[0][2])
# for row in matrix:
#     print(row)
#     for item in row:
#         print(item)

#Example 2
# List manipulation
# number = [1, 2, 2, 3, 4, 5, 6, 9, 1]
# number.append(20)
# number.insert(0, 20)
# number.remove(1)
# number.clear()
# number.pop()
# number.sort()
# number.reverse()
# number2 = number.copy()
# print(number.index(2))
# print(number.count(2))

# print(number2)
# remove duplicate number from the list
# for item in number:
#     if number.count(item) > 1 :
#         number.remove(item)
#         number.sort()
# print(number)

# tuple on like list it can't be modify it can only be count and ge the Index!
# numbers = (1, 2, 3, 4)
# print(numbers[1])
# print(numbers.index(2))
# print(numbers.count(1))

# unpacking
# coordinate = (1, 2, 5)
# coordinate = [1, 2, 5]
# x,y,z = coordinate
# print(x)
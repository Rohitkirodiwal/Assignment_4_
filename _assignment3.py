def square_num(num):
  return num * num
nums = [4, 5, 2, 9]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements by map:",list(result))
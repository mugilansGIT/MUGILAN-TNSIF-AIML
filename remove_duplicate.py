def dup(arr):
  unique=[]
  for i in arr:
    if i not in unique:
      unique.append(i)
  return unique
arr=[10, 20, 10, 30, 20, 40, 30]
print(dup(arr))
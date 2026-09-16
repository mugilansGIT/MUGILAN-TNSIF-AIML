def eq(a,b):
  if len(a)!=len(b):
    print("not equal")
    return
  visited=[]
  for i in range (len(a)):
    found=False
    for j in range (len(b)):
      if a[i]==b[j] and j not in visited:
        visited.append(j)
        found=True
        break
    if not found:
      print("not equal")
      return
  print("arrays are equal")
a = [1, 2, 2, 3, 4]
b = [4, 2, 1, 2, 3]

eq(a, b)

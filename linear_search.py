def fin(arr,target):
  for i in range(len(arr)):
    if arr[i]==target:
      print("target found")
      return
  print("not found")
        

arr=[1,2,3,4]
target=int(input("enter a element: "))
fin(arr,target)
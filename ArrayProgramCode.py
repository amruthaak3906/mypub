print("Press 'x' to exit");
size=input('Enter the size of the array:\n')
if size=='x':
    exit();
else:
    n=int(size);
    arr=[];
    print('Enter the array elements:\n');
    for i in range(0,n):
        val=input();
        arr.insert(i,val);
arr.sort();
print("\nArray elements are:\n")
for i in range(0,n):
    print(arr[i],"\n",end='')

item=input("\nEnter the number to be inserted into the array:\n")
def linearsearch(arr, item):
   for i in range(len(arr)):
      if arr[i] == item:
         return i
   return -1
a=linearsearch(arr,item)
if(a==-1):
   print("Element not found")
   arr.append(item);
   arr.sort();
   print("\nArray elements are:\n")
   for i in range(0, len(arr)):
       print(arr[i], "\n", end='')
   exit();
else:
   print("Cannot insert, element found at index",a)


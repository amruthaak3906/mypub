
def arr_index(arr, n, item):
    start = 0
    end = n - 1
    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == item:
            return mid

        elif arr[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1

arr=[]
n=int(input('Enter the number of elements:\n'))
print('Enter the array elements:\n')
for i in range(0,n):
    val=int(input())
    arr.insert(i,val)
arr.sort()
print('Sorted array is:\n')
for i in range(0,n):
    print(arr[i],'\n')
item=int(input('\nEnter the item to be inserted:\n'))
print('You can insert the item in ',arr_index(arr, n, item),'th position')

#Time Complexity= O(log n)
def arr_search(arr,item):
    for i in range (0,n):
        if arr[i]==item:
            print('\nItem already present in the ',i,'th position')
            exit()
        elif arr[i]>item and i<=n:
            print('\nItem can insert at ',i,'th position')
            exit()
    print('\nItem can insert at ', n, 'th position')

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
arr_search(arr,item)

#Time Complexity= O(n)
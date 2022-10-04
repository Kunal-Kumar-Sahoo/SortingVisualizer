l1 = []
n = int(input("Enter the no of elements to be added in the list: "))

for i in range(0,n):
    element = int(input("Add element: "))
    l1.append(element) 

print(l1)

for j in range(n):
    #initially swapped is false
    swapped = False
    i = 0
    while i<n-1:
        if l1[i]>l1[i+1]:
            l1[i],l1[i+1] = l1[i+1],l1[i]
            swapped = True
        i = i+1
    if swapped == False:
        break
    
print("After bubble sort: ")
print(l1)   
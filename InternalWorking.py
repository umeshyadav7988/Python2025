import copy
# list is a collections of items
myList = [1,2,3,4]
print(myList[0])

# for i in range(len(myList)):
    # print(myList[i])
    
myListOne = [1,2,3,4,5]
myListTwo = myListOne
myListOne = "chaiandcode"
myListOne = [1,2,3,4,5]
myListOne[0] = 33
print(myListTwo)
print(myListOne)



list1=[1,2,3,4]
list2=list1
print(list1)
list1[0]=33
print("List 1",list1)
print("List 2",list2)

# slicing
h1 = [1,2,3]
h2=h1[:] #copy
print(h1)
h1[0]=33
print(h1)
print(h2)


n = [1,2,3,4]
m= n
print(n)
print(m == n)
print(m is n)
m = [1,2,3,4]
print(m==n)
print(m is n)




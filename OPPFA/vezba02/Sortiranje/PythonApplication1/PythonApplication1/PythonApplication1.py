import random
import time
def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

list1 = random_list(1, 100, 50)
list2 = random_list(1, 100, 50)
list3 = random_list(1, 100, 50)

print ("List 1: ")
print (" ")
print (list1)
print (" ")

print ("List 2: ")
print (" ")
print (list2)
print (" ")

print ("List 3: ")
print (" ")
print (list3)
print (" ")

def search_linear(x,y):
    n = len( x )
    for i in range(n):
        if theValue[i] == y:
            return True

    return False

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    print("Merging ",alist)

#TO DO:
#----------------------------------------------------------------\
print (" ")
print ("Merge sort: ")
print (" ")
start_time1 = time.clock()

def foo1():

     mergeSort(list1)

foo1()

end_time1 = time.clock() - start_time1
print (" ")
print ("Merge sort: ")
print (" ")
print ("Duration: ", end_time1)
print (" ")
print(list1)
print (" ")
print ("Insertion sort: ")
print (" ")

start_time2 = time.clock()

def foo2():
     insertionSort(list2)

foo2()

end_time2 = time.clock() - start_time2
print ("Duration: ", end_time2)
print (" ")
print(list2)

start_time3 = time.clock()

def foo3():
     i = search_linear(list3, 15)
     if(i == True)
        
foo3()

end_time3 = time.clock() - start_time3
print (" ")
print ("Duration: ", end_time3)
print (" ")




#----------------------------------------------------------------




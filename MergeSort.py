#Program to merge sort an array

import numpy

def merge_sort(lst):
    '''
    function to merge sort a list
    '''
    #find the length of list
    l = len(lst)
    
    #if length of list is 1, return the list
    if (l<=1):
        return (lst)
    
    #find the middle value and split the list
    midl = l/2   

    #create left and right lists
    leftlst = lst[:midl]
    rightlst = lst[midl:]

    #recursively sort both the lists
    leftlst = merge_sort(leftlst)
    rightlst = merge_sort(rightlst)

    return (merge(leftlst, rightlst))


def merge(left, right):
    '''
    function to merge two lists in ascending order
    '''
    result = []

    while ((len(left) != 0) & (len(right) != 0)):
        if (left[0] < right[0]):
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
            
    while (len(left) != 0):
        result.append(left[0])
        left = left[1:]
    
    while (len(right) != 0):
        result.append(right[0])
        right = right[1:]
                
    return (result)


# Sample program to test the code
c = [1, 4, 245, 33, 1, 10, 11, 3]

merge_sort(c)

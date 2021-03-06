def iterativeBinarySearch(array, target):
    """
    This algorithm represents the binary search algorithm implemented iteratively. This algorithm 
    finds the position of a target value within within a sorted array by dividing a range of values 
    into halves, and continuing to narrow down the search space until the desired value is found. 
    As such, it is an example of a divide and conquer algorithm. 

    This algorithm assumes the simplest case of binary search searching over an explicit sorted array, 
    but the search space can be any space that is sorted. For example, binary search can be used on 
    functions which are monotonically increasing  or decreasing in order to find the lowest possible 
    value some condition is met (low bound binary search), or the highest possible value some condition 
    is met (high bound binary search). This means binary searching over the inputs of these functions to
    determine which input produces the most optimal value -- highest or lowest output value that meets
    some condition. 

    Key tip: If the search space consists of integers, then test the binary search on a two element set 
    in order to ensure convergence. 

    Inputs:
        - array(list[int]): List of integers sorted in ascending order
        - target(int): Integer we're looking for in the array 
    Output:
        - Integer representing the idx at which the target value occurs, or -1 if it does not occur
    """
    left = 0
    right = len(array)-1

    while left < right:
        mid = left + (right-left)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid
        else:
            left = mid+1 
        
    return left if array[left] == target else -1 



def recursiveBinarySearch(array, target):
    """
    This algorithm represents the binary search algorithm implemented recursively. This algorithm finds 
    the position of a target value within within a sorted array by dividing a range of values into halves, 
    and continuing to narrow down the search space until the desired value is found. As such, it is an 
    example of a divide and conquer algorithm. 

    This algorithm assumes the simplest case of binary search searching over an explicit sorted array, but the 
    search space can be any space that is sorted. For example, binary search can be used on functions which are
    monotonically increasing or decreasing in order to find the lowest possible value some condition is met (low
    bound binary search), or the highest possible value some condition is met (high bound binary search). This means 
    binary searching over the inputs of these functions to determine which input produces the most optimal value -- 
    highest or lowest output value that meets some condition. 

    Key tip: If the search space consists of integers, then test the binary search on a two element set in order 
    to ensure convergence. 

    Inputs:
        - array(list[int]): List of integers sorted in ascending order
        - target(int): Integer we're looking for in the array 
    Output:
        - Integer representing the idx at which the target value occurs, or -1 if it does not occur
    """
    return recursiveHelperBinarySearch(array, target, 0, len(array)-1)


def recursiveHelperBinarySearch(array, target, left, right):
    if left == right:
        return left if array[left] == target else -1 
    
    mid = left + (right-left)//2

    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return recursiveHelperBinarySearch(array, target, left, mid)
    
    else:
        return recursiveHelperBinarySearch(array, target, mid+1, right)
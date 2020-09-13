"""
Given an ascending sorted rotated array Arr of distinct integers of size N. The array is right rotated K times. Find the value of K.
Input:
N = 5
Arr[] = {5, 1, 2, 3, 4}
Output: 1
Explanation: The given array is 5 1 2 3 4.
The original sorted array is 1 2 3 4 5.
We can see that the array was rotated
1 times to the right.
"""
#################################################################################################
"""Algorithm
The minimum element is the only element whose previous is greater than it. 
If there is no previous element, then there is no rotation (first element is minimum).
We check this condition for middle element by comparing it with (mid-1)’th and (mid+1)’th elements.

If the minimum element is not at the middle (neither mid nor mid + 1),
then minimum element lies in either left half or right half.
    1. If middle element is smaller than last element, then the minimum element lies in left half
    2. Else minimum element lies in right half.
"""


# code
def count_rotation(arr, low, high):
    if high < low:
        return 0
    if high == low:
        return low
    mid = int(low + (high - low) / 2)
    if mid < high and arr[mid + 1] < arr[mid]:
        return mid + 1
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid
    if arr[high] > arr[mid]:
        return count_rotation(arr, low, mid - 1)
    return count_rotation(arr, mid + 1, high)


size = int(input())
arr = list(map(int, input().strip().split()))[:size]
print(count_rotation(arr, 0, size-1))

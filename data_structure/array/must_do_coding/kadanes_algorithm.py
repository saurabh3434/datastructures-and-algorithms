"""
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

Constraints:
1 ≤ T ≤ 110
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Example:
Input
2
5
1 2 3 -2 5
4
-1 -2 -3 -4
Output
9
-1

Explanation:
Testcase 1: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.
"""
#code
from sys import maxsize


def max_sub_array_sum(arr, size):
    max_sum = -maxsize - 1
    max_end_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(0, size):

        max_end_here += arr[i]

        if max_sum < max_end_here:
            max_sum = max_end_here
            start = s
            end = i

        if max_end_here < 0:
            max_end_here = 0
            s = i + 1
    print(start, end)
    return max_sum


tc = int(input())
for i in range(tc):
    N = int(input())
    A = list(map(int, input().split()))
    print(max_sub_array_sum(A, len(A)))

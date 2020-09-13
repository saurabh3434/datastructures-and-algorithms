"""

Given an unsorted array arr[] of size N, rotate it by D elements (clockwise).

Input:
The first line of the input contains T denoting the number of testcases. First line of each test case contains two space separated elements, N denoting the size of the array and an integer D denoting the number size of the rotation. Subsequent line will be the N space separated array elements.

Output:
For each testcase, in a new line, output the rotated array.

Constraints:
1 <= T <= 200
1 <= N <= 107
1 <= D <= N
0 <= arr[i] <= 105

Example:
Input:
2
5 2
1 2 3 4 5
10 3
2 4 6 8 10 12 14 16 18 20

Output:
3 4 5 1 2
8 10 12 14 16 18 20 2 4 6

Explanation :
Testcase 1: 1 2 3 4 5  when rotated by 2 elements, it becomes 3 4 5 1 2.

"""
#################################################################################################
"""Algorithm:
# 1) Store the first d elements in a temp array
#    temp[] = [1, 2]
# 2) Shift rest of the arr[]
#    arr[] = [3, 4, 5, 6, 7, 6, 7]
# 3) Store back the d elements
#    arr[] = [3, 4, 5, 6, 7, 1, 2]"""
##################################################################################################

# code
tc = int(input())
for i in range(tc):
    size, d = map(int, input().split())
    arr = list(map(int, input().strip().split()))[:size]
    tem = arr[:d]
    for i in range(size - d):
        arr[i] = arr[i + d]
    arr[size - d:] = tem
    print(*arr)

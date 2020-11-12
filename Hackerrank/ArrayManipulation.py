"""
coding: utf-8
Created on 11/11/2020

@author: github.com/edrmonteiro

From: Hackerrank challenges
Language: Python
Title: Array Manipulation

Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Example


Queries are interpreted as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of  between the indices  and  inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is  after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below.

arrayManipulation has the following parameters:

int n - the number of elements in the array
int queries[q][3] - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Returns

int - the maximum value in the resultant array
Input Format

The first line contains two space-separated integers  and , the size of the array and the number of operations.
Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.

Constraints

Sample Input

5 3
1 2 100
2 5 100
3 4 100
Sample Output

200
Explanation

After the first update the list is 100 100 0 0 0.
After the second update list is 100 200 100 100 100.
After the third update list is 100 200 200 200 100.

The maximum value is .

"""
#from array import *


def arrayManipulation(n, queries):
    arr = [0] * n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
    maxVal = 0
    currentVal = 0
    for q in arr:
        currentVal += q
        maxVal = max(maxVal, currentVal)
    return maxVal


n = 100
queries = [[1,1,10000000000]]
print(arrayManipulation(n, queries))

n = 1000000000
queries = [[1,1,3]]
print(arrayManipulation(n, queries))

n = 3
queries = [[3,3,3]]
print(arrayManipulation(n, queries))

queries = [[1,1,3]]
print(arrayManipulation(n, queries))

n = 10
queries = [[1,5,3], [4,8,7], [6,9,1]]
print(arrayManipulation(n, queries))


n = 5
queries = [[1,2,100], [2,5,100], [3,4,100]]
print(arrayManipulation(n, queries))


stop = True



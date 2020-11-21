"""
coding: utf-8
Created on 31/10/2020

@author: github.com/edrmonteiro

From: Codility Lessons
"""
# CountFactors

# A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

# For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the number of its factors.

# For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].


def solution(N):
    if N == 1:
        return 1
    factors = 0
    i = 1
    while i ** 2 < N:
        if N % i == 0:
            factors += 2
        i += 1
    if i ** 2 == N:
        factors += 1

    return factors

N = 24
print(solution(N))

stop = True


# 57% performance problem
# def solution(N):
#     factors = 0
#     for i in range(1, N + 1):
#         if N % i == 0:
#             factors += 1
#     return factors
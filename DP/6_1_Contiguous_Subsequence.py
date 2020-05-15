# 6.1. A contiguous subsequence of a list S is a subsequence made up of consecutive elements of S.
# For instance, if S is,
# [5, 15, -30, 10, -5, 40, 10]
# then 15, -30, 10 is a contiguous subsequence but 5, 15, 40 is not.
# Give a linear-time algorithm for the following task:
# Input: A list of numbers, a1, a2, ..., an
# Output: The contiguous subsequence of maximum sum (a subsequence of length zero has sum zero).
# For the preceding example, the answer would be 10, -5, 40, 10, with a sum of 55.
# (Hint: For each j in { 1, 2, ..., n }, consider contiguous subsequences ending exactly at position j.)


def solution(given_numbers):
    d = [0] * len(given_numbers)
    d[0] = 0
    for i in range(1, len(given_numbers)):
        num = given_numbers[i]
        d[i] = num + max(d[i-1], 0)

    answer = 0
    for i in range(len(d)):
        if answer < d[i]:
            answer = d[i]
    return answer


given_list = [5, 15, -30, 10, -5, 40, 10]
print(solution(given_list))

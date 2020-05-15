# LIS (Longest Increase Subsequence)


def lis(given_list):
    l = [1] * len(given_list)
    for i in range(len(given_list)):
        l[i] = 1
        for j in range(0, i):
            if given_list[i] > given_list[j] and l[i] < l[j] + 1:
                l[i] = l[j] + 1

    answer = 1
    for i in range(len(l)):
        if l[i] > answer:
            answer = l[i]

    return answer


list_of_numbers = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
print(lis(list_of_numbers))

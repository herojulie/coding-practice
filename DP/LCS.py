# LCS (Longest Common Subsequence)


def get_max(a, b) -> int:
    return a if a > b else b


def print_my_list(my_list):
    for i in range(len(my_list)):
        print(my_list[i])


def lcs(str1, str2) -> int:
    len1 = len(str1)
    len2 = len(str2)

    # l = [[0] * (len1 + 1)] * (len2+1)

    l = [0] * (len1 + 1)
    for i in range(len(l)):
        l[i] = [0] * (len2 + 1)

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i-1] == str2[j-1]:
                l[i][j] = 1 + l[i-1][j-1]
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])

    print_my_list(l)
    return l[len1][len2]


s1 = 'BCDBCDA'
s2 = 'ABECBA'
print(lcs(s1, s2))

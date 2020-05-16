# 6.2. You are going on a long trip. You start on the road at mile post 0.
# Along the way there are n hotels,
# at mile posts a1 < a2 < ... < an, where each ai is measured from the starting point.
# The only places you are allowed to stop are at these hotels,
# but you can choose which of the hotels you stop at.
# You must stop at the final hotel (at distance an), which is your destination.
# You'd ideally like to travel 200 miles a day, but this may not be possible (depending
# on the spacing of the hotels). If you travel x miles during a day,
# the penalty for that day is (200-x)^2. You want to plan your trip so as to minimize
# the total penalty--that is, the sum, over all travel days, of the daily penalties.
# Give an efficient algorithm that determines the optimal sequence of hotels at which to stop.


import math


def get_penalty(distance) -> int:
    return int(math.pow((200 - distance), 2))


def solution(hotels) -> int:
    length = len(hotels)
    H = [0] * length
    H[0] = 0

    for i in range(1, length):
        min_penalty = 99999
        for j in range(i):
            penalty = H[j] + get_penalty(hotels[i] - hotels[j])
            if penalty < min_penalty:
                min_penalty = penalty
        H[i] = min_penalty
    print(H)
    return H[length-1]


Hotels = [0, 100, 300, 450, 500, 600, 770]

print(solution(Hotels))

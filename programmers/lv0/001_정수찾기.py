def solution(num_list, n):
    for x in num_list:
        if n == x:
            return 1
    return 0


print(solution([1,2,3], 2))

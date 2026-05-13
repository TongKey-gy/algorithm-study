# 정수가 담긴 리스트 num_list가 주어질 때, 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    
    result = 1 #곱셈은 1부터 시작하므로.

    #if구문이 참이면 바로 return되므로 else를 쓰지 않아도 됨.
    for num in num_list: 
        result *= num

    return result

#if-else로 쓴 경우

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    
    else :
        result = 1

        for num in num_list:
            result *= num

        return result
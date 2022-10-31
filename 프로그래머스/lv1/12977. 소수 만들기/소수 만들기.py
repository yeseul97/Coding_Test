from itertools import combinations

def solution(nums):
    answer = []
    per = []

    per = list(combinations(nums,3)) # 3개씩 조합

    for arr in per: 
        n = sum(arr)
        if n<2: # 2보다 작은 1,0의 경우 소수 아님
            continue
        check = True
        for i in range(2, int(n**0.5)+1):  # n의 제곱근보다 작은 숫자까지만 나눗셈
            if n%i == 0:
                check = False
                break
        if check:
            answer.append(n)  # 소수일경우 answer 배열에 추가
            
    return len(answer)
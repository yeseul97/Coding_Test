from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)]) # 시간초과 문제해결 위해 deque 활용

while (len(deque) > 1):
    deque.popleft() # 첫번째꺼 삭제
    move_num = deque.popleft() # 다음꺼 삭제 및 저장
    deque.append(move_num) # 위에서 받은 거 마지막 자리에 붙이기 
    
print(deque[0])
from sys import stdin

N = int(stdin.readline()) # stdin은 시간초과 안되려고 사용

queue = []

for i in range(N):
    cmd = stdin.readline().split()

    if cmd[0] == "push":
        queue.insert(0, cmd[1]) # 첫번째 자리에 cmd[1]을 넣음

    elif cmd[0] == "pop":
        if len(queue) != 0: print(queue.pop()) # queue에 값이 있을 때
        else: print(-1)

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        if len(queue) == 0: print(1)
        else : print(0)

    elif cmd[0] == "front": # 큐의 가장 앞에 있는 정수 출력
        if len(queue) == 0: print(-1)
        else: print(queue[len(queue) -1]) # 제일 최근에 넣은거

    elif cmd[0] == "back": # 큐의 가장 뒤에 있는 정수 출력
        if len(queue) == 0: print(-1)
        else: print(queue[0]) # 제일 처음에 넣은거
answer=[0,0]

def solution(s):
    answer[0]+=1
    answer[1]+=s.count('0')
    s = s.replace('0','')
    s = format(len(s),'b')
    if s != '1':
        return solution(s)
    else:
        return answer

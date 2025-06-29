# https://github.com/dremdeveloper/codingtest_python/blob/main/solution/03.py
def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            answer.append(arr[i] + arr[j])
    print(sorted(set(answer)))
    

#solution([2, 1, 3, 4, 1])
solution([5, 0, 2, 7])
# https://github.com/dremdeveloper/codingtest_python/blob/main/solution/02.py
def solution(arr):
    return sorted(set(arr), reverse=True)

print(solution([2, 1, 1, 3, 2, 5, 4]))
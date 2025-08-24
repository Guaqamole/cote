# https://github.com/dremdeveloper/codingtest_python/blob/main/solution/04.py

def solution(arr):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = [0] * 3

    for i, answer in enumerate(arr):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(arr)]:
                scores[j] += 1
    
    max_score = max(scores)

    highest_scores = []

    for idx, score in enumerate(scores):
        if score == max_score:
            highest_scores.append(idx + 1)
    return highest_scores


#print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))

# 15: 3, 5, 6, 9, 10, 12

def solution(N):  # O(N)

    multiples = []

    for num in range(1, N):
        if num % 3 == 0:
            multiples.append(num)
        elif num % 5 == 0:
            multiples.append(num)

    # print(multiples)
    return sum(multiples)


if __name__ == '__main__':
    total = solution(1000)
    print("Total sum:", total)
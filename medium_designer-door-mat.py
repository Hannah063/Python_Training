N, M = map(int, input().split())

title = "WELCOME"
num = 1
flag = False

for i in range(N):
    if i == N // 2:
        left = (M - len(title)) // 2
        right = M - len(title) - left
        print("-" * left + title + "-" * right)
        flag = True
        num -= 2
    else:
        pattern = ".|." * num
        left = (M - len(pattern)) // 2
        right = M - len(pattern) - left
        print("-" * left + pattern + "-" * right)
        if flag:
            num -= 2
        else:
            num += 2
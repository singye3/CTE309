n, m, a, b = map(int, input().split())
article = [input() for _ in range(n)]

enlarged_article = []
for row in article:
    enlarged_row = ''.join([char * b for char in row])
    for _ in range(a):
        enlarged_article.append(enlarged_row)

for row in enlarged_article:
    print(row)

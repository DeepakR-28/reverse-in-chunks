# n = int(input())
# alist = list(map(str,input().split()))
# r = int(input())
# chunk = alist[:r]
# chunk.sort(reverse = True)
# for i in range(r):
#   alist.remove(alist[i])
# print(*(chunk + alist))

n = int(input())
alist = list(map(int,input().split()))
print(*list(set(alist)))

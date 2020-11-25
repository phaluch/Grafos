_ = input()
l = [int(n) for n in input().split(' ')]
ans = []

for i in range(len(l)):
    s = set()
    cur = i+1
    s.add(cur)
    #print('Comecando de ',cur)
    while True:
        #print(f'O {cur} falou que o {l[cur-1]} é o culpado.')
        s.add(cur)
        cur=l[cur-1]
        if cur in s:
            #print(f'Cheguei no {cur} de novo.')
            ans.append(cur)
            break
            

print(' '.join([str(n) for n in ans]))
n, k = map(int, input().split())
d = {}
for i in range(n):
    name, n1 = map(str, input().split())
    for i in range(int(n1)):
        skill, level = map(str, input().split())
        if skill in d:
            d[skill].append([int(level), name])
        else:
            d[skill] = [[int(level), name]]
for i in d:
    d[i].sort()
e = []
for i in range(k):
    name, di, si, bi, ri = map(str, input().split())
    e += [[int(bi), int(si), int(di), [], name]]
    for i in range(int(ri)):
        skill, lvl = map(str, input().split())
        e[len(e)-1][3].append([skill, int(lvl)])
e.sort()
print(d)
print(e)
final = []
for i in e:
    flag = True
    la = []
    da = []
    for j in i[3]:
        if j[0] in d:
            if d[j[0]][-1][0] >= j[1]:
                if d[j[0]][-1][1] in da:
                    flag = False
                    break
                else:
                    la.append(d[j[0]][-1][1])
                    da.append(d[j[0]][-1][1])
            else:
                flag = False
        else:
            flag = False
    if flag:
        final.append([i[4], la])
print(len(final))
for i in final:
    print(i[0])
    print(' '.join(i[1]))

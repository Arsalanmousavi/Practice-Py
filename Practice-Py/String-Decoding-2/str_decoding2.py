strings = 'a4 c2 e1 g3 i5 g8'

parts = strings.split(" ")
print(parts, type(parts))

answer = []
for i in range(100):
    answer.append("")

for p in parts:
    pstr = p[0]
    pindx = int(p[1:])
    print(pstr, pindx)
    answer[pindx] = pstr

answer = ''.join(answer)
print(answer)

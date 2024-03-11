l = []
temp = head
while temp != None:
    l.append(temp.val)
    temp = temp.next
head = None
c = 0
for i in range(len(l) // 2):
    c = max(c, l[i] + l[len(l) - i - 1])
return c

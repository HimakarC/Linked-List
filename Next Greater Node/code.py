l = []
L = []
temp = head
i = 0
while temp != None:
    while l and l[-1][0] < temp.val:
        L[l[-1][1]] = temp.val
        l.pop()
    l.append([temp.val, i])
    L.append(0)
    i += 1
    temp = temp.next
return L

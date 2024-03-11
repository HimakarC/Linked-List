l = []
temp = head
while temp != None:
  while l and l[-1].val < temp.val:
      l.pop()
  if l: l[-1].next = temp
  l.append(temp)
  temp = temp.next
return l[0]

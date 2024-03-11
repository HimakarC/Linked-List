temp1, temp2 = head.next, head.next.next
while temp2.next != None:
    if temp2.val == 0:
        temp1.next = temp2.next
        temp1 = temp1.next
        temp2 = temp2.next.next
    else:
        temp1.val += temp2.val
        temp2 = temp2.next
else: temp1.next = None
return head.next

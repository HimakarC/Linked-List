temp = low = ListNode(-1)
high = temp1 = ListNode(-1)
while head:
    if head.val < x:
        low.next = head
        low = low.next
    else:
        temp1.next = head
        temp1 = temp1.next
    head = head.next
temp1.next = None
low.next = high.next
return temp.next

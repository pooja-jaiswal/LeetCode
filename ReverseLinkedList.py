def reverseList(head):
    if head == None or head.next == None:
        return head
    temp1 = head.next
    temp2 = head.next.next
    head.next = None
    while temp1.next != None:
        temp2 = temp1.next
        temp1.next = head
        head = temp1
        temp1 = temp2
    temp1.next = head
    head = temp1
    return head
def middleNode(head):
    temp1 = head
    count = 1
    while temp1.next != None:
        temp1 = temp1.next
        count += 1
    count = int(count/2)
    temp1 = head
    for i in range(0,count):
        temp1 = temp1.next
    head = temp1
    return head
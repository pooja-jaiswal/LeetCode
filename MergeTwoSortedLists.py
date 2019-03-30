class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

start = ListNode(0)
temp = start
for i in range(1,50):
    temp.next = ListNode(i)
    temp = temp.next

def mergeTwoLists(l1, l2):
    list1 = ListNode
    list2 = ListNode
    while l1 != None and l2 != None:
        if l1.val < l2.val:
            temp = l1
            l1 = l1.next
        else:
            temp = l2
            l2 = l2.next
        list2.next = temp          
        list2 = list2.next
    list2.next = l1 or l2
    return list1.next


        

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

start = ListNode(0)
temp = start
for i in range(1,50):
    temp.next = ListNode(i)
    temp = temp.next

temp1 = start.next
temp2 = start.next.next
start.next = None
while temp1.next != None:
    temp2 = temp1.next
    temp1.next = start
    start = temp1
    temp1 = temp2
temp1.next = start
start = temp1

temp3 = start
while temp3 != None:
    print(temp3.val)
    temp3 = temp3.next

# count = 1
# temp1 = start
# # for i in range(0,96):
# #     temp1 = temp1.next

# # Middle element
# while temp1.next != None:
#     temp1 = temp1.next
#     count += 1
# count = count/2
# temp1 = start
# for i in range(0,count):
#     temp1 = temp1.next

# temp1 = start
# temp1 = start.next.next.next
# temp2 = start
# # temp2 = temp2
# while temp1 != None:
#     temp1 = temp1.next
#     temp2 = temp2.next
# print(temp2.val)

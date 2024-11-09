# Singly Linked Lists

class SinglyNode:

    def __init__(self, val, next=None):
        self.val=val
        self.next=next

Head=SinglyNode(1)
A=SinglyNode(7)
B=SinglyNode(4)
C=SinglyNode(23)

Head.next=A
A.next=B
B.next=C

print(Head.val)

#Traverse the list - O(n)
curr=Head

while curr:
    print(curr.val)
    curr=curr.next


#Display the list - O(n)
def display_list(head):
    curr = head
    element=[]
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(element))

display_list(Head)



# Search for node value - O(n)
def search(head,val):
    curr = head
    while curr:
        if curr.val == val:
            return bool(1)
        curr = curr.next

    return bool(0)

print(search(Head,23))




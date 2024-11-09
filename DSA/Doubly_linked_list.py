# Doubly linked list

class DoublyNode:

    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev =prev

    def __str__(self):
        return str(self.val)

Head = Tail= DoublyNode(1)


#Display the list - O(n)
def display_list(head):
    curr = head
    element=[]
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(element))

display_list(Head)


#Inserting a new node at the beginning - O(1)
def insert_at_beginning(Head, Tail,val):
    new_node = DoublyNode(val, Head, None)
    Head.prev=new_node
    return new_node, Tail

Head, Tail= insert_at_beginning(Head,Tail,3)
display_list(Head)

#Inserting a new node at the end - O(1)
def insert_at_end(Head, Tail,val):
    new_node = DoublyNode(val, prev=Tail)
    Tail.next=new_node
    return Head,new_node

Head, Tail= insert_at_end(Head,Tail,7)
display_list(Head)
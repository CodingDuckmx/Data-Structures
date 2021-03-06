"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head:
            self.head.prev = ListNode(value,None,self.head)
            self.head = self.head.prev   
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head:
            value = self.head.value
            self.delete(self.head)
            return value
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail:
            self.tail.next = ListNode(value,self.tail,None)
            self.tail = self.tail.next
        else:
            self.tail = ListNode(value)
            self.head = self.tail
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail:
            value = self.tail.value
            self.delete(self.tail)
            return value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        node_val = node.value
        self.delete(node)
        self.add_to_head(node_val)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        node_val = node.value
        self.delete(node)
        self.add_to_tail(node_val)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return
        self.length -=1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
        elif self.tail == node:
            self.tail = node.prev
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        maxval = self.head.value
        curr = self.head
        while curr.next:
            if curr.next.value > maxval:
                maxval = curr.next.value
            curr = curr.next
        return maxval


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.add_to_head(ListNode(5))
    dll.add_to_head(ListNode(4))
    print(dll.head.next)
    print(dll.tail.prev)
    print(dll.head.next is dll.tail.prev)
    # dll.delete(ListNode(5))
# Reverse a singly linked list

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example usage
# Creating a linked list 1->2->3->4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reversed_head = reverse_linked_list(head)

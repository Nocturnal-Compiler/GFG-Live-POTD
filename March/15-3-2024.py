# 15th March 2024 POTD: Linked List that is Sorted Alternatingly
# User function Template for python3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Solution:
    def sort(self, head):
        if not head or not head.next:
            return head
        
        # Helper function to get the length of the linked list
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        # Helper function to convert the linked list to an array
        def linked_list_to_array(head):
            array = []
            while head:
                array.append(head.data)
                head = head.next
            return array
        
        # Helper function to convert the array to a sorted linked list
        def array_to_linked_list(array):
            dummy = Node(0)
            curr = dummy
            for val in array:
                curr.next = Node(val)
                curr = curr.next
            return dummy.next
        
        # Main function logic starts here
        length = get_length(head)
        array = linked_list_to_array(head)
        array.sort()
        sorted_head = array_to_linked_list(array)
        
        return sorted_head
# 16th March 2024 POTD: Delete without head pointer

class Solution:
    def deleteNode(self, del_node):
        # Check if the del_node is not the last node of the linked list
        if del_node.next is not None:
            del_node.data = del_node.next.data
            next_node = del_node.next
            # Update the link of the given node to skip the next node
            del_node.next = del_node.next.next
            # Delete the next node
            del next_node
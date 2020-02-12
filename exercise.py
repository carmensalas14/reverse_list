class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def reverse(node: Node) -> Node:
    current = node
    next_node = None
    prev = None
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev 
    

        
    
    
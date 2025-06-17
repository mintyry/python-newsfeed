# building block for a linked list

# constructor
class Node(object):
    # takes two args: d (data) and n (next node)
    # n defaults as none (no next node)
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n

    # next, we need getters and setters functions for data and next node
    def get_next (self):
        return self.next_node
    def set_next (self, n):
        self.next_node = n
    def get_data (self):
        return self.data
    def set_data (self, d):
        self.data = d
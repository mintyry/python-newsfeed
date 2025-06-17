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
 # write linkedlist class
 # every linkedlist needs to have two instance variables: root and size
class LinkedList (object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_size (self):
        return self.size
    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1
    def remove (self, d):
        # track node we're looking at, starting at root
        this_node = self.root
        # track previous node because we're going to have to change pointer of previous node
        prev_node = None
        # iterate through list and if we find node we lookin for, and if we're not in root node, then set prev node's next node pointer to this node's next node pointer
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    # if we are in the root, then there' no prev node
                    self.root = this_node.get_next()
                self.size -= 1
                    # indicates we successfully removed the data
                return True
           #if we didnt find data in current node, then advance pointer from prev node to next node and this node to next node
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        # exit while loop and we didnt successfully remove the data:
        return False
    def find (self, d):
        # start at root
        this_node = self.root
        # while theres another node, look at each node to compare data against data we're looking for
        while this_node:
            if this_node.get_data() == d:
            # finds it, return data
                return d
            else:
            # doesnt find it, move on
                this_node = this_node.get_next()
        # if exits loop without finding data, return non
        return None

# practice: instansiate a new list and use methods
myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.remove(8)
# print(myList.remove(12)) should print true
# print(myList.find(5)) should print the data (5)

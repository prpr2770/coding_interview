# Chapter 2: Linked List

"""
LinkedList Data-structure

Node:
    +data
    +next_node
    @__init__
    @__str__
    @get_node_data
    @get_next_node
    @set_next_node

LinkedList:
    +head
    +size
    @__init__
    @__str__
    @append_data(data,loc='head'/'tail')
    @delete_data(data)

"""

class Node(object):

    def __init__(self, data= None, next_node = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return 'Node('+str(self.data)+')'

    def get_node_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self,new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def __str__(self):
        curr_node = self.head
        count_nodes_traversed = 1
        res_str = 'LinkedList['
        while count_nodes_traversed <= self.size:
            res_str = res_str + str(curr_node) + ' -> '
            curr_node = curr_node.get_next_node()
            count_nodes_traversed = count_nodes_traversed + 1
        res_str = res_str + str(curr_node) + ']'
        return res_str

    def append_data(self,data,loc='head'):
        new_node = Node(data)
        # --------------------------------------------
        if loc == 'head':
            # New data nodes are entered at the head of the linkedList
            new_node.set_next_node(self.head)
            self.head = new_node
        else:
            # New node is inserted at tail of linkedList
            cur_node = self.head # start at head
            while cur_node.get_next_node() != None:
                cur_node = cur_node.get_next_node()
            #cur_node now points at the last element
            cur_node.set_next_node(new_node)
        # --------------------------------------------
        # update size of the linkedList
        self.size = self.size + 1

    def delete_data(self,data):

        # traverse from the head-onwards and delete first-entry that equals data.
        par_node = self.head
        cur_node = par_node.get_next_node()

        while cur_node != None:

            if cur_node.get_node_data() == data:
                # delete cur_node
                par_node.set_next_node(cur_node.get_next_node())
            else:
                par_node = cur_node
                cur_node = par_node.get_next_node()

        if cur_node == None:
            # only one-node in linkedList
            if data == par_node.get_node_data():
                self.head = None
            else:
                print("End_Of_linkedList_Reached. data not found.")


if __name__ == "__main__":
    a_node = Node()
    print(a_node)

    a_list = LinkedList(a_node)
    #a_list.append_data(3)
    #a_list.append_data(2)
    #a_list.append_data(1)
    print(a_list)

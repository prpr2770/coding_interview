# 2.x1 Reverse Direction LinkedList:

from singleLinkedList import *

class rev_LinkedList(LinkedList):
    def reverse_linkedList(self): #a_list
        ptr_prev = None
        ptr_curr = self.head
        ptr_next = ptr_curr.get_next_node()

        while ptr_next != None:
            ptr_curr.set_next_node(ptr_prev)
            ptr_prev = ptr_curr
            ptr_curr = ptr_next
            ptr_next = ptr_next.get_next_node()

        ptr_curr.set_next_node(ptr_prev)
        self.head = ptr_curr



if __name__=="__main__":
    a_node = Node(1)
    a_list = rev_LinkedList(a_node)
    a_list.append_data(2)
    a_list.append_data(3)
    a_list.append_data(4)
    a_list.append_data(5)
    print(a_list)
    c_list = a_list
    print(c_list)

    a_list.reverse_linkedList()
    print(a_list)

# 2.1 Remove Dump: Write code to remove duplicates form an unsorted linked list

from singleLinkedList import *

class no_dups_LinkedList(LinkedList):
    def removeDuplicates_from_linkedList(self): #a_list
        ref_node = self.head

        while ref_node != None:
            ref_node_data = ref_node.get_node_data()
            par_node = ref_node
            inc_node = par_node.get_next_node()

            while inc_node != None:
                if inc_node.get_node_data() == ref_node_data:
                    # remove this node
                    inc_node = inc_node.get_next_node()
                    par_node.set_next_node(inc_node)
                else:
                    par_node = inc_node
                    inc_node = par_node.get_next_node()

            ref_node = ref_node.get_next_node()

if __name__=="__main__":
    a_node = Node(4)
    a_list = no_dups_LinkedList(a_node)
    a_list.append_data(6)
    a_list.append_data(6)
    a_list.append_data(4)
    a_list.append_data(4)
    a_list.append_data(4)
    a_list.append_data(1)
    a_list.append_data(2)
    a_list.append_data(1)
    print(a_list)
    c_list = a_list
    print(c_list)

    a_list.removeDuplicates_from_linkedList()
    print(a_list)

# 2.x2 Determining Loops in LinkedList:

from singleLinkedList import *

class loop_LinkedList(LinkedList):

    def append_node(self,data_node,loc='tail'):

        if loc == 'head':
            # New data nodes are entered at the head of the linkedList
            data_node.set_next_node(self.head)
            self.head = data_node
        else:
            # New node is inserted at tail of linkedList
            cur_node = self.head # start at head
            while cur_node.get_next_node() != None:
                cur_node = cur_node.get_next_node()
            #cur_node now points at the last element
            cur_node.set_next_node(data_node)
        # --------------------------------------------
        # update size of the linkedList
        self.size = self.size + 1


    def detect_loop_linkedList(self): #a_list
        slow_ptr = self.head
        fast_ptr = self.head
        slow_step_count = 0
        while slow_ptr != None and fast_ptr != None:
            try:
                slow_ptr = slow_ptr.get_next_node()
                slow_step_count = slow_step_count + 1
                fast_ptr = fast_ptr.get_next_node().get_next_node()
            except:
                # exception could have been only due to attempt at None_node.
                self.loop_exists = False
            if slow_ptr == fast_ptr:
                self.loop_exists = True
                self.index_of_first_meetup = slow_step_count
                break

        # determine length of loop
        if self.loop_exists:
            slow_ptr = slow_ptr.get_next_node()
            loop_length_count = 1
            while fast_ptr != slow_ptr:
                slow_ptr = slow_ptr.get_next_node()
                loop_length_count = loop_length_count + 1
            # when fast_ptr == slow_ptr
            self.loop_length = loop_length_count





    def detect_index_loop_enter(self):
        self.detect_loop_linkedList()
        if loop_exists:
            # determine the beginning of loop.
            # slow goes k, fast goes 2k.fast ahead by (LOOP_LEN - k%LOOP_LEN) time-steps it will catch up with slow.
            # steps ahead by slow, into loop: n = LOOP_LEN - k%LOOP_LEN
            # k = (LOOP_LEN - n)*LOOP_LEN : Index from where the loop begins.
            # n = slow_step_count

            # determine loop_length
            loc_loop_begin = (self.loop_length - self.index_of_first_meetup)*self.loop_length

if __name__=="__main__":
    a_node = Node(1)
    a_list = loop_LinkedList(a_node)
    a_list.append_data(2,loc='tail')
    a_list.append_data(3,loc='tail')
    c_node = Node(5)
    a_list.append_node(c_node,loc='tail')
    a_list.append_data(6,loc='tail')
    a_list.append_data(7,loc='tail')
    a_list.append_node(c_node,loc='tail')
    print(a_list)

    print("Loop Exists \t:" + str(a_list.detect_loop_linkedList()))

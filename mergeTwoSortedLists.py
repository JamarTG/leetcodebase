class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def traverseNode(lst):
    while lst:
        print(lst.val)
        lst = lst.next
    
        


def mergeTwoLists(list1, list2):
    
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    start_val = -10

    head = ListNode(start_val,None)
    currNode = head
    


    # # instead of adding lets print and see

    while not (list1 == None and list2 == None):
        if not list1 and list2:
            # create the new node and add the correct value
            print("list2:",list2.val)
            newNode = ListNode(list2.val , None)
            list2 = list2.next
            
            
            # attach the new node the list
            currNode.next = newNode

            # update the current node
            currNode = currNode.next
            # traverseNode(currNode)

            
        
        elif list1 and not list2:
            print("list1: ",list1.val)
            # create the new node and add the correct value
            newNode = ListNode(list1.val , None)
            list1 = list1.next
            # attach the new node the list
            currNode.next = newNode
        
            # update the current node
            currNode = currNode.next

            # traverseNode(currNode)

        elif list1.val < list2.val:
      
            print("list1:",list1.val)
            # create the new node and add the correct value
            newNode = ListNode(list1.val , None)
            list1 = list1.next
            # attach the new node the list
            currNode.next = newNode
        
            # update the current node
            currNode = currNode.next

            # traverseNode(currNode)
        
        elif list2.val <= list1.val:
            print("list2:",list2.val)
            # create the new node and add the correct value
            newNode = ListNode(list2.val , None)

            list2 = list2.next
            # attach the new node the list
            currNode.next = newNode
        
            # update the current node
            currNode = currNode.next

            # traverseNode(currNode)
        
    
    head = head.next
 


        
# Create the nodes for the first linked list
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

# Link the nodes together to form the linked list
node1.next = node2
node2.next = node3

# The first linked list is represented by the head node, which is node1
list1 = node1

# Create the nodes for the second linked list
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

# Link the nodes together to form the linked list
node4.next = node5
node5.next = node6

# The second linked list is represented by the head node, which is node4
list2 = node4

mergeTwoLists(list1,list2)
from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def find(self,item):

    current = self.head

    found = False
    counter = 0

    while current != None and not found:

      if current.data == item:
        found = True
      else:
        current = current.next
        counter += 1

    if found:
      return counter
    else:
      return -1

  def update(self, item):
    curr_node = self.head

    while curr_node.next != None:
      if curr_node.data[0] == key:
        curr_node.data = (curr_node[0], curr_node[1]+ 1)
      else:
        curr_node = curr_node.next


  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def print_nodes(self):
    current = self.head
    
    if current == None:
      #  change this too dont print if empty
      print('The linked list is empty.')
    else:
      for i in range(self.length()):
        # change below
        print(f'Node {i}: {current.data}')
        current = current.next
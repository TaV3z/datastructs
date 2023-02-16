class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        node = Node(data)
        if not self.head:
            self.tail = self.head = node
            return

        if not self.head.next:
            node.next = self.tail
            self.head = node
            return 

        node.next = self.head
        self.head = node

    def push_back(self, data):
        node = Node(data)
        if not self.head:
            self.tail = self.head = node
            return

        if not self.head.next:
            self.head.next = self.tail = node
            return 

        self.tail.next = node
        self.tail = node

    def pop_front(self):
        if not self.head:
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        node = self.head
        self.head = node.next
        del node

    def pop_back(self):
        if not self.head:
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        node = self.head
        while node.next != self.tail:
            node = node.next

        self.tail = node
        del node.next
        node.next = None

    def insert(self, data, index):
        if index == 0:
            self.push_front(data)
            return
        if not self.get_node(index):
            return

        node = Node(data)
        left = self.get_node(index)
        right = left.next

        left.next = node
        node.next = right

    def erase(self, index):
        if not self.head or index < 0:
            return

        if index == 0 and not self.head.next:
            self.pop_front()
            return

        left = self.get_node(index)
        if not left or not left.next:
            return

        right = left.next.next

        del left.next
        left.next = right

    def get_node(self, index):
        count = 0
        node = self.head

        while count != index - 1:
            if not node:
                return None
            node = node.next
            count +=1

        if not node or (not node.next and node != self.head):
            return None

        return node

    def __str__(self):
        """ [data] -> [data] -> None """

        node = self.head
        lst = ""
        while node:
            lst += f"[{node.data}] -> "
            node = node.next

        return lst + f"[None]"





lst = SinglyLinkedList()
print(lst)

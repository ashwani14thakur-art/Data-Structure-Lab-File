class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            new.next = new
            print("Inserted:", data)
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new
        new.next = self.head
        print("Inserted:", data)

    def search(self, key):
        if self.head is None:
            print("List is empty.")
            return False

        temp = self.head
        pos = 1
        while True:
            if temp.data == key:
                print(key, "found at position", pos)
                return True
            temp = temp.next
            pos += 1
            if temp == self.head:
                break

        print(key, "not found")
        return False

    def delete(self, key):
        if self.head is None:
            print("List is empty.")
            return

        curr = self.head
        prev = None

        # Only one node
        if curr.data == key and curr.next == self.head:
            self.head = None
            print("Deleted:", key)
            return

        # Deleting head
        if curr.data == key:
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
            print("Deleted:", key)
            return

        # Middle / end node
        prev = self.head
        curr = self.head.next
        while curr != self.head:
            if curr.data == key:
                prev.next = curr.next
                print("Deleted:", key)
                return
            prev = curr
            curr = curr.next

        print(key, "not found")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


cll = CircularLinkedList()

cll.insert(100)
cll.insert(200)
cll.insert(300)
cll.insert(400)

cll.display()

cll.search(300)
cll.search(150)

cll.delete(100)
cll.delete(300)

cll.display()

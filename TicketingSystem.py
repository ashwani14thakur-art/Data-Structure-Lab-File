class TicketQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return self.rear == self.size - 1

    def isEmpty(self):
        return self.front == -1 or self.front > self.rear

    def enqueue(self, ticket):
        if self.isFull():
            print("Queue is Full!")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = ticket
        print("Ticket Added:", ticket)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        print("Ticket Processed:", self.queue[self.front])
        self.front += 1

    def display(self):
        if self.isEmpty():
            print("No pending tickets.")
        else:
            print("Pending Tickets:", *self.queue[self.front : self.rear + 1])


def main():
    q = TicketQueue(5)

    while True:
        print("\n1. Add Ticket")
        print("2. Process Ticket")
        print("3. Show Tickets")
        print("4. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            q.enqueue(input("Enter Ticket ID: "))
        elif ch == "2":
            q.dequeue()
        elif ch == "3":
            q.display()
        elif ch == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
1

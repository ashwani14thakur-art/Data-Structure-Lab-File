# Simple Ticketing System using Linear Queue

class TicketQueue:
    def __init__(self, size):
        self.size = size
        self.queue = []
    
    def isFull(self):
        return len(self.queue) == self.size
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, ticket_id):
        if self.isFull():
            print("Queue is Full!")
        else:
            self.queue.append(ticket_id)
            print("Ticket Added:", ticket_id)
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            ticket = self.queue.pop(0)
            print("Ticket Processed:", ticket)
    
    def display(self):
        if self.isEmpty():
            print("No Pending Tickets")
        else:
            print("Pending Tickets:", self.queue)


def main():
    q = TicketQueue(5)

    while True:
        print("\n1. Add Ticket")
        print("2. Process Ticket")
        print("3. Show Tickets")
        print("4. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            t = input("Enter Ticket ID: ")
            q.enqueue(t)

        elif ch == "2":
            q.dequeue()

        elif ch == "3":
            q.display()

        elif ch == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

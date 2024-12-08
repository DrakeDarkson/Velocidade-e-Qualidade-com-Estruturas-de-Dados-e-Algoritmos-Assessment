from collections import deque

class CustomerServiceQueue:
    def __init__(self):
        self.queue = deque()

    def add_ticket(self, ticket):
        self.queue.append(ticket)
        print(f"Ticket '{ticket}' added to the queue.")

    def serve_ticket(self):
        if self.queue:
            ticket = self.queue.popleft()
            print(f"Serving ticket: {ticket}")
        else:
            print("No tickets to serve.")

    def show_queue(self):
        print("Current queue:", list(self.queue))

queue = CustomerServiceQueue()

queue.add_ticket("Ticket 1")
queue.add_ticket("Ticket 2")
queue.add_ticket("Ticket 3")

queue.show_queue()

queue.serve_ticket()
queue.serve_ticket()

queue.show_queue()

queue.serve_ticket()
queue.serve_ticket()

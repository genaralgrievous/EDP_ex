class Event:
    pass

# Define specific events
class TaskAssignmentEvent(Event):
    name = 'task_assignment'

    def __init__(self, task_id, worker_id, deadline):
        self.task_id = task_id
        self.worker_id = worker_id
        self.deadline = deadline

class TaskCompletionEvent(Event):
    name = 'task_completion'

    def __init__(self, task_id, worker_id):
        self.task_id = task_id
        self.worker_id = worker_id

class PaymentRequestEvent(Event):
    name = 'payment_request'

    def __init__(self, worker_id, amount):
        self.worker_id = worker_id
        self.amount = amount

class PaymentConfirmationEvent(Event):
    name = 'payment_confirmation'

    def __init__(self, worker_id, amount):
        self.worker_id = worker_id
        self.amount = amount

# Global communication queue
communication_queue = []

class Manager:
    def __init__(self, name):
        self.name = name

    def assign_task(self, task_id, worker_id, deadline):
        event = TaskAssignmentEvent(task_id=task_id, worker_id=worker_id, deadline=deadline)
        communication_queue.append(event)
        print(f'Event {event.name} emitted by {self.name}!')

class Worker:
    def __init__(self, worker_id, name):
        self.worker_id = worker_id
        self.name = name

    def complete_task(self, task_id):
        event = TaskCompletionEvent(task_id=task_id, worker_id=self.worker_id)
        communication_queue.append(event)
        print(f'Event {event.name} emitted by {self.name}!')

    def request_payment(self, amount):
        event = PaymentRequestEvent(worker_id=self.worker_id, amount=amount)
        communication_queue.append(event)
        print(f'Event {event.name} emitted by {self.name}!')

class Accountant:
    def __init__(self, name):
        self.name = name

    def handle_payment_request(self):
        current_event = communication_queue.pop(0)
        if isinstance(current_event, PaymentRequestEvent):
            print(f"{self.name} received payment request from Worker {current_event.worker_id} for {current_event.amount}.")
            event = PaymentConfirmationEvent(worker_id=current_event.worker_id, amount=current_event.amount)
            communication_queue.append(event)
            print(f'Event {event.name} emitted by {self.name}!')

class CEO:
    def __init__(self, name):
        self.name = name

    def review_system(self):
        print(f"{self.name} is reviewing the system state:")
        for event in communication_queue:
            print(f"Pending Event: {event.name}")

# Basic User Interface
if __name__ == "__main__":
    manager = Manager("Alice")
    worker1 = Worker(1, "Bob")
    worker2 = Worker(2, "Charlie")
    accountant = Accountant("Diana")
    ceo = CEO("Eve")

    # Simulating interactions
    manager.assign_task(task_id=101, worker_id=1, deadline="2025-01-30")
    manager.assign_task(task_id=102, worker_id=2, deadline="2025-02-15")

    worker1.complete_task(task_id=101)
    worker1.request_payment(amount=500)
    
    worker2.complete_task(task_id=102)
    worker2.request_payment(amount=700)

    accountant.handle_payment_request()
    accountant.handle_payment_request()

    ceo.review_system()


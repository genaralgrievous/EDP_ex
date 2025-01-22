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

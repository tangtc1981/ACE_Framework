import threading


class Bus:
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.message_log = []
        self.lock = threading.Lock()

    def messages(self):
        with self.lock:
            return list(self.message_log)

    def publish(self, sender: str, message: str):
        with self.lock:
            self.message_log.append((sender, message))
            for subscriber in self.subscribers:
                subscriber(sender, message)
            print(f"{threading.current_thread().name} Bus {self.name} received message from {sender}: {message}")

    def subscribe(self, listener):
        with self.lock:
            self.subscribers.append(listener)
            print(f"{threading.current_thread().name} Bus {self.name} was asked to subscribe listener {listener}")

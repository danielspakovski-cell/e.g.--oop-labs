from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(NotificationService):
    def send(self, message):
        print(f"[Email]: {message}")

class SMSNotification(NotificationService):
    def send(self, message):
        print(f"[SMS]: {message}")

class NotificationFactory(ABC):
    @abstractmethod
    def create_notifier(self) -> NotificationService:
        pass

class EmailFactory(NotificationFactory):
    def create_notifier(self) -> NotificationService:
        return EmailNotification()

class SMSFactory(NotificationFactory):
    def create_notifier(self) -> NotificationService:
        return SMSNotification()
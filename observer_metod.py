from abc import ABC, abstractmethod
class NewsAgency():
    def __init__(self):
        self.news = []
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)


    def notify_subscribers(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)

    def add_news(self, news):
        self.news.append(news)
        self.notify_subscribers(news)



class Subscriber(ABC):
    @abstractmethod
    def update(self, news):
        pass

class ConcreteSubscriber(Subscriber):
    def update(self, news):
        return f"Новости: {news}"





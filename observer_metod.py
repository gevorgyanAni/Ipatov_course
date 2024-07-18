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


news_agency = NewsAgency()

subscriber1 = ConcreteSubscriber()
subscriber2 = ConcreteSubscriber()

news_agency.subscribe(subscriber1)
news_agency.subscribe(subscriber2)

news_agency.add_news("Breaking News: New Python Version Released!")
news_agency.add_news("Latest News: Observer Pattern Explained!")
news_agency.unsubscribe(subscriber1)
news_agency.add_news("Final News: Subscriber1 won't see this.")

news_agency = NewsAgency()
subscriber = ConcreteSubscriber()

news_agency.subscribe(subscriber)
news_agency.add_news("Test News")
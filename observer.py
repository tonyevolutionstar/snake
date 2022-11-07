class Observer:
    def on_notify(self, entity, event):
        print("Entity: " + entity + " just " + event)


class Subject:
    def __init__(self):
        self.observers = {}
    def add_observer(self, event, event_handler):
        if event not in self.observers:
            self.events[event] = []
        self.observers[event].append(event_handler)

    def notify(self, event):
        for obs in self.observers[event]:
            obs(self)

class ScoreBoard(Observer):
    def __init__(self, entity):
        self.score = 0
        self.entity = entity
        self.observers = []

    def add_score(self):
        self.score += 1
      
    def status(self, st):
        if st not in self.observers:
            self.observers.append(st)
            self.on_notify(self.entity, st)

    def finish(self):
        game_score = "finished with " + str(self.score) + " score"
        if game_score not in self.observers:
            self.observers.append(game_score)
            self.on_notify(self.entity, game_score)
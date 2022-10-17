class Observer:
    def on_notify(self, entity, event):
        print("Entity: " + entity + " just " + event)

class Subject:
    def __init__(self):
        self.observers = []
    def add_observer(self, obs: Observer):
        self.observers.append(obs)
    def notify(self, entity, event):
        for obs in self.observers:
            obs.on_notify(entity, event)

class ScoreBoard(Observer):
    def __init__(self, entity):
        self.score = 0
        self.entity = entity
        
    def add_score(self):
        self.score += 1
        self.on_notify(self.entity, "score")

    def on_notify(self, entity, event):
       self.on_notify(entity, event)
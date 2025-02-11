class Pupil:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)
    def lose(self):
        import random
        if self.knowledge:
            self.knowledge.remove(random.choice(self.knowledge))

import random
import copy


class Hat:

    def __init__(self, **kwargs):
        self.contents = list()
        for key, value in kwargs.items():
            for n in range(0, value):
                self.contents.append(key)

    def draw(self, qty):
        if qty > len(self.contents):
            return self.draw(len(self.contents))
        else:
            drawn = list()
            for n in range(0, qty):
                ball = random.choice(self.contents)
                self.contents.remove(ball)
                drawn.append(ball)
            return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for n in range(0, num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        if compare_balls(expected_balls, balls):
            success += 1
    return success / num_experiments


def compare_balls(expected_balls, actual):
    for key, value in expected_balls.items():
        if actual.count(key) >= value:
            continue
        else:
            return False
    return True

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

xiaoming = Student('ming', 59)
xiaohong = Student('hong', 87)
xiaoming.print_score()
xiaohong.print_score()

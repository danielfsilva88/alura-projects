class Data:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def formatada(self):
        print("{0}/{1}/{2}".format(self.day, self.month, self.year))
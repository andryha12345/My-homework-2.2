import random
class Student:

    def __init__(self, name):

        self.name = name
        self.money = 50
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 1
        self.gladness -= 5
        self.money += 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 10
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.money <= 0:
            print("You need to go study")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress ={round(self.progress, 2)}")
        print(f"Money = {round(self.money, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" +self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_money()
        elif live_cube == 4:
            self.end_of_day()
            self.is_alive ()
        andriy = Student(name="Andriy")
        for day in range(365):
            if andriy.alive == False:
                break
                andriy.live(day)
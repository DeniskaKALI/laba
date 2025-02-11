class Person:
    def __init__(self, first_name, last_name, skill_level=1):
        self.first_name = first_name
        self.last_name = last_name
        self.skill_level = skill_level

    def __del__(self):
        print("Goodbye, Mr.", self.first_name, self.last_name)

    def info(self):
        return "{} {}, Skill Level: {}".format(self.first_name, self.last_name, self.skill_level)


worker = Person("I", "Kotov", 3)
helper = Person("D", "Myshev", 1)
maker = Person("O", "Risov", 2)

print(worker.info())
print(helper.info())
print(maker.info())

del helper
print("End of program")
input()
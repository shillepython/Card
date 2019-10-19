<<<<<<< HEAD
class Critter:
    """Виртуальный питомец"""
    total = 0

    @staticmethod   
    def status():
        print("Общее число зверюшек", Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'Имя: ' + self.name + '\n'
        ans += "Голод: " + str(self.hunger) + "\n"
        ans += "Скука: " + str(self.boredom) + "\n"
        return ans
        
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
=======
import time

class Critter(object):
    total = 0

    @staticmethod
    def status():
        print("critters all: " + str(Critter.total))

    def __init__(self, name, hungred = 0, boredom = 0):
        self.__name = name
        self.hungred = hungred
        self.boredom = boredom
        self.tiredness = 25
        Critter.total += 1

    def __str__(self):
        ans = "____________________\n"
        ans += "class Critter \n"
        ans += "name " + self.name + '\n'
        ans += "____________________"
        return ans

    def __pass_time(self, value):
        self.hungred += value
        self.boredom += value
        self.tiredness += value * 2
    
    def __all_propertys(self):
        return "name:", self.name, "hungred:", self.hungred, "boredom:", self.boredom, "tiredness:", self.tiredness, "total:", Critter.total, "name class: Critter"
>>>>>>> bd6ae7714a5b7f6644957a39f36e9ec985a409ff

    @property
    def name(self):
        return self.__name

<<<<<<< HEAD
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    def talk(self):
        print("Меня зовут", self.name)

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self, food = 5):
        print("Мррр...  Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
        
        
def main():
    crit_name = input("Как вы назовете свою зверюшку?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Моя зверюшка
    
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)
    
        choice = input("Ваш выбор: ")

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()
        
        # кормление зверюшки
        elif choice == "2":
            crit.eat(int(input("Сколько еды дать зверюшке?: ")))
         
        # игра со зверюшкой
        elif choice == "3":
            crit.play(int(input("Сколько играть со зверюшкой?: ")))
        
        #черный ход
        elif choice == "10":
            print(crit.__str__())


        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)
    
=======
    @property
    def mood(self):
        unhappiness = self.hungred + self.boredom
        if unhappiness < 5:
            m = "amazing"
        elif 5 <= unhappiness <= 10:
            m = "good"
        elif 10 < unhappiness <= 15:
            m = "Ok"
        else:
            m = "bad"
        return m

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Can't set new name")
        else :
            self.__name = new_name
            print("The name set COMPLETED!")

    def talk(self):
        print("My name", self.name)
        self.__pass_time(1)

    def hungred_count(self):
        print("hungred: " + str(self.hungred) + ", name: " + self.name)

    def mood_count(self):
        print("mood " + self.name + " is " + str(self.mood))

    def eat(self, food = 4):
        print("mrr... food")
        self.hungred -= food
        if self.hungred < 0:
            print("Is so much food")
            self.hungred = 0
        self.__pass_time(food)
        self.boredom -= 1
        self.hungred_count()

    def play(self, play = 4):
        print("mrr... play")
        self.boredom -= play
        if self.boredom < 0:
            print("Is so much play")
            self.boredom = 0
        self.__pass_time(play)
        self.hungred += 10
        print("boredom:", self.boredom, "name:", self.name)

    def sleep(self, time_ = 2):
        print("Goodnight bro!")
        print("I am go to bed")
        time.sleep(2)
        if time_ >= self.tiredness:
            time_ = self.tiredness

        if time_ != 0:
            for _ in range(time_):
                time.sleep(1)
                print("zzz..zzz")
                self.tiredness -= 1
        else:
            print("I can't sleep for a so short time")
        self.hungred += time_ // 2
        self.boredom += time_ // 2
print("tiredness:", self.tiredness, "name:", self.name)
def main():

    while True:
        ans = int(input())
        if ans == 1:
            print("Please enter name ", end = "")
            name = input("Enter creature's name: ")
        elif ans == 0:
            print("try again")


>>>>>>> bd6ae7714a5b7f6644957a39f36e9ec985a409ff
main()
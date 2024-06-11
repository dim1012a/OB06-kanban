import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")
        print(f"У {other.name} осталось {other.health} здоровья.\n")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра началась!\n")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if self.computer.is_alive():
                self.computer_turn()

        self.declare_winner()

    def player_turn(self):
        input(f"{self.player.name}, нажмите Enter чтобы атаковать...")
        self.player.attack(self.computer)

    def computer_turn(self):
        print(f"{self.computer.name} атакует...")
        self.computer.attack(self.player)

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

# Пример использования
player_name = input("Введите имя вашего героя: ")
game = Game(player_name)
game.start()
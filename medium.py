
class Person:

    def __init__(self, name, health,armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def count_damage(self, enemy):
        return self.damage / enemy.armor

    def fight(self, enemy):
        enemy.health -= self.count_damage(enemy)


class Player(Person):
    pass


class Enemy(Person):
    pass


class Game:

    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def start(self):
        last = self._player
        while self._player.health > 0 and self._enemy.health > 0:
            if last == self._player:
                self._enemy.fight(self._player)
                last = self._enemy
            else:
                self._player.fight(self._enemy)
                last = self._player
        if player.health > 0:
            print('Victory')
        else:
            print('Defeat')


player = Player('Petya', 900, 50, 30)
enemy = Enemy('Kolya', 890, 90, 25)
game = Game(player, enemy)

game.start()
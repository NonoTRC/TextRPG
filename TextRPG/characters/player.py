from data import vowels


class Player:
    def __init__(self):
        self.name = "Player"
        self.inventory = {}
        self.max_health = 100
        self.health = 100
        self.location = "Forest"
        self.stats = {}
        self.next_level_xp = 20
        self.xp = 0
        self.level = 1
        self.money = 0
        self.entered_shop = False
        self.is_god = False
        self.times_grinded = 0

    def add_item(self, item, amount=1):
        if item in self.inventory:
            self.inventory[item] += amount
        else:
            self.inventory[item] = amount

    def receive_item(self, item, amount=1):
        print(
            f"You received {amount if amount > 1 else "a"}{"n" if item[0] in vowels and amount == 1 else ""} {item}{"s" if amount > 1 else ""}.")
        self.add_item(item, amount)

    def lose_item(self, item, amount=1):
        self.inventory[item] -= amount

    def has_item(self, item):
        return item in self.inventory

    def item_count(self, item,):
        if self.has_item(item):
            return self.inventory.get(item)
        else:
            return 0

    def lose_health(self, damage):
        if self.health > damage:
            self.health -= damage
        else:
            self.health = 1

    def heal(self, amount=1):
        if self.health + amount > self.max_health:
            healed = self.max_health - self.health
            self.health = self.max_health
            return healed
        else:
            self.health += amount
            return amount

    def manual_heal(self):
        if self.health < self.max_health:
            if self.has_item("Apple") and self.has_item("Health Potion"):
                while True:
                    healing_item = input(
                        "What healing item would you like to use?").lower().strip()
                    if healing_item == "apple":
                        amount = self.heal(10)
                        self.lose_item("Apple", 1)
                        print(f"You ate an Apple and healed {amount} health.")
                        break
                    elif healing_item == "health potion" or healing_item == "potion":
                        self.heal(9999999)
                        self.lose_item("Health Potion", 1)
                        print("You drank a Health Potion and healed to max health.")
                        break
                    else:
                        print(
                            "Unknown command. Please Type \"Apple\" or \"Health Potion\"")
            elif self.has_item("Apple"):
                amount = self.heal(10)
                self.lose_item("Apple", 1)
                print(f"You ate an apple and healed {amount} health.")
            elif self.has_item("Health Potion"):
                self.heal(99999999)
                self.lose_item("Health Potion", 1)
                print("You drank a health potion and healed to max health.")
            else:
                print("You dont have any healing items.")
        else:
            print("You are at max health.")

    def has_health(self):
        return self.health > 5

    def increment_money(self, amount=1):
        self.money += amount

    def increment_stat(self, stat_name, amount=1):
        if stat_name in self.stats:
            self.stats[stat_name] += amount
        else:
            self.stats[stat_name] = amount

    def get_stat(self, stat_name):
        return self.stats.get(stat_name)

    def increment_xp(self, xp):
        if self.level != 15:
            self.xp += xp
            level_rewards = {
                1: (1, 10),
                2: (1, 15),
                3: (1, 20),
                4: (1, 25),
                5: (2, 15),
                6: (2, 20),
                7: (2, 25),
                8: (2, 30),
                9: (2, 35),
                10: (3, 20),
                11: (3, 25),
                12: (3, 30),
                13: (3, 35),
                14: (3, 40)
            }
            while self.level in level_rewards and self.xp >= self.next_level_xp:
                health, money = level_rewards[self.level]
                self.level_up(health, money)

    def level_up(self, health_increase, money_increase):
        if self.level != 15:
            self.level += 1
            self.xp -= self.next_level_xp
            self.max_health += health_increase
            self.heal(health_increase)
            self.money += money_increase
            self.next_level_xp = int(self.next_level_xp * 1.5)
            print(
                f"You leveled up to level {self.level} and gained {health_increase} max health and {money_increase} doubloons!")
            if self.level == 15:
                print("Well done you have reached the maximum level!")

from logic import boss_fight
from data import proceed
import random


class Shrek:
    def __init__(self):
        self.name = "Shrek"
        self.max_health = 500
        self.health = 500
        self.heal_threshold = 200
        self.inventory = {
            "Legendary Sword+": 1,
            "Health Potion": 3
        }

    def has_item(self, item):
        return item in self.inventory

    def lose_health(self, damage):
        if self.health > damage:
            self.health -= damage
        else:
            self.health = 0

    def lose_item(self, item, amount=1):
        self.inventory[item] -= amount

    def fight(self, game):
        if game.player.has_item("Legendary Sword"):
            if game.player.location == "Swamp":
                if self.health > 0:
                    print("Shrek: WHAT ARE YOU DOING IN MY SWAMP!")
                    print(
                        f"Your Legendary Sword senses the danger and transforms into the Legendary Arsenal! You can now use the commands slash, shoot and parry")
                    input(proceed)
                    boss_fight(self, game)
                else:
                    print("Shrek: ......get out of my swamp please......")
            else:
                print("Unknown command, Shrek cannot be found here, Type \"help enemies\" for a list of enemies and where you can find them.")
        else:
            print(f"{game.narrator.name}: Woah you should probably get the Legendary Sword before messing with the big fucking ogre!")

    def ready_attack(self, random):
        if random == 1:
            print("Shrek is looking at his grubby ogre hand.")  # slash
        elif random == 2:
            print("Shrek looks like he's about to puke.")  # shoot
        elif random == 3:
            print("Shrek is looking around.")  # parry
        elif random == 4:
            print("Shrek is looking weak.")  # heal

    def slash(self, game, outcome):  # attack is shrek attack outcome is player outcome
        print("Shrek swung his grubby hand at a high speed towards you.")
        if outcome == "win":
            dmg = random.randint(60, 100)
            print(
                f"Using your Legendary Shield you parried Shrek's hand and countered with the Legendary Sword dealing {dmg} damage.")
            self.lose_health(dmg)
        elif outcome == "draw":
            print(
                "You swung your Legendary Sword and it clashed with Shrek's hand, nullifying the blow.")
        elif outcome == "lose":
            dmg = random.randint(10, 25)
            print(
                f"You shoot your Legendary Bow but Shrek swats away the arrow and hits you across the face in the same swing, dealing {dmg} damage.")
            game.player.lose_health(dmg)
        elif outcome == "heal_lose":
            dmg = random.randint(10, 25)
            print(
                f"You had just enough time to finish healing before Shrek smacked you across the face, dealing {dmg} damage.")
            game.player.lose_health(dmg)

    def shoot(self, game, outcome):
        print("Shrek belches up a ball of slime and spits it towards you.")
        if outcome == "win":
            dmg = random.randint(60, 100)
            print(
                f"You slashed through the slime using your Legendary Sword and then landed a direct blow to Shrek, dealing {dmg} damage.")
            self.lose_health(dmg)
        elif outcome == "draw":
            print("Using your Legendary Bow, you shot an arrow that split the slime in half caused it to miss you.")
        elif outcome == "lose":
            dmg = random.randint(10, 25)
            print(
                f"You tried to deflect the slime using your Legendary Shield, but there was too much and it ended up soaking you anyways, dealing {dmg} damage.")
            game.player.lose_health(dmg)
        elif outcome == "heal_lose":
            dmg = random.randint(10, 25)
            print(
                f"You had just enough time to finish healing before getting covered in slime and taking {dmg} damage.")
            game.player.lose_health(dmg)

    def parry(self, game, outcome):
        print("Shrek picks up the outhouse door and awaits an attack.")
        if outcome == "win":
            dmg = random.randint(60, 100)
            print(
                f"Using your Legendary Bow, you shot an arrow that went right through the small peephole on the outhouse door, hitting Shrek in the eye and dealing {dmg} damage.")
            self.lose_health(dmg)
        elif outcome == "draw":
            print(
                "You readied your Legendary Shield and looked at Shrek doing the same thing, just wasting time")
        elif outcome == "heal_draw":
            print(
                "You had plenty of time to enjoy healing while Shrek looked at you through the outhouse door")
        elif outcome == "lose":
            dmg = random.randint(10, 25)
            print(
                f"You tried to slash through the outhouse door with your Legendary Sword, but Shrek deflected the attack, sending you flying and dealing {dmg} damage.")
            game.player.lose_health(dmg)

    def heal(self, game, outcome):
        print("Shrek drinks a healing potion that looks suspiciously similar to yours...")
        if outcome == "win":
            dmg = random.randint(60, 100)
            print(
                f"You attacked Shrek while he was drinking his potion, causing him to spill half of it on the floor, only healing 50 health and also dealt {dmg} damage to him.")
            self.health += 50
            self.lose_health(dmg)
            self.lose_item("Health Potion")
        elif outcome == "draw" or outcome == "heal_draw":
            print(
                f"Shrek drank his Health Potion and healed 100 health{" while you looked at him through your Legendary Shield" if outcome == "draw" else ""}.")
            self.health += 100
            self.lose_item("Health Potion")

    def defeat(self, game):
        print("Shrek: ARGHHHH OKAY OKAY YOU WIN! TAKE ALL MY THINGS BUT LEAVE ME MY SWAMP.")
        input(proceed)
        for item, amount in self.inventory.items():
            game.player.receive_item(item, amount)
        self.inventory.clear()
        input(proceed)

    def reset(self, game):
        self.health = 500
        self.inventory = {
            "Legendary Sword+": 1,
            "Health Potion": 3
        }
        game.narrator.player_ko(game)

from data import proceed
from logic import boss_fight
import random


class Narrator:
    def __init__(self):
        self.name = "Narrator"
        self.health = 99999

    def player_ko(self, game):
        game.player.location = "Shed"
        print("You suffered one too many attacks and lost consciousness...")
        input(proceed)
        print(f"{self.name}: Wake up {game.player.name}.")
        input(proceed)
        print(f"{self.name}: Are you okay? Shrek messed you up pretty good, I recommend getting stronger before trying again.\n Here, have a Health Potion to get you back up and running again.")
        game.player.receive_item("Health Potion")
        input(proceed)

    # boss fight

    def lose_health(self, damage):
        if self.health > damage:
            self.health -= damage
        else:
            self.health = 0

    def fight(self, game):
        game.player.heal(99999)
        print("You quickly dissasembled the Meat Grinder into a makeshift arsenal. You can now use the commands slash, shoot and parry")
        boss_fight(self, game)

    def ready_attack(self, random):
        if random == 1:
            print(f"{self.name} is looking up")  # slash
        elif random == 2:
            print(f"{self.name} is looking into your soul")  # shoot
        elif random == 3:
            print(f"{self.name} closes his eyes")  # parry
        elif random == 4:
            print(f"{self.name} looks deep in thought")  # heal

    def slash(self, game, outcome):  # attack is narrator attack outcome is player outcome
        print(
            f"{self.name} grabbed a rod of lightning from the heavens and swung it at you")
        if outcome == "win":
            dmg = random.randint(60, 100)
            print(
                f"Using a sheet of metal you parried the lightning bolt causing it to shock the narrator, dealing {dmg} damage.")
            self.lose_health(dmg)
        elif outcome == "draw":
            print(
                "You swung a blade and it split the lightning bolt in half, causing it to miss you.")
        elif outcome == "lose":
            dmg = random.randint(10, 25)
            print(
                f"You threw some meat at the lightning bolt. It did nothing. You took {dmg} damage.")
            game.player.lose_health(dmg)
        elif outcome == "heal_lose":
            dmg = random.randint(10, 25)
            print(
                f"You had just enough time to finish healing before getting zapped by a lightning bolt, dealing {dmg} damage.")
            game.player.lose_health(dmg)

    def shoot(self, game, outcome):
        print(f"{self.name} shot you with laser beams from his eyes.")
        if outcome == "win":
            dmg = random.randint(60, 100)
            print(
                f"You reflected the laser beams back at {self.name} with your shiny blades, dealing {dmg} damage.")
            self.lose_health(dmg)
        elif outcome == "draw":
            print(
                f"You threw some meat at the lasers causing {self.name} to stop shooting at you because he is vegan.")
        elif outcome == "lose":
            dmg = random.randint(10, 25)
            print(
                f"You tried to deflect the laser beams using a sheet of metal, but the lasers melted through it, dealing {dmg} damage.")
            game.player.lose_health(dmg)
        elif outcome == "heal_lose":
            dmg = random.randint(10, 25)
            print(
                f"You had just enough time to finish healing before getting lasered, dealing {dmg} damage.")
            game.player.lose_health(dmg)

    def parry(self, game, outcome):
        print(f"{self.name} conjured a shield out of thin air!")
        if outcome == "win":
            dmg = random.randint(60, 100)
            print(
                f"You threw some meat at {self.name} causing him to panic (because he is vegan). He then slipped and fell, dealing {dmg} damage.")
            self.lose_health(dmg)
        elif outcome == "draw":
            print(
                f"You raised up a sheet of metal and looked at {self.name} doing the same thing, just wasting time.")
        elif outcome == "heal_draw":
            print(
                f"You had plenty of time to enjoy healing while {self.name} stood behind his shield.")
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

from logic import boss_fight
from data import proceed
import random


class Jerma985:
    def __init__(self):
        self.name = "Jerma985"
        self.inventory = {
            "Meat Grinder": 1,
            "Health Potion": 99
        }
        self.health = 999999999999999
        self.heal_threshold = 1
        self.alive = True

    def fight(self, game):
        if self.alive:
            if game.player.times_grinded == 0:
                print(
                    "Jerma985: you want to fight me? how about a game of rock paper scissors instead.")
                boss_fight(self, game)
            elif 1 < game.player.times_grinded < 5:
                boss_fight(self, game)
            elif game.player.level == 15:
                print(
                    f"Jerma985: why am i shaking?\n{game.player.name}: Because I'm bored of you.")
                input(proceed)
                self.defeat(self, game)
            else:
                self.reset(self, game)

    def ready_attack(self, random):
        print("Jerma985 is holding his right fist above his left palm")

    def slash(self, game, outcome):
        print("Jerma threw scissors.")
        if outcome == "win":
            print(
                "Jerma changed his hand to be paper and insists that it was always that way.")
            game.player.health = 0
        elif outcome == "draw":
            print(
                "Jerma changed his hand to be rock and insists that it was always that way.")
            game.player.health = 0
        elif outcome == "lose":
            print("Jerma grabs your hand and leads you into the back room.")
            game.player.health = 0
        elif outcome == "heal_lose":
            print(
                "Jerma is confused why you didn't play along but acts as if he won anyways.")
            game.player.health = 0

    def shoot(self, game, outcome):
        print("Jerma threw paper.")
        if outcome == "win":
            print(
                "Jerma changed his hand to be rock and insists that it was always that way.")
            game.player.health = 0
        elif outcome == "draw":
            print(
                "Jerma changed his hand to scissors and insists it was always that way.")
            game.player.health = 0
        elif outcome == "lose":
            print("Jerma grabs your hand and leads you into the back room.")
            game.player.health = 0
        elif outcome == "heal_lose":
            print(
                "Jerma is confused why you didn't play along but acts as if he won anyways.")
            game.player.health = 0

    def parry(self, game, outcome):
        print("Jerma threw rock.")
        if outcome == "win":
            dmg = random.randint(60, 100)
            print(
                "Jerma changed his hand to scissors and insists it was always that way.")
            game.player.health = 0
        elif outcome == "draw":
            print(
                "Jerma changed his hand to be paper and insists that it was always that way.")
            game.player.health = 0
        elif outcome == "heal_draw":
            print(
                "Jerma is confused why you didn't play along but acts as if he won anyways.")
            game.player.health = 0
        elif outcome == "lose":
            print("Jerma grabs your hand and leads you into the back room.")
            game.player.health = 0

    def reset(self, game):
        print("You fade in and out of consciousness, hearing loud mechanical scraping and maniacal laughter.\nYou finally wake up and somehow you're in one piece.")
        game.player.location = "Forest"
        game.player.times_grinded += 1

    def defeat(self, game):
        print(
            f"You swung your Bloodstained Sword at Jerma985 and cut him into two pieces...\nYou walk into the back of the shop and take the Meat Grinder, there are {game.player.times_grinded} fingers next to it")
        game.player.recieve_item("Meat Grinder")
        input(proceed)

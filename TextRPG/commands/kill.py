from data import vowels
import random


def kill_creature(game, creature, creature_plural_ending, stat_name, weapon, drop_1, drop_1_min_amount, drop_1_max_amount,
                  drop_1_plural, xp_min_amount, xp_max_amount, damage_min_amount, damage_max_amount, money_min_amount, money_max_amount,
                  location_1, drop_2="", drop_2_min_amount=0, drop_2_max_amount=0, drop_2_plural=False):
    if game.player.has_item(weapon):
        if game.player.location == location_1:
            if random.random() < 0.9 or game.player.is_god:
                drop_count_1 = random.randint(
                    drop_1_min_amount, drop_1_max_amount)
                drop_count_2 = random.randint(
                    drop_2_min_amount, drop_2_max_amount)
                money = random.randint(money_min_amount, money_max_amount)
                xp = random.randint(xp_min_amount, xp_max_amount)
                damage = random.randint(
                    damage_min_amount, damage_max_amount) if not game.player.is_god else 0
                drop_1_string = f"{drop_count_1} {drop_1}{"s" if drop_1_plural and drop_count_1 > 1 else ""}"
                drop_2_string = f" and {drop_count_2} {drop_2}{"s" if drop_2_plural and drop_count_2 > 1 else ""}."
                print(
                    f"You killed a{"n" if creature[0] in vowels else ""} {creature} and took {damage} damage, but gained {xp} XP, {money} doubloons{"," if drop_2 != "" else " and"} {drop_1_string}{drop_2_string if drop_2 != "" else "."}")
                game.player.increment_stat(stat_name)
                game.player.lose_health(damage)
                game.player.add_item(drop_1, drop_count_1)
                if drop_2:
                    game.player.add_item(drop_2, drop_count_2)
                game.player.increment_money(money)
                game.player.increment_xp(xp)
            else:
                print(
                    f"You tried to attack a{"n" if creature[0] in vowels else ""} {creature} but it fought back hard. You lost {damage_max_amount + 5} health and ran away")
                game.player.lose_health(damage_max_amount + 5)
        else:
            print(
                f"Unknown command, {creature+creature_plural_ending} cannot be found here, Type \"help enemies\" for a list of enemies and where you can find them.")
    elif not game.player.has_item("Flimsy Sword"):
        print(
            f"You punched a{"n" if creature[0] in vowels else ""} {creature} with your bare hands.... It looked at you, unphased")
    else:
        if creature not in ("dog", "human"):
            print(
                f"{game.narrator.name}: Woah you should probably get a{"n" if weapon[0] in vowels else ""} {weapon} before messing with a{"n" if creature[0] in vowels else ""} {creature}.")
        else:
            print(
                "Unknown Command. Type \"help enemies\" for a list of enemies and where you can find them.")


def kill(target, game):
    if game.player.has_health() or game.player.is_god:
        if game.player.location == "Shop":
            if game.player.has_item("Bloodstained Sword") and target in ("jerma", "jerma985", "sus guy"):
                game.jerma.fight(game)
            else:
                print(
                    "Jerma985: hey stop swinging that around in my shop or i'll have to put the meat grinder to work")
        elif target == "rat":
            kill_creature(game, "rat", "s", "Rats Killed", "Flimsy Sword",
                          "Fur", 1, 2, False, 3, 9, 0, 10, 1, 3, "Shed")
        elif target == "zombie":
            kill_creature(game, "zombie", "s", "Zombies Killed",
                          "Weak Sword", "Flesh", 1, 2, False, 4, 12, 0, 15, 2, 4, "Graveyard")
        elif target == "ghost":
            kill_creature(game, "ghost", "s", "Ghosts Killed",
                          "Okay Sword", "Ectoplasm", 1, 2, False, 5, 15, 0, 20, 4, 6, "Graveyard")
        elif target == "troll":
            kill_creature(game, "troll", "s", "Trolls Killed",
                          "Good Sword", "Leather", 1, 3, False, 8, 18, 0, 25, 4, 6, "Badlands")
        elif target == "orc":
            kill_creature(game, "orc", "s", "Orcs Killed",
                          "Great Sword", "Bone", 2, 5, True, 10, 25, 0, 30, 5, 7, "Badlands")
        elif target == "minotaur":
            kill_creature(game, "minotaur", "s", "Minotaurs Killed",
                          "Amazing Sword", "Horn", 0, 2, True, 12, 30, 0, 35, 6, 8, "Badlands")
        elif target == "dog":
            game.player.increment_stat("Dogs Murdered", 0)
            if game.player.get_stat("Dogs Murdered") != 10:
                kill_creature(game, "dog", "s", "Dogs Murdered",
                              "Legendary Sword+", "Enemy", 1, 1, True, 0, 0, 0, 0, 0, 0, "Village")
            else:
                print(f"{game.name}: You've already killed all the dogs.")
        elif target == "human":
            game.player.increment_stat("Humans Murdered", 0)
            if game.player.get_stat("Humans Murdered") != 50:
                kill_creature(game, "human", "s", "Humans Murdered",
                              "Peta's Nightmare", "Felony", 1, 1, True, 0, 0, 0, 0, 0, 0, "Village")
            else:
                print(f"{game.name}: You've already killed everybody.")
        elif target in ("shrek", "ogre"):
            game.shrek.fight(game)
        else:
            print(
                "Unknown command. Type \"help enemies\" for a list of enemies and where you can find them.")
    else:
        print(
            f"{game.narrator.name}: You should do some other tasks before returning to battle as your health is dangerously low")

from data import vowels
import random


def gather_resource(game, action, resource_name, resource_plural_ending, stat_name, tool, item_1, item_1_min_amount, item_1_max_amount,
                    item_1_plural, xp_min_amount, xp_max_amount, location_1, location_2="", item_2=0, item_2_min_amount=0, item_2_max_amount=0,
                    item_2_plural=False, heal_amount=1):
    if game.player.has_item(tool):
        if game.player.location in (location_1, location_2):
            item_count_1 = random.randint(item_1_min_amount, item_1_max_amount)
            item_count_2 = random.randint(item_2_min_amount, item_2_max_amount)
            xp = random.randint(xp_min_amount, xp_max_amount)
            item_1_string = f"{item_count_1} {item_1}{"s" if item_1_plural and item_count_1 != 1 else ""}"
            item_2_string = f" and {item_count_2} {item_2}{"s" if item_2_plural and item_count_2 != 1 else ""}."
            print(f"You {"chopped a" if action == "chop" else "mined some"} {resource_name}{resource_plural_ending if action == "mine" else ""} and gained {xp} XP{"," if item_2 != 0 else " and"} {item_1_string}{item_2_string if item_2 != 0 else "."}")
            game.player.increment_stat(stat_name)
            game.player.heal(heal_amount)
            game.player.add_item(item_1, item_count_1)
            if item_2:
                game.player.add_item(item_2, item_count_2)
            game.player.increment_xp(xp)
        else:
            print(
                f"Unknown command, {resource_name+resource_plural_ending} cannot be found here. Type \"help resources\" for a list of resources and where to find them.")
    elif not game.player.has_item("Flimsy Axe"):
        print(f"{game.narrator.name}: Why are you punching a {resource_name}?")
    else:
        print(
            f"You need a{"n" if tool[0] in vowels else ""} {tool} to mine this {resource_name}.")


def chop(target, game):
    if game.player.location == "Shop":
        print(f"Jerma985: hey stop swinging that around in my shop or i'll have to put the meat grinder to work")
    elif target == "bush":
        gather_resource(game, "chop", "bush", "es", "Bushes Chopped",
                        "Flimsy Axe", "Stick", 1, 2, True, 1, 3, "Forest", "Shed")
    elif target == "spruce":
        gather_resource(game, "chop", "spruce tree", "s", "Spruce Chopped",
                        "Makeshift Axe", "Spruce Wood", 1, 2, False, 2, 4, "Forest", "", "Stick", 0, 1, True, 2)
    elif target == "pine":
        gather_resource(game, "chop", "pine tree", "s", "Pine Chopped",
                        "Cobbled Axe", "Pine Wood", 2, 4, False, 3, 5, "Forest", "Deep Woods", "Stick", 0, 1, True, 3)
    elif target == "beech":
        gather_resource(game, "chop", "beech tree", "s", "Beech Chopped",
                        "Iron Axe", "Beech Wood", 1, 3, False, 4, 6, "Deep Woods", "", 0, 0, 0, False, 4)
    elif target == "oak":
        gather_resource(game, "chop", "oak tree", "s", "Oak Chopped",
                        "Gold Axe", "Oak Wood", 1, 2, False, 5, 7, "Deep Woods", "", "Apple", 0, random.randint(0, 1), True, 5)
    elif target in ("helltree", "hell tree"):
        gather_resource(game, "chop", "helltree", "s",
                        "Helltrees Chopped", "Diamond Axe", "Hellwood", 1, 2, False, 15 if game.player.has_item("Hell Axe") else 0, 20 if game.player.has_item("Hell Axe") else 0, "Hell", "", 0, 0, 0, False, 7)
    else:
        print(
            "Unknown command. Type \"help resources\" for a list of resources and where to find them.")


def mine(target, game):
    if game.player.location == "Shop":
        print(f"Jerma985: hey stop swinging that around in my shop or i'll have to put the meat grinder to work.")
    elif target == "stone":
        gather_resource(game, "mine", "stone", "s", "Stones Mined",
                        "Flimsy Pickaxe", "Pebble", 1, 2, True, 1, 3, "Forest", "Quarry")
    elif target == "rock":
        gather_resource(game, "mine", "rock", "s", "Rocks Mined",
                        "Makeshift Pickaxe", "Rock", 2, 3, True, 2, 4, "Quarry", "", "Pebble", 0, 1, True, 2)
    elif target == "iron":
        gather_resource(game, "mine", "iron", "", "Iron Mined",
                        "Cobbled Pickaxe", "Iron", 2, 4, False, 3, 5, "Quarry", "Cave", "Rock", 0, 2, True, 3)
    elif target == "gold":
        gather_resource(game, "mine", "gold", "", "Gold Mined",
                        "Iron Pickaxe", "Gold", 1, 3, False, 4, 6, "Cave", "", "Rock", 0, 2, True, 4)
    elif target == "diamond":
        gather_resource(game, "mine", "diamond", "s", "Diamonds Mined",
                        "Gold Pickaxe", "Diamond", 1, 2, True, 5, 7, "Cave", "", "Rock", 0, 2, True, 5)
    elif target == "hellstone" or target == "hell stone":
        gather_resource(game, "mine", "hellstone", "", "Hellstone Mined",
                        "Diamond Pickaxe", "Hellstone", 1, 2, False, 15 if game.player.has_item("Hell Pickaxe") else 0, 20 if game.player.has_item("Hell Pickaxe") else 0, "Hell", "", 0, 0, 0, False, 7)
    else:
        print("Unknown command. Type \"help resources\" for a list of resources and where to find them.")

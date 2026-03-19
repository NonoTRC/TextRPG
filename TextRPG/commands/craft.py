from data import vowels


def show_crafts(game):

    # picks

    if not game.player.has_item("Hell Pickaxe"):
        if game.player.has_item("Diamond Pickaxe"):
            print("Hell Pickaxe - 100 Hellwood and 100 Hellstone \"Has a mystical aura that makes hellstone release its XP.\"")
        elif game.player.has_item("Gold Pickaxe"):
            print(
                "Diamond Pickaxe - 60 Oak and 40 Diamonds \"Strong enough to mine hellstone.\"")
        elif game.player.has_item("Iron Pickaxe"):
            print(
                "Gold Pickaxe - 60 Beech and 35 Gold \"Strong enough to mine diamonds.\"")
        elif game.player.has_item("Cobbled Pickaxe"):
            print(
                "Iron Pickaxe - 50 Pine and 30 Iron \"Strong enough to mine gold.\"")
        elif game.player.has_item("Makeshift Pickaxe"):
            print(
                "Cobbled Pickaxe - 25 Spruce and 15 Rocks \"Strong enough to mine iron.\"")
        elif game.player.has_item("Flimsy Pickaxe"):
            print(
                "Makeshift Pickaxe - 15 Sticks and 10 Pebbles \"Strong enough to mine rocks.\"")

    # axes

    if not game.player.has_item("Hell Axe"):
        if game.player.has_item("Diamond Axe"):
            print("Hell Axe - 100 Hellwood and 100 Hellstone \"Has a mystical aura that makes hell trees release their XP.\"")
        elif game.player.has_item("Gold Axe"):
            print(
                "Diamond Axe - 40 Oak and 60 Diamonds \"Strong enough to chop hell trees.\"")
        elif game.player.has_item("Iron Axe"):
            print(
                "Gold Axe - 35 Beech and 60 Gold \"Strong enough to chop oak trees.\"")
        elif game.player.has_item("Cobbled Axe"):
            print(
                "Iron Axe - 30 Pine and 50 Iron \"Strong enough to chop beech trees.\"")
        elif game.player.has_item("Makeshift Axe"):
            print(
                "Cobbled Axe - 15 Spruce and 25 Rocks \"Strong enough to chop pine trees.\"")
        elif game.player.has_item("Flimsy Axe"):
            print(
                "Makeshift Axe - 10 Sticks and 15 Pebbles \"Strong enough to chop spruce trees.\"")

    # armour

    if not game.player.has_item("Horned Helm"):
        if game.player.has_item("Bone Vest"):
            print(
                "Horned Helm - 16 Horns and 70 Gold \"Increases your max health by 30.\"")
        elif game.player.has_item("Leather Boots"):
            print(
                "Bone Vest - 100 Bones and 15 Leather \"Increases your max health by 30\"")
        elif game.player.has_item("Spooky Gloves"):
            print(
                "Leather Boots - 40 Leather and 50 Iron \"Increases your max health by 20\"")
        elif game.player.has_item("Fleshy Pants"):
            print(
                "Spooky Gloves - 20 Ectoplasm and 10 Fur \"Increases your max health by 20\"")
        elif game.player.has_item("Fur Socks"):
            print("Fleshy Pants - 20 Flesh \"Increases your max health by 10\"")
        else:
            print("Fur Socks - 16 Fur \"Increases your max health by 10\"")

    if game.player.has_item("Hell Pickaxe") and game.player.has_item("Hell Axe") and game.player.has_item("Horned Helm"):
        print("Well done you have crafted every single item!!!")


def craft(target, game):
    if target == "menu":
        show_crafts(game)

    # picks

    elif target == "makeshift pickaxe":
        make(game, "Makeshift Pickaxe", "You can now mine rocks in the quarry!", "Pebble", 10,
             "Stick", 15)
    elif target == "cobbled pickaxe":
        make(game, "Cobbled Pickaxe", "You can now mine for iron in the quarry!",
             "Rock", 15, "Spruce Wood", 25)
    elif target == "iron pickaxe":
        make(game, "Iron Pickaxe", "You can now mine for gold in the cave!",
             "Iron", 30, "Pine Wood", 50)
    elif target == "gold pickaxe":
        make(game, "Gold Pickaxe", "You can now mine for diamonds in the cave!",
             "Gold", 35, "Beech Wood", 60)
    elif target == "diamond pickaxe":
        make(game, "Diamond Pickaxe", "You can now mine hellstone in hell!",
             "Diamond", 40, "Oak Wood", 60)
    elif target == "hell pickaxe":
        make(game, "Hell Pickaxe", "Hellstone now drops xp!",
             "Hellstone", 100, "Hellwood", 100)

    # axes

    elif target == "makeshift axe":
        make(game, "Makeshift Axe", "You can now chop spruce trees in the forest!", "Pebble", 15, "Stick",
             10)
    elif target == "cobbled axe":
        make(game, "Cobbled Axe", "You can now chop pine trees in the forest!",
             "Rock", 25, "Spruce Wood", 15)
    elif target == "iron axe":
        make(game, "Iron Axe", "You can now chop beech trees in the deep woods!",
             "Iron", 50, "Pine Wood", 30)
    elif target == "gold axe":
        make(game, "Gold Axe", "You can now chop oak trees in the deep woods!",
             "Gold", 60, "Beech Wood", 35)
    elif target == "diamond axe":
        make(game, "Diamond Axe", "You can now chop helltrees in hell!",
             "Diamond", 60, "Oak Wood", 40)
    elif target == "hell axe":
        make(game, "Hell Axe", "Helltrees now drop xp!",
             "Hellstone", 100, "Hellwood", 100)

    # armour

    elif target == "fur socks":
        make(game, "Fur Socks", "Your max health increased by 10!", "Fur", 16)
    elif target == "fleshy pants":
        make(game, "Fleshy Pants", "Your max health increased by 10!", "Flesh", 20)
    elif target == "spooky gloves":
        make(game, "Spooky Gloves", "Your max health increased by 20!",
             "Ectoplasm", 20, "Fur", 10)
    elif target == "leather boots":
        make(game, "Leather Boots",
             "Your max health increased by 20!", "Leather", 40, "Iron", 50)
    elif target == "bone vest":
        make(game, "Bone Vest", "You max health increased by 30!",
             "Bone", 100, "Leather", 15)
    elif target == "horned helm":
        make(game, "Horned Helm", "Your max health increased by 30!",
             "Horn", 16, "Gold", 70)

    else:
        print("Unknown command. Type \"craft menu\" for a list of things you can craft.")


def make(game, item, message, item_1, item_1_amount, item_2="", item_2_amount=0):
    if not game.player.has_item(item):
        if game.player.item_count(item_1) >= item_1_amount:
            if game.player.item_count(item_2) >= item_2_amount or not item_2:
                print(
                    f"You crafted{" a" if item[-1] != "s" else ""}{"n" if item[0] in vowels and item[-1] != "s" else ""} {item}. {message}")
                game.player.add_item(item)
                game.player.lose_item(item_1, item_1_amount)
                if item_2:
                    game.player.lose_item(item_2, item_2_amount)
                if item == "Fur Socks" or item == "Fleshy Pants":
                    game.player.max_health += 10
                    game.player.heal(10)
                elif item == "Spooky Gloves" or item == "Leather Boots":
                    game.player.max_health += 20
                    game.player.heal(20)
                elif item == "Bone Vest" or item == "Horned Helm":
                    game.player.max_health += 30
                    game.player.heal(30)
            else:
                print(f"You don't have enough resources to craft this.")
        else:
            print(f"You don't have enough resources to craft this.")
    else:
        print(
            f"You already have{" a" if item[-1] != "s" else ""}{"n" if item[0] in vowels and item[-1] != "s" else ""} {item}.")

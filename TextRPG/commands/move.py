from commands.buy import show_shop


def move_to(game, location, requirement="", other_requirement=""):
    if not requirement or game.player.has_item(requirement) or game.player.has_item(other_requirement):
        if location == "shed":
            if game.player.location == location.title():
                print(f"You are already at the {location}.")
            else:
                game.player.location = location.title()
                print(f"You are now at the {location}.")
        elif location == "shop":
            game.player.location = "Shop"
            if not game.player.entered_shop:
                print("Jerma985: woah chat look at this strange guy.\nJerma985: how about you have a look at some of my items and stop worrying about the meat grinder.")
                game.player.entered_shop = True
            elif not game.player.has_item("Bloodstained Sword"):
                print("Jerma985: welcome to the shop, take a look at my wares.")
            show_shop(game)
        elif location == "hell":
            if game.player.location == location.title():
                print(f"You are already in {location}")
            else:
                game.player.location = location.title()
                print(f"You are now in {location}")
        elif game.player.location == location.title():
            print(f"You are already in the {location}.")
        else:
            game.player.location = location.title()
            print(f"You are now in the {location}")
    else:
        print("Unknown command. Type \"help areas\" for a list of areas")


def move(target, game):
    if target == "shed" or target == "forest":
        move_to(game, target)
    elif target == "quarry":
        move_to(game, target, "Flimsy Pickaxe")
    elif target == "graveyard":
        move_to(game, target, "Weak Sword")
    elif target == "badlands":
        move_to(game, target, "Good Sword")
    elif target == "swamp":
        move_to(game, target, "Legendary Sword")
    elif target == "shop":
        move_to(game, target, "Flimsy Sword")
    elif target == "village":
        move_to(game, target, "Legendary Sword+")
    elif target == "deep woods":
        move_to(game, target, "Iron Axe")
    elif target == "cave":
        move_to(game, target, "Iron Pickaxe")
    elif target == "hell":
        move_to(game, target, "Diamond Axe", "Diamond Pickaxe")
    else:
        print("Unknown command. Type \"help areas\" for a list of areas")

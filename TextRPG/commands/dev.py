def dev(target, game):
    if target == "money":
        game.player.increment_money(9999999999)
    elif target == "skip":
        game.player.location = "Shed"
        game.player.increment_stat("Bushes Chopped", 999999)
        game.player.increment_stat("Stones Mined", 999999)
        game.player.increment_stat("Rats Killed", 999999)
        game.player.add_item("Weak Sword")
        game.player.add_item("Stick", 999999)
        game.player.add_item("Pebble", 99999)
    elif target == "shrek":
        game.player.add_item("Legendary Sword")
        game.player.add_item("Health Potion", 5)
        game.player.add_item("Hell Axe")
        game.player.add_item("Hell Pickaxe")
        game.player.max_health = 220
        game.player.health = 220
    elif target[:5] == "give ":
        amount = input("How many?\n> ")
        game.player.add_item(target[5:].title(), amount)
        print(f"You received {amount} {target[5:].title()}.")

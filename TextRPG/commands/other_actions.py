def stats(target, game):
    print(
        f"Health: {game.player.health}/{game.player.max_health}\nLevel: {game.player.level}\nXP: {game.player.xp}/{game.player.next_level_xp}\nLocation: {game.player.location}\nMoney: {game.player.money}\nType \"more\" for more stats, or \"back\" to return.")
    while True:
        sub_command = input("> ").lower()
        if sub_command == "more":
            print(game.player.stats)
            return
        elif sub_command == "back":
            return
        else:
            print("Please type \"more\" or \"back\"")


def heal(target, game):
    game.player.manual_heal()


def health(target, game):
    print(f"You have {game.player.health}/{game.player.max_health} health.")


def level(target, game):
    print(
        f"You are level {game.player.level} and have {game.player.xp} XP. It is {game.player.next_level_xp - game.player.xp} XP until the next level up")


def money(target, game):
    print(f"You have {game.player.money} doubloons.")


def inventory(target, game):
    if not game.player.inventory:
        print("Your inventory is empty.")
    else:
        for item, amount in game.player.inventory.items():
            if amount:
                print(f"{item}{" x"+str(amount) if amount > 1 else ""}")


def v(target, game):
    if game.player.location == "Shop":
        print("Jerma985: imagine failing ctrl v but also WHY ARE YOU EVEN DOING IT IN MY SHOP STOP TRYNA BREAK MY SHIT.")
    else:
        print(f"{game.name}: Imagine failing ctrl v loser.")

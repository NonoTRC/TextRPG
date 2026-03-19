from data import proceed, vowels


def show_shop(game):
    if not game.player.has_item("Legendary Sword"):
        if game.player.has_item("Amazing Sword"):
            print("Jerma985: this is the strongest weapon that i have for sale, it's said to be strong enough to kill that terrifying ogre.")
            print("Legendary Sword - 500 doubloons")
        elif game.player.has_item("Great Sword"):
            print("Amazing Sword - 200 doubloons")
        elif game.player.has_item("Good Sword"):
            print(
                "Jerma985: it's not actually a greatsword, just a great sword (makes obscene face at you)")
            print("Great Sword - 150 doubloons")
        elif game.player.has_item("Okay Sword"):
            print("Good Sword - 125 doubloons")
        elif game.player.has_item("Weak Sword"):
            print(
                "Jerma985: yup i got more swords behind the counter, right next to these slippery baseballs...")
            print("Okay Sword - 100 doubloons")
        elif game.player.has_item("Flimsy Sword"):
            print("Weak Sword - 50 doubloons")
    elif game.player.has_item("Legendary Sword+"):
        if not game.player.confronted_jerma:
            print(f"{game.player.name}: Why did you give Health Potions to Shrek.")
            input(proceed)
            print("Jerma985: what can i say, business doesn't descriminate. wouldn't want to get cancelled now would i?")
            input(proceed)
            game.player.confronted_jerma = True
    elif game.player.has_item("Bloodstained Sword") and game.player.times_grinded == 0:
        print(
            f"Jerma985: {game.narrator.name} warned me about you... don't try anything funny or ill have to use the meat grinder.")
    if game.player.times_grinded == 0:
        print("Health Potion - 50 doubloons")
    elif game.player.times_grinded == 1:
        print("Jerma985: you're back?!?!? get over here!")
    elif game.player.times_grinded == 2:
        print("Jerma985: you must really want to play rock paper scissors then. okay come get some.")
    elif game.player.times_grinded == 3:
        print("Jerma985: i dont know how or why you keep coming back because you know it always is going to end up with you in the meat grinder.")
    elif game.player.times_grinded == 4:
        print("Jerma985: okay okay one last game.")
    elif game.player.times_grinded <= 5:
        print(f"{game.player.name}: i'm done playing games now.")
        input(proceed)
        print("Jerma985: have you not realised that you can't kill me?")


def purchase(game, item, price, prev_sword, message, amount=1):
    if (game.player.has_item(prev_sword) and not game.player.has_item(item)) or item == "Health Potion":
        if game.player.money >= price:
            if item == "Legendary Sword":
                print(
                    "Jerma985: don't be afraid to buy some health potions before your big battle.")
            else:
                print(
                    f"You bought{" a" if amount == 1 else str(amount)}{"n" if item[0] in vowels and amount == 1 else ""} {item}{"s" if amount > 1 else ""}. {message}")
            game.player.add_item(item, amount)
            game.player.money -= price * int(amount)
        else:
            print("Jerma985: you dont have enough money for this, would be a shame if you fell into the meat grinder.")
    else:
        print("Jerma985: i dont have that sword in stock buddy how about you pick one from the tiny list.")
        show_shop(game)


def buy(target, game):
    if game.player.location == "Shop":
        if target == "health potion":
            amount = input("Jerma985: how many would you like to buy?\n> ")
            if amount.isdigit():
                purchase(game, "Health Potion", 50, "",
                         "\nJerma985: thanks for your money.", amount)
            else:
                print(
                    "Jerma985: do you have a dent in your head? come back when you learn how to write numbers.")
                show_shop(game)
        elif target == "weak sword":
            purchase(game, "Weak Sword", 50, "Flimsy Sword",
                     "You can now fight zombies in the graveyard.")
        elif target == "okay sword":
            purchase(game, "Okay Sword", 100, "Weak Sword",
                     "You can now fight ghosts in the graveyard.")
        elif target == "good sword":
            purchase(game, "Good Sword", 125, "Okay Sword",
                     "You can now fight trolls in the badlands.")
        elif target == "great sword":
            purchase(game, "Great Sword", 150, "Good Sword",
                     "You can now fight orcs in the badlands.")
        elif target == "amazing sword":
            purchase(game, "Amazing Sword", 200, "Great Sword",
                     "You can now fight minotaurs in the badlands.")
        elif target == "legendary sword":
            purchase(game, "Legendary Sword", 500, "Amazing Sword",
                     "You can now battle Shrek in the swamp.")
        else:
            print("Unknown command. Type \"help\" for more info.")
    else:
        print("Unkown command. Type \"help\" for more info.")

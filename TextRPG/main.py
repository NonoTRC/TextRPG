from logic import command
from data import Game, vowels, proceed
game = Game()


print(f"\n{game.narrator.name}: Welcome to my text based rpg, I dont have a name for it so how about you do the honours.")
game.name = input("Game: What would you like to name me? \n> ").strip()
for attempts in range(3):
    if game.name.strip() == "":
        print(f"{game.narrator.name}: How about you actually type something this time")
        game.name = input("What should this game be called? \n> ")
    elif game.name.strip() != "":
        print(f"{game.narrator.name}: {game.name}... I like it (:")
        break
else:
    print(f"{game.narrator.name}: Okay fine I'll just name it nothing then.")
    game.name = "nothing"
input(proceed)
print(f"{game.narrator.name}: Well in this rpg you will chop trees, mine rocks and kill monsters to gain xp, basic enough stuff.")
input(proceed)
print(f"{game.narrator.name}: I think I left some old tools in that shed over there. I have no use for them anymore so you can have them. Try typing the command \"move shed\"")
while game.player.location != "Shed":
    command(game)
game.player.receive_item("Flimsy Axe")
game.player.receive_item("Flimsy Pickaxe")
game.player.receive_item("Flimsy Sword")
input(proceed)
print(f"{game.narrator.name}: Those tools aren't great but it'll be enough to start. Try chopping that bush over there next to the shed using the \"chop bush\" command")
while game.player.get_stat("Bushes Chopped") is None:
    command(game)
print(f"{game.narrator.name}: Good job! Lets try mining a stone next. You won't find many near my shed though, so try moving to the quarry. \nOnce you're there, use the \"mine stone\" command")
input(proceed)
print(f"{game.name}: Type \"help\" if you get stuck at any point.")
if game.player.get_stat("Stones Mined") is not None:
    print(f"{game.narrator.name}: You broke one already?")
    input(proceed)
else:
    while game.player.get_stat("Stones Mined") is None:
        command(game)
print(f"{game.narrator.name}: Well done! You're great at this! Now time for a real challenge.\nThere is a rat infestation behind the shed, how about you kill 5 of them with the \"kill rat\" command.")
game.player.increment_stat("Rats Killed", 0)
if game.player.get_stat("Rats Killed") >= 5:
    print(f"{game.narrator.name}: You killed 5 of them already?")
    input(proceed)
else:
    while game.player.get_stat("Rats Killed") < 5:
        command(game)
print(f"{game.narrator.name}: Wow you're a natural!")
input(proceed)
print(f"{game.narrator.name}: How about you go to the shop and see if you can afford something. I'd recommend buying a new sword for yourself.")
while not game.player.has_item("Weak Sword") and not game.player.has_item("Health Potion"):
    command(game)
print(f"{game.narrator.name}: Wow thats a nice {"sword" if game.player.has_item("Weak Sword") else "Health Potion"}. Im sure you'll put it to good use.")
input(proceed)
game.player.name = input(
    f"{game.narrator.name}: I just realised that I never got your name. What is it?\n> ")
while game.player.name.strip() == "":
    game.player.name = input(
        f"{game.narrator.name}: How about you actually type something this time.\n> ")
print(f"{game.narrator.name}: {game.player.name}? Thats a nice name! I've always wanted to have a name but I've always just been the narrator.")
while True:
    naming_choice = input(
        f"{game.name}: Do you want to name the narrator?\n> ").lower()
    if naming_choice == "y" or naming_choice == "yes":
        game.narrator.name = input(
            f"{game.name}: What would you like to name him?\n> ")
        while True:
            while game.narrator.name.lower() == game.name.lower():
                game.narrator.name = input(
                    f"{game.name}: Come on you can't give him the same name as the game.\n> ")
            while game.narrator.name.lower() == "jerma985":
                game.narrator.name = input(
                    f"{game.name}: Come on you can't name him after the famous shopkeeper Jerma985.\n> ")
            while game.narrator.name.lower() == game.player.name.lower():
                game.narrator.name = input(
                    f"{game.name}: Come on you can't name him after yourself that's really concerning.\n> ")
            while game.narrator.name.strip() == "":
                game.narrator.name = input(
                    f"{game.name}: You said you wanted to name him so name him.\n> ")
            if game.narrator.name.lower() not in (game.name.lower(), "jerma985", game.player.name.lower(), ""):
                break
        print(
            f"{game.narrator.name}: You want to name me {game.narrator.name}? I love it so much, Thank you!!!")
        input(proceed)
        break
    elif naming_choice == "n" or naming_choice == "no":
        print(f"{game.name}: Best not to get attached")
        input(proceed)
        break
    else:
        print(f"{game.name}: Please type yes or no")
if not game.player.has_item("Makeshift Axe") and not game.player.has_item("Makeshift Pickaxe"):
    if not game.player.item_count("Stick") >= 15 or not game.player.item_count("Pebble") >= 15:
        print(f"{game.narrator.name}: So {game.player.name}, how about you try collecting a few more resources and I'll show you how to make some new tools. Try collecting 15 sticks and 15 pebbles.")
        while game.player.item_count("Stick") < 15 or game.player.item_count("Pebble") < 15:
            command(game)
    print(f"{game.narrator.name}: You should have enough resources to make a tool now. Try crafting one. Type \"craft menu\" for a list of things you can craft.")
    while not game.player.has_item("Makeshift Pickaxe") and not game.player.has_item("Makeshift Axe"):
        command(game)
    print(f"{game.narrator.name}: Thatll serve you much better that your previous tool, you should be able to harvest some new resources now.")
    input(proceed)
print(f"""{game.narrator.name}: I think youve gotten the hang of things now and you should be ready to progress on your own. 
Thank you for keeping me company {game.player.name} and I'll keep watch over you during your adventure. Safe travels!""")
input(proceed)
print(f"{game.narrator.name}: oh also theres a scary fucking ogre you gotta kill good luckkkkkkk.")
while not game.player.has_item("Legendary Sword"):
    command(game)
print(f"{game.narrator.name}: Wow is that really the Legendary Sword? Go to the swamp {game.player.name}, and slay that scary fucking ogre!")
while not game.player.has_item("Legendary Sword+"):
    command(game)
print(f"{game.narrator.name}: Well done you have slain the mighty ogre and have finished {game.name}!!! We can now leave in peace free from the nasty ogre!\nThank you for everything {game.player.name}, it has been nice knowing you and I wish you the best on your future endeavours.")
input(proceed)
print(f"{game.name}: There is always more to do... Don't you find it a little suspicious that Shrek used the same Health Potions as you?")
while game.player.get_stat("Dogs Murdered") is None:
    command(game)
print(f"{game.narrator.name}: Why did you kill that dog...")
input(proceed)
while game.player.get_stat("Dogs Murdered") > 3:
    command(game)
print(f"{game.narrator.name}: Please stop killing dogs, they dont even drop anything.")
input(proceed)
while game.player.get_stat("Dogs Murdered") > 10:
    command(game)
print("A new weapon materialises in your bloodied hands...")
game.player.receive_item("Peta's Nightmare")
input(proceed)
print(f"{game.narrator.name}: What. I didn't even know that sword existed, but I dont think it was worth it to kill all of those dogs. Not like theres anything left to kill anyways")
input(proceed)
while game.player.get_stat("Humans Murdered") is None:
    command(game)
print(f"{game.narrator.name}: You're killing people now? I can't be a part of this anymore {game.player.name}. You're on your own now.")
input(proceed)
game.player.is_god = True
game.player.health = game.player.max_health
while game.player.get_stat("Humans Murdered") > 10:
    command(game)
print(f"{game.name}: Interesting path you've chosen {game.player.name}.")
input(proceed)
while game.player.get_stat("Humans Murdered") > 50:
    command(game)
print(f"A new weapon emerges from the blood stained village...")
game.player.receive_item("Bloodstained Sword")
input(proceed)
while not game.player.has_item("Meat Grinder"):
    command(game)
print(f"{game.narrator.name}: I didn't think you would actually try to kill Jerma985. I can't let you go any further {game.player.name}, I'm putting an end to this now.")
input(proceed)
game.narrator.fight(game)

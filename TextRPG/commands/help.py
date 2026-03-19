def game_help(target, game):
    flimsy_axe = game.player.has_item("Flimsy Axe")
    flimsy_pickaxe = game.player.has_item("Flimsy Pickaxe")
    makeshift_axe = game.player.has_item("Makeshift Axe")
    makeshift_pickaxe = game.player.has_item("Makeshift Pickaxe")
    cobbled_axe = game.player.has_item("Cobbled Axe")
    cobbled_pickaxe = game.player.has_item("Cobbled Pickaxe")
    iron_axe = game.player.has_item("Iron Axe")
    iron_pickaxe = game.player.has_item("Iron Pickaxe")
    gold_axe = game.player.has_item("Gold Axe")
    gold_pickaxe = game.player.has_item("Gold Pickaxe")
    diamond_axe = game.player.has_item("Diamond Axe")
    diamond_pickaxe = game.player.has_item("Diamond Pickaxe")
    flimsy_sword = game.player.has_item("Flimsy Sword")
    weak_sword = game.player.has_item("Weak Sword")
    okay_sword = game.player.has_item("Okay Sword")
    good_sword = game.player.has_item("Good Sword")
    great_sword = game.player.has_item("Great Sword")
    amazing_sword = game.player.has_item("Amazing Sword")
    legendary_sword = game.player.has_item("Legendary Sword")
    legendary_sword_plus = game.player.has_item("Legendary Sword+")
    petas_nightmare = game.player.has_item("Peta's Nightmare")
    bloodstained_sword = game.player.has_item("Bloodstained Sword")
    meat_grinder = game.player.has_item("Meat Grinder")

    if target in ("command", "commands"):
        command_help_lines = [
            "To use a command you must type the prefix (such as chop) followed the target (such as bush).",
            "Here is a list of prefixes and what they do.",
            "-chop - chops bushes and trees",
            "-mine - mines stones and ores",
            "-kill - attacks an enemy"
            "-move - moves you to another area",
            "-craft - crafts an item if you have sufficient resources, type craft menu for a list of things you can craft",
            "-buy - buys an item if you are in the shop",
            "-stats - displays your stats",
            "-inventory - shows the contents of your inventory",
            "-health - shows how much health you have",
            "-level - shows what level you are and how much xp until the next level",
            "-money - shows how much money you have",
            "-heal - uses a healing item",
        ]
        print("\n".join(command_help_lines))

    elif target in ("resource", "resources", "chop", "mine", "break", "chopping", "mining", "breaking"):
        resource_help_lines = [
            "Here is a list of resources, where to find them, and what tool you need to gather them",
            "bush - found in the forest and at the shed, requires a flimsy axe to chop",
            "stone - found in the forest and in the quarry, requires a flimsy pickaxe to mine",
        ]
        if makeshift_axe:
            resource_help_lines.append(
                "spruce - found in the forest, requires a makeshift axe to chop")
            resource_help_lines.append(
                f"pine - found in the forest{" and in the deep woods" if game.player.has_item("Iron Axe") else ""}, requires a cobbled axe to chop")
        if makeshift_pickaxe:
            resource_help_lines.append(
                "rock - found in the quarry, requires a makeshift pickaxe to mine")
            resource_help_lines.append(
                f"iron - found in the quarry{" and in the cave" if game.player.has_item("Iron Pickaxe") else ""}, requires a cobbled pickaxe to mine")
        if iron_axe:
            resource_help_lines.append(
                "beech - found in the deep woods, requires an iron axe to chop")
            resource_help_lines.append(
                "oak - found in the deep woods, requires a gold axe to chop")
        if iron_pickaxe:
            resource_help_lines.append(
                "gold - found in the cave, requires an iron pickaxe to mine")
            resource_help_lines.append(
                "diamond - found in the cave, requires a gold pickaxe to mine")
        if diamond_axe or diamond_pickaxe:
            resource_help_lines.append(
                "hellwood - found in hell, requires a diamond axe to chop")
            resource_help_lines.append(
                "hellstone - found in hell, requires a diamond pickaxe to mine")
        print("\n".join(resource_help_lines))

    elif target in ("enemy", "enemies", "kill", "slay"):
        enemy_help_lines = [
            "Here is a list of enemies, where to find them, and what sword you need to fight them",
            "-rat - drops fur, found behind the shed, requires a flimsy sword to defeat",
        ]
        if weak_sword:
            enemy_help_lines.append(
                "zombie - drops flesh, found in the graveyard, requires a weak sword to defeat")
            enemy_help_lines.append(
                "ghost - drops ectoplasm, found in the graveyard, requires an okay sword to defeat")
        if good_sword:
            enemy_help_lines.append(
                "troll - drops leather, found in the badlands, requires a good sword to defeat")
            enemy_help_lines.append(
                "orc - drops bones, found in the badlands, requires a great sword to defeat")
            enemy_help_lines.append(
                "minotaur - drops horns, found in the badlands, requires an amazing sword to defeat")
        if legendary_sword:
            enemy_help_lines.append(
                "shrek - found in the swamp, requires a legendary sword to defeat")
        if legendary_sword_plus:
            enemy_help_lines.append(
                "dog - found in the village, requires a legendary sword+ to murder")
        if petas_nightmare:
            enemy_help_lines.append(
                "human - found in the village, requires peta's nightmare to murder")
        if bloodstained_sword:
            enemy_help_lines.append(
                "jerma - found in the shop, requires the bloodstained sword to fight")
        if meat_grinder:
            enemy_help_lines.append(
                "narrator - found in his shed, requires the meat grinder to eviscerate")
        print("\n".join(enemy_help_lines))

    elif target in ("move", "go", "area", "areas", "locations", "location", "place", "places"):
        area_help_lines = [
            "This is a list of all the areas you can visit currently",
            f"forest - bushes{" and stones" if not makeshift_axe and not cobbled_axe else ", stones,"}{" and spruce" if makeshift_axe and not cobbled_axe else ""}{" spruce, and pine" if cobbled_axe else ""} can be found here",
            "shed - bushes and rats can be found here",
        ]
        if flimsy_pickaxe:
            area_help_lines.append(
                f"quarry - stones{" and rocks" if makeshift_pickaxe and not cobbled_pickaxe else ""}{", rocks, and iron" if cobbled_pickaxe else ""} can be found here")
        if game.player.money >= 15:
            area_help_lines.append("shop - jerma985 can be found here")
        if iron_axe:
            area_help_lines.append(
                f"deep woods - pine{" and beech" if not gold_axe else ", beech, and oak"} can be found here")
        if iron_pickaxe:
            area_help_lines.append(
                f"cave - iron{" and gold" if not gold_pickaxe else ", gold, and diamonds"} can be found here")
        if diamond_axe or diamond_pickaxe:
            area_help_lines.append(
                "hell - hellstone and hellwood can be found here")
        if weak_sword:
            area_help_lines.append(
                f"graveyard - zombies{" and ghosts" if okay_sword else ""} can be found here")
        if good_sword:
            area_help_lines.append(
                f"badlands - trolls{" and orcs" if great_sword and not amazing_sword else ""}{", orcs, and minotaurs" if amazing_sword else ""} can be found here")
        if legendary_sword:
            area_help_lines.append("-swamp - Shrek can be found here")
        if legendary_sword_plus:
            area_help_lines.append(
                "village - people with their cute dogs can be found here")
        print("\n".join(area_help_lines))

    elif target in ("boss", "boss command", "bosses", "boss commands", "command boss", "command bosses", "commands boss", "commands bosses"):
        boss_commands_help_lines = [
            "This is a list of all the commands you can do during a boss fight",
            f"{"-rock - beats scissors and ends your turn" if bloodstained_sword else "-parry - uses your legendary shield to parry an incoming attack"}",
            f"{"-paper - beats rock and ends your turn" if bloodstained_sword else "-shoot - uses your legendary bow to shoot an arrow"}",
            f"{"-scissors - beats paper and ends your turn" if bloodstained_sword else "-slash - uses your legendary sword to slash a boss"}",
            "-heal - uses a healing item and ends your turn",
            "-health - displays your health",
            "-inventory - displays your inventory",
            "-boss health - displays the boss's health",
        ]
        print("\n".join(boss_commands_help_lines))

    elif target in ("general", "game", "info", "about"):
        general_help_lines = [
            "This is a list of helpful game mechanics to get you started",
            "gathering resources restores a small amount of health",
            "killing enemies drains health but they drop money",
            "leveling up and crafting armour raises your max hp",
            "leveling up also gives you money",
        ]
        print("\n".join(general_help_lines))

    else:
        main_help_lines = [
            "Type \"help\" followed by what you want more info about:",
            "-commands",
            "-resources",
            "-enemies",
            "-areas",

        ]
        if legendary_sword:
            main_help_lines.append("-boss commands")
        main_help_lines.append("-general")
        print("\n".join(main_help_lines))

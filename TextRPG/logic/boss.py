import random


def boss_command(game, boss_attack):
    from commands import heal, health, inventory
    while True:
        boss_command = input("> ").lower().strip()
        if boss_command in ("slash", "scissors"):
            if boss_attack == 1:
                game.boss.slash(game, "draw")
            elif boss_attack == 2:
                game.boss.shoot(game, "win")
            elif boss_attack == 3:
                game.boss.parry(game, "lose")
            elif boss_attack == 4:
                game.boss.heal(game, "win")
            break
        elif boss_command in ("shoot", "paper"):
            if boss_attack == 1:
                game.boss.slash(game, "lose")
            elif boss_attack == 2:
                game.boss.shoot(game, "draw")
            elif boss_attack == 3:
                game.boss.parry(game, "win")
            elif boss_attack == 4:
                game.boss.heal(game, "win")
            break
        elif boss_command == ("parry", "rock"):
            if boss_attack == 1:
                game.boss.slash(game, "win")
            elif boss_attack == 2:
                game.boss.shoot(game, "lose")
            elif boss_attack == 3:
                game.boss.parry(game, "draw")
            elif boss_attack == 4:
                game.boss.heal(game, "draw")
            break
        elif boss_command == "heal":
            game.player.manual_heal()
            if boss_attack == 1:
                game.boss.slash(game, "heal_lose")
            elif boss_attack == 2:
                game.boss.shoot(game, "heal_lose")
            elif boss_attack == 3:
                game.boss.parry(game, "heal_draw")
            elif boss_attack == 4:
                game.boss.heal(game, "heal_draw")
            break
        elif boss_command == "health":
            health("", game, "")
        elif boss_command == "inventory":
            inventory("", game, "")
        elif boss_command == "boss health" or boss_command == "health boss":
            print(f"{game.boss.name} has {game.boss.health} health remaining.")
        else:
            print("Unknown command. Type \"help boss\" for a list of boss commands.")


def boss_fight(game):
    while game.boss.health > 0:
        if game.player.has_health == False:
            game.boss.reset(game)
            break
        boss_attack = random.randint(1, 3)
        if game.boss.health < game.boss.heal_threshold and random.randint(1, 2) == 2 and game.boss.has_item("Health Potion"):
            boss_attack = 4
        game.boss.ready_attack(boss_attack)
        boss_command(game, boss_attack)
    game.boss.defeat(game.player)

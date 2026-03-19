from commands import chop, mine, kill, move, buy, craft, stats, inventory, health, level, money, heal, dev, game_help, v


def command(game):
    print("")
    command = input("> ").lower().strip()
    parts = command.split(maxsplit=1)
    if parts:
        verb = parts[0]
        target = parts[1] if len(parts) > 1 else ""
        action = actions.get(verb)
        if action:
            action(target, game)
        else:
            print("Unknown command. Type \"help\" for a list of commands.")


actions = {
    "chop": chop,
    "cut": chop,
    "mine": mine,
    "break": mine,
    "kill": kill,
    "slay": kill,
    "fight": kill,
    "attack": kill,
    "move": move,
    "move to": move,
    "go": move,
    "go to": move,
    "buy": buy,
    "purchase": buy,
    "jerma985": buy,
    "craft": craft,
    "make": craft,
    "stats": stats,
    "stat": stats,
    "inventory": inventory,
    "inv": inventory,
    "health": health,
    "hp": health,
    "level": level,
    "lvl": level,
    "xp": level,
    "exp": level,
    "wallet": money,
    "money": money,
    "cash": money,
    "heal": heal,
    "dev": dev,
    "help": game_help,
    "help!": game_help,
    "v": v,
}

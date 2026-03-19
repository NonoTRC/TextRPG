from characters import Jerma985, Player, Shrek, Narrator


class Game:
    def __init__(self):
        self.name = "game"
        self.player = Player()
        self.narrator = Narrator()
        self.jerma = Jerma985()
        self.shrek = Shrek()

##########################AGENTE##############################
#game
import os
import importlib.util
spec = importlib.util.spec_from_file_location("Brick", os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/agent.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
Brick = foo.Brick

def builder():
    def new_perception(self, entry):
        if entry == "info_edge":
            return "Invalid perception"
        else:
            return True

    def new_action(self, entry):
        if entry == "info_edge":
            return "Invalid reaction"
        else:
            print ("Do nothing!")

    state_interactions = [0]
    output_interactions = [0]
    wander = Brick("Wander", "New State", 0, state_interactions,output_interactions, new_perception, new_action)
    bricks_game = []
    bricks_game.append(wander)
    ##brick created##

    def new_action1(self, entry):
        if entry == "info_edge":
            return "Prepare shotgun\n                    Relax Mode!"
        if entry == "Player is near":
            print ("Prepare shotgun!")
        if entry == "Player is out of sight":
            print ("Relax mode!")

    def new_perception1(self, entry):
        if entry == "info_edge":
            return "Player is near\n                    Player is out of sight"
        if entry == "info_edge_from_0":
            return "Player is near"
        if entry == "info_edge_from_1":
            return "Player is out of sight"
        if entry == "Player is near":
            if self.current_state == 0:
                return True
            else:
                return False
        if entry == "Player is out of sight":
            if self.current_state == 1:
                return True
            else:
                return False

    state_interactions = [1, 0, 1]
    output_interactions = [1, 1, 0]
    attack = Brick("Attack", "New State", 1, state_interactions, output_interactions, new_perception1, new_action1)
    bricks_game.append(attack)
    ##brick created##

    def new_perception2(self, entry):
        if entry == "info_edge":
            return "Player is idle\n                    Player is attacking back"
        if entry == "info_edge_from_2":
            return "Player is idle"
        if entry == "info_edge_from_1":
            return "Player is attacking back"
        if entry == "Player is idle":
            if self.current_state == 2:
                return True
            else:
                return False
        if entry == "Player is attacking back":
            if self.current_state == 1:
                return True
            else:
                return False

    def new_action2(self, entry):
        if entry == "info_edge":
            return "Vendetta!\n                    OMG!"
        if entry == "Player is idle":
            print ("Vendetta!")
        if entry == "Player is attacking back":
            print ("OMG!")

    state_interactions = [0, 2, 1, 2, 2]
    output_interactions = [0, 2, 2, 0, 0]
    evade = Brick("Evade", "New State", 2, state_interactions, output_interactions, new_perception2, new_action2)
    bricks_game.append(evade)
    ##brick created##

    def new_perception3(self, entry):
        if entry == "info_edge":
            return "Healthpoints are low\n                    Found aid"
        if entry == "info_edge_from_2":
            return "Healthpoints are low"
        if entry == "info_edge_from_3":
            return "Found aid"
        if entry == "Healthpoints are low":
            return True
        if entry == "Found aid":
            return True

    def new_action3(self, entry):
        if entry == "info_edge":
            return "I'm not good!\n                    That's better!"
        if entry == "Healthpoints are low":
            print ("I'm not good!")
        if entry == "Found aid":
            print ("That's better!")

    state_interactions = [0, 1, 3, 0, 3, 3, 3]
    output_interactions = [0, 0, 3, 0, 0, 0, 0]
    find_aid = Brick("Find Aid", "New State", 3, state_interactions, output_interactions, new_perception3, new_action3)
    bricks_game.append(find_aid)

    return foo.AbstractAgent(bricks_game, "game")

##########################AGENTE##############################
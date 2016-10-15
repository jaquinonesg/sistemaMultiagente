##########################AGENTE##############################
#game
import importlib.util
spec = importlib.util.spec_from_file_location("State", "/home/diego/Documents/virtualEnv/agent.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
State = foo.State

def builder():
    def new_perception(self, entry):
        return True

    def new_action(self, entry):
        print ("Do nothing!")

    state_interactions = [0]
    output_interactions = [0]
    wander = State("Wander", "New State", 0, state_interactions,output_interactions, new_perception, new_action)
    states_game = []
    states_game.append(wander)
    ##state created##

    def new_action1(self, entry):
        if entry == "Player is near":
            print ("Prepare shotgun!")
        if entry == "Player is out of sight":
            print ("Relax mode!")

    def new_perception1(self, entry):
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
    attack = State("Attack", "New State", 1, state_interactions, output_interactions, new_perception1, new_action1)
    states_game.append(attack)
    ##state created##

    def new_perception2(self, entry):
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
        if entry == "Player is idle":
            print ("Vendetta!")
        if entry == "Player is attacking back":
            print ("OMG!")

    state_interactions = [0, 2, 1, 2, 2]
    output_interactions = [0, 2, 2, 0, 0]
    evade = State("Evade", "New State", 2, state_interactions, output_interactions, new_perception2, new_action2)
    states_game.append(evade)
    ##state created##

    def new_perception3(self, entry):
        if entry == "info_edge_from_2":
            return "Healthpoints are low"
        if entry == "info_edge_from_3":
            return "Found aid"
        if entry == "Healthpoints are low":
            return True
        if entry == "Found aid":
            return True

    def new_action3(self, entry):
        if entry == "Healthpoints are low":
            print ("I'm not good!")
        if entry == "Found aid":
            print ("That's better!")

    state_interactions = [0, 1, 3, 0, 3, 3, 3]
    output_interactions = [0, 0, 3, 0, 0, 0, 0]
    find_aid = State("Find Aid", "New State", 3, state_interactions, output_interactions, new_perception3, new_action3)
    states_game.append(find_aid)

    return foo.AbstractAgent(states_game, "game")
    # -   0 1 2 3  states
    #
    # 0   0 1 2 3
    # 1   1 0 2 3    (next state)
    # 2   0 1 3 0
    # 3
    # perceptions
    # -   0 1 2 3  states
    #
    # 0   0 0 0 0
    # 1   1 1 0 0     (output)
    # 2   0 2 2 0
    # 3   0 0 3 0
    # perceptions

##########################AGENTE##############################
##########################AGENTE##############################
#calculator
import importlib.util
spec = importlib.util.spec_from_file_location("State", "/home/diego/Documents/virtualEnv/agent.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
State = foo.State

def builder():

    def new_perception(self, entry):
        return True

    def new_action(self, entry):
        print ("Invalid entry: ", entry)

    state_interactions = [0]
    output_interactions = [0]
    waiting_number = State("Waiting Number", "Entry any real number", 0, state_interactions,output_interactions, new_perception, new_action)
    states_calculator = []
    states_calculator.append(waiting_number)
    ##state created##

    def new_action1(self, entry):
        self.memory.append(entry)
        print ("Stored: ", entry)

    def new_perception1(self, entry):
        if entry == "info_edge_from_0":
            return "First Real number"
        if entry == "info_edge_from_2":
            return "Second Real number"
        try:
            check = float(entry)
            return True
        except ValueError:
            return False

    state_interactions = [1, 1, 1]
    output_interactions = [1, 0, 0]
    waiting_operator = State("Waiting Operator", "Entry +, -, *, /", 1, state_interactions, output_interactions, new_perception1, new_action1)
    states_calculator.append(waiting_operator)
    ##state created##

    def new_perception2(self, entry):
        if entry == "info_edge_from_1":
            return "Operators (+, -, *, /)"
        operators = ["+", "-", "*", "/"]
        if entry in operators:
            return True
        else:
            return False

    def new_action2(self, entry):
        if self.memory[1] == "+":
            print ("solution: ", float(self.memory[0]) + float(entry))
            self.memory.clear()
        else:
            if self.memory[1] == "-":
                print ("solution: ", float(self.memory[0]) - float(entry))
                self.memory.clear()
            else:
                if self.memory[1] == "*":
                    print ("solution: ", float(self.memory[0]) * float(entry))
                    self.memory.clear()
                else:
                    print ("solution: ", float(self.memory[0]) / float(entry))
                    self.memory.clear()

    state_interactions = [0, 2, 2, 0, 2]
    output_interactions = [0, 1, 0, 2, 0]
    waiting_final_number = State("Waiting Final number", "Entry second number", 2, state_interactions, output_interactions, new_perception2, new_action2)
    states_calculator.append(waiting_final_number)

    return foo.AbstractAgent(states_calculator, "calculator")
    # -   Waiting_number    Waiting_operator       Waiting_second_number       states
    #
    # 0   Waiting_number    Waiting_operator       Waiting_second_number
    # 1   Waiting_operator  Waiting_operator       Waiting_number (next state)
    # 2   Waiting_number    Waiting_second_number  Waiting_second_number
    # perceptions
    # -   0 1 2  states
    #
    # 0   0 0 0
    # 1   1 0 2     (output)
    # 2   0 1 0
    # perceptions


##########################AGENTE##############################
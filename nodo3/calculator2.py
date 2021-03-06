##########################AGENTE##############################
#calculator
import os
import importlib.util
import math
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
            print ("Invalid entry: ", entry)

    state_interactions = [0]
    output_interactions = [0]
    waiting_number = Brick("Waiting Number", "Entry any real number", 0, state_interactions,output_interactions, new_perception, new_action)
    bricks_calculator = []
    bricks_calculator.append(waiting_number)
    ##brick created##

    def new_action1(self, entry):
        if entry == "info_edge":
            return "Store first number"
        else:
            self.memory.append(entry)
            print ("Stored: ", entry)

    def new_perception1(self, entry):
        if entry == "info_edge":
            return "Recieve real number"
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
    waiting_operator = Brick("Waiting Operator", "Entry +, -, *, /", 1, state_interactions, output_interactions, new_perception1, new_action1)
    bricks_calculator.append(waiting_operator)
    ##brick created##

    def new_perception2(self, entry):
        if entry == "info_edge":
            return "Recieve operator"
        if entry == "info_edge_from_1":
            return "Operators (+, -, *, /)"
        operators = ["+", "-", "*", "/"]
        if entry in operators:
            return True
        else:
            return False

    def new_action2(self, entry):
        if entry == "info_edge":
            return "Return the result"
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
    waiting_final_number = Brick("Waiting Final number", "Entry second number", 2, state_interactions, output_interactions, new_perception2, new_action2)
    bricks_calculator.append(waiting_final_number)
    ##brick created##

    def new_perception3(self, entry):
        if entry == "info_edge":
            return "Recieve trigonometric function"
        if entry == "info_edge_from_3":
            return "Recieve trigonometric function"
        if entry == "info_edge_from_1":
            return "Jump to trigonometric calculator"
        operators = ["sen()", "cos()", "tan()"]
        if self.current_state == 1:
            if entry == "trigo":
                return True
        else:
            if entry in operators:
                return True
            else:
                return False

    def new_action3(self, entry):
        if entry == "info_edge":
            return "Return trigonometric result"
        if entry == "sen()":
            print ("solution: sen(", float(self.memory[0]), ")= ", float(math.sin(float(self.memory[0]))))
            self.memory.clear()
        else:
            if entry == "cos()":
                print ("solution: cos(", float(self.memory[0]), ")= ", float(math.cos(float(self.memory[0]))))
                self.memory.clear()
            else:
                print ("solution: tan(", float(self.memory[0]), ")= ", float(math.tan(float(self.memory[0]))))
                self.memory.clear()

    state_interactions = [0, 3, 2, 0, 3, 3, 3]
    output_interactions = [0, 1, 0, 3, 0, 0, 0]
    waiting_trigo_operator = Brick("Waiting trigonometric operator", "Entry trigonometric operator", 3, state_interactions, output_interactions, new_perception3, new_action3)
    bricks_calculator.append(waiting_trigo_operator)


    return foo.AbstractAgent(bricks_calculator, "calculator2")

##########################AGENTE##############################
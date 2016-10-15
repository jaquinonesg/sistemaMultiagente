#!/usr/bin/env python


from __future__ import generators
import json
import importlib.util
import os
import random


class State(object):
    def __init__(self, name, description, id, state_interactions, output_interactions, new_perception, new_action):
        self.name = name
        self.description = description
        self.id = id
        self.state_interactions = state_interactions
        self.output_interactions = output_interactions
        self.new_perception = new_perception
        self.new_action = new_action


# - 0 1 2 3 ... states
# 0
# 1
# 2
# ..
# perceptions


class AbstractAgent(object):
    def state_info(self):
        print (self.states[self.current_state].name, ": ", self.states[self.current_state].description)

    def __init__(self, states, description):
        self.description = description
        self.memory = []
        self.current_state = 0
        self.actions = []
        self.perceptions = []
        self.states = states
        self.next_state_function_matrix = []
        self.output_function_matrix = []
        self.size = len(states)
        self.dispersion = []

        if self.size == 0:
            pass
        else:
            for i in range(len(self.states)):  # Building of the matrix and the alphabets
                state = self.states[i]
                self.perceptions.append(state.new_perception)
                self.actions.append(state.new_action)
                if i == 0:
                    self.next_state_function_matrix.append(state.state_interactions)
                    self.output_function_matrix.append(state.output_interactions)
                else:
                    for j in range(state.id+1):
                        if j == 0:
                            self.next_state_function_matrix.append([state.state_interactions[j]])
                            self.output_function_matrix.append([state.output_interactions[j]])
                        else:
                            self.next_state_function_matrix[state.id].append(state.state_interactions[j])
                            self.output_function_matrix[state.id].append(state.output_interactions[j])
                    for j in range(state.id):
                        self.next_state_function_matrix[state.id-1-j].append(state.state_interactions[state.id+1+j])
                        self.output_function_matrix[state.id-1-j].append(state.output_interactions[state.id + 1+ j])
            self.state_info()

    def alphabet_in_check(self, entry):
        for i in range(len(self.states)):
            check = self.states[len(self.states)-1-i].new_perception(self, entry)
            if check:
                return len(self.states)-1-i

    def output_function(self, index, entry):
        self.actions[index](self, entry)

    def behave(self, entry):
        perception = self.alphabet_in_check(entry)
        action = self.output_function_matrix[perception][self.current_state]
        self.output_function(action, entry)
        self.current_state = self.next_state_function_matrix[perception][self.current_state]
        self.state_info()

    def add_nodes_edges(self, type_graph):
        nodes = []
        for n in self.states:
            nodes.append((str(n.id), {'label': n.name}))
        for h in nodes:
            if isinstance(h, tuple):
                type_graph.node(h[0], **h[1])
            else:
                type_graph.node(h)
        edges = []

        for i in range(len(self.next_state_function_matrix)):
            for j in range(len(self.next_state_function_matrix)):
                if self.next_state_function_matrix[i][j] == j:
                    pass
                else:
                    info_request = "info_edge_from_" + str(j)
                    edge_name = self.perceptions[i](self, info_request) + "  "
                    edges.append(((str(j), str(self.next_state_function_matrix[i][j])), {'label': edge_name}))
        for e in edges:
            if isinstance(e[0], tuple):
                type_graph.edge(*e[0], **e[1])
            else:
                type_graph.edge(*e)
        return type_graph

    def apply_styles(self, type_graph, styles):
        type_graph.graph_attr.update(
            ('graph' in styles and styles['graph']) or {}
        )
        type_graph.node_attr.update(
            ('nodes' in styles and styles['nodes']) or {}
        )
        type_graph.edge_attr.update(
            ('edges' in styles and styles['edges']) or {}
        )
        return type_graph

    def render_agent(self):
        import graphviz as gv
        digraph = gv.Digraph(format='svg')
        render_graphic = self.add_nodes_edges(digraph)
        render_graphic.render('render/agente')   #render the state diagram
        print ("########### FIVE TUPLE ###########")  #Render the five tuple
        print ("States: {")
        for i in self.states:
            print ("            ", i.id, ". ", i.name, ":  ", i.description)
        print ("                }")
        print ("")    #First the States
        print ("Input alphabet: {")
        #for i in range(len(self.states)):
            #for j in range(len(self.states)):
                #edge_name = self.perceptions[i](self, "info_edge_from_" + str(j))
                #if edge_name not = "":
                #   list =
                #    print ("            ", self.states[i].id, ". ", self.states[i].name, ":  ", self.states[i].description)
        #print ("                }")
        #print ("")

    def disperse_agent(self):

        nodes = ["nodo1", "nodo2", "nodo3", "nodo4"]
        x1 = []  # Number of nodes
        p = 0.01  # Distribution parameter
        sum = 0
        # Calculate the geometric distribution
        for i in range(len(nodes)):
            x1.append(((1-p)**i)*p)
            sum = sum + x1[i]  # store the acumulative probability
        # Truncate the distribution
        for i in range(len(x1)):
            if i == 0:
                x1[i]= (x1[i]/sum)
            else:
                x1[i] = x1[i-1] + (x1[i]/sum)
        rdm_numbers = []
        for i in range(self.size):
            random_number = random.random()
            for j in range(len(x1)):
                if random_number < x1[j]:
                    rdm_numbers.append(j)
                    break
        f = open(self.description + '.py', 'r')
        data_split = f.read().split("##state created##")
        f.close()
        # Request for the existing nodes in the network to the environment
        for p in range(len(data_split)):
            # Randomly choose a node according to a geometric truncated distribution
            # print (np.random.geometric(.01, 3))
            file_name = "/dis" + self.description + str(p) + ".txt"
            random_node = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/" + nodes[rdm_numbers[p]]
            with open(random_node + file_name, 'w') as outfile:
                json.dump(data_split[p], outfile)
        # now the agent is inactive
        f = open(self.description + '.py', 'w')
        inactive_code = "##########################AGENTE##############################\n#calculator\nimport importlib.util\nspec = importlib.util.spec_from_file_location('State', '/home/diego/Documents/virtualEnv/agent.py')\nfoo = importlib.util.module_from_spec(spec)\nspec.loader.exec_module(foo)\nState = foo.State\n\ndef builder():\n    states_calculator = []\n    agent = foo.AbstractAgent(states_calculator, '" + self.description + "')\n    agent.size = " + str(self.size) + "\n    agent.dispersion = " + str(rdm_numbers) + "\n    agent.recopile_agent()\n    print ('Agent recopiled')"
        f.write(inactive_code)
        f.close()

    def recopile_agent(self):
        # Request for the existing nodes in the network to the environment
        nodes = ["nodo1", "nodo2", "nodo3", "nodo4"]
        agent_code = {}
        for i in range(self.size):
            file_name = "dis" + self.description + str(i) + ".txt"
            search_node = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/" + nodes[self.dispersion[i]] + "/" + file_name
            if os.path.exists(search_node):
                with open(search_node, 'r') as outfile:
                    agent_code[file_name] = json.load(outfile)
                os.remove(search_node)
        code_array = sorted(agent_code.keys())
        for i in range(len(code_array)):
            if i == 0:
                original_code = agent_code[code_array[i]]
            else:
                original_code = original_code + "##state created##" + agent_code[code_array[i]]
        with open(os.getcwd() + "/" + self.description + ".py",
                  'w') as outfile:
            outfile.write(original_code)


########################################################
########################################################

class AgentFactory:
    factories = {1: 'Reflex', 2: 'Reactive'}

    def add_factory(agent_id, agent_factory):
        agent_factory.factories.put[agent_id] = agent_factory

    add_factory = staticmethod(add_factory)

    # A Template Method:
    def create_agent(agent_id, entry_agent):
        if agent_id not in AgentFactory.factories:
            AgentFactory.factories[agent_id] = eval(agent_id + '.Factory()')
        spec = importlib.util.spec_from_file_location("builder", entry_agent)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        return foo.builder()

    create_agent = staticmethod(create_agent)


########################################################
########################################################

class Reflex(AbstractAgent):
    def behave(self):
        print("behave.reflex")


    class Factory:
        def create(self): return Reflex()

########################################################
########################################################


class Reactive(AbstractAgent):

    def behave(self):
        print("behave.Reactive")

    class Factory:
        def create(self): return Reactive()


########################################################
########################################################


class Utility(AbstractAgent):

    def behave(self):
        print("behave.Utility")

    class Factory:
        def create(self): return Utility()


########################################################
########################################################


class Rational(AbstractAgent):

    def behave(self):
        print("behave.Rational")

    class Factory:
        def create(self): return Rational()


########################################################
########################################################


class Social(AbstractAgent):

    def behave(self):
        print("behave.Social")

    class Factory:
        def create(self): return Social()
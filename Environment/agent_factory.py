#!/usr/bin/env python


from __future__ import generators


class AbstractAgent(object):
    # TODO implement transition output function (DIEGO)
    # TODO draw agent behaviour with graphviz (DIEGO)
    # TODO complete function: agent request and join (JUAN)
    # TODO implement ACL (IVAN)

    def __init__(self, alphabet_in='ai', alphabet_out='ao', states='states'):
        self.alphabet_in = alphabet_in
        self.alphabet_out = alphabet_out
        self.states = states

    def next_state_function(self):
        pass

    def output_function(self):
        pass

    def addition(self, a, b):
        return a + b

########################################################
########################################################


class AgentFactory:
    factories = {1: 'Reflex', 2: 'Reactive'}

    def add_factory(agent_id, agent_factory):
        agent_factory.factories.put[agent_id] = agent_factory

    add_factory = staticmethod(add_factory)

    # A Template Method:
    def create_agent(agent_id):

        if agent_id not in AgentFactory.factories:
            AgentFactory.factories[agent_id] = eval(agent_id + '.Factory()')
        return AgentFactory.factories[agent_id].create()

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


########################################################
########################################################

"""
def agent_name(n):
    types = AbstractAgent.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__


agent = [AgentFactory.create_agent(i) for i in agent_name(3)]

for agent in agent:
    agent.behave()
    print(agent.addition(2, 3))

agent2 = AgentFactory.create_agent("Social")
agent2.behave()
agent2 = AgentFactory.create_agent("Rational")
agent2.behave()
print(agent2.addition(1, 8))
"""
if __name__ == '__main__':
    from agent import *
    import os
    import importlib.util
    continueX = True
    while continueX:
        print("Enter a node to work")
        entry = input("")
        if entry == "exit":
            continueX = False
        else:
            if os.path.exists(os.getcwd()+"/" + entry):
                os.chdir(os.getcwd()+"/" + entry)
                os.getcwd()
                print("Enter an agent to create")
                entry_agent = input("")
                if os.path.isfile(entry_agent + ".py"):
                    name = os.getcwd()+ "/" + entry_agent +".py"
                    agentNew = AgentFactory.create_agent("Reflex", name)
                    continueY = True
                    while continueY:
                        entry_agent_behave = input("")
                        if entry_agent_behave == "exit":
                            os.chdir(os.getcwd())
                            continueY = False
                        else:
                            if entry_agent_behave == "render":
                                agentNew.render_agent()
                                print ("Agent rendered")
                                agentNew.behave("")
                            else:
                                if entry_agent_behave == "disperse":
                                    agentNew.disperse_agent()
                                    print ("Agent disperse")
                                    os.chdir(os.getcwd())
                                    continueY = False
                                else:
                                    agentNew.behave(entry_agent_behave)
                else:
                    print("Agent does not exist")
                    os.getcwd()
            else:
                print("Node invalid")
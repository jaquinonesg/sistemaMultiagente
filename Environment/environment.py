#!/usr/bin/env python


import socket
import sys
import server
import subprocess
from agent_factory import*
from threading import Thread



#####################################################################
#####################################################################
#####################################################################


class Environment(object):
    """Environment for MAS"""

    def __init__(self, port):
        print('##################################')
        print('  MAS environment - TLON Project  ')
        print('##################################')
        print('Initial Setup...')
        #self.initialize_adhoc_network()
        self.info_local_machine = server.get_info_local_machine()
        self.port = port

        #self.nodes_directory = server.get_info_active_nodes()
        #self.local_agents = {}
        #self.agent_directory = {}
        server_thread = Thread(target=self.initialize_server())
        server_thread.start()

    def initialize_server(self):
        '''

        :return:
        '''
        environment_server = server.ThreadedTCPServer((self.info_local_machine[0], self.port),
                                                      server.ClientThreadRequest)
        server_thread = Thread(target=environment_server.serve_forever)
        server_thread.start()

    def initialize_adhoc_network(self):
        '''

        :return:
        '''
        print('Configuring TLON-ADHOC network...')
        if subprocess.call(['sh', 'adhoc.sh']) == 0:
            print('TLON-ADHOC is available!')
        else:
            print('It is not possible setup ad hoc network in %s' % self.info_local_machine[1])
            sys.exit(0)

def main():
    ############################################################
    #               Environment - Initial Setup
    ############################################################
    # TODO implement singleton design pattern in the environment instance
    # TODO It is necessary implement the exception in the server file
    # TODO define environment states

    environment = Environment(12345)
    print('Info-Local Machine : %s' % str(environment.info_local_machine))
    #print('Info-Active Nodes: ', environment.nodes_directory)
    # print('Info-Local Agents: ', environment.local_agents)
    # print('Info-AbstractAgent Directory: ', environment.agent_directory)

    ############################################################
    #               Local agents - setup
    ############################################################

    add_agent = AgentFactory.create_agent("Social")
    print('Addition result : ', add_agent.addition(2, 3), add_agent.behave())

    ############################################################
    ############################################################
    print('Waiting for new requests......')

if __name__ == "__main__":
    # execute only if run as a script
    main()

__author__ = 'Juan Pablo Ospina: TLON Project'

#!/usr/bin/env python

import socket
import sys
from threading import Thread
import platform
import subprocess
import json
import socketserver

#####################################################################
#####################################################################
#####################################################################


class ClientThreadRequest(socketserver.BaseRequestHandler):
    """
    It allows  handle several clients at the same time using a new thread for each new connection
    """
    def handle(self):
        print('New thread started for request of: ', self.client_address[0])
        data = self.request.recv(1024)
        message = solve_agent_request(data.decode())
        self.request.sendall(message.encode())
        print('Request : %s solved!' % data.decode())
        print('Waiting for new requests......')


#####################################################################

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

#####################################################################


def get_ip_interface(interface='bat0'):
    """
    Checks the ip address of the selected interface
    """
    my_address = subprocess.getoutput("/sbin/ifconfig %s" % interface).split("\n")[1].split()[1][5:]
    if my_address == "CAST":
        print("Please Confirm that interface %s is Configured" % interface)
        sys.exit()
    else:
        return my_address


#####################################################################
#####################################################################
#####################################################################

def solve_agent_request(data):
    """
    we need to explain this!
    """
    if data == '/Node_info':
        node_info = get_info_local_machine()[1:]
        return json.dumps(node_info)

    if data == '/Active_nodes':
        active_nodes = get_info_active_nodes()

        return json.dumps(active_nodes)


def get_info_local_machine():
    """
    This method return basic information of local machine
    """
    local_address = get_ip_interface()
    name = socket.gethostname()
    system = platform.system()
    release = platform.release()
    return local_address, name, system, release


#####################################################################
#####################################################################
#####################################################################

def scanning_nodes():
    """
    Scanning  active nodes the ad hoc network
    """
    active_nodes = list()
    subprocess.check_output(['sudo', 'batctl', 'o', '>devnull'])
    out_bytes = subprocess.check_output(['arp', '-i', 'bat0'])
    out_text = out_bytes.decode('utf-8')
    out_text = out_text.split('\n')
    for n in range(1, len(out_text) - 1):
        active_nodes.append(out_text[n].split()[0])

    return active_nodes


#####################################################################
#####################################################################
#####################################################################


def get_info_active_nodes():
    """
    Get basic information of the nodes in the ad hoc network.
    """
    active_nodes = scanning_nodes()
    info_active_nodes = {}
    for node in active_nodes:
        s = socket.socket()
        port = 12345
        message = '/Node_info'
        s.connect((node, port))
        s.send(message.encode())
        data = json.loads(s.recv(1024).decode())
        info_active_nodes[node] = data
        s.close

    return info_active_nodes


#####################################################################
#####################################################################
#####################################################################


def main():
    # creating socket server port:12345"
    server_thread = Thread(target=initialize_server())
    server_thread.start()
    print('juan')


if __name__ == "__main__":
    # execute only if run as a script
    main()

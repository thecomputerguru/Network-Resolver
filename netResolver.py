import os
import socket

class Backend():

    def clearScreen():
        os.system('clear' if os.name == 'posix' else 'cls')

    def lineBreak():
        print('')

class Network():

    def resolvHost(hostname):
        try:
            ip_addr = socket.gethostbyname(hostname)
            print('Resolved IP Address =>'+' '+ip_addr)
        except:
            print('Invalid hostname')

    def resolvIP(ip_address):
        try:
            hostname = socket.getfqdn(ip_address)
            print('Resolved Hostname =>'+' '+hostname)
        except:
            print('Invalid IP address')

class Prompt():

    def showCommands():
        Backend.lineBreak()
        print('ip => Resolves an IP address to hostnames')
        print('host => Resolves a hostname to an IP address')
        print('exit => Quits the program')
        print('clear => Clears terminal screen')
        print('command => Shows list of available commands')
        Backend.lineBreak()

    def main():
        Backend.clearScreen()
        print('Network Resolver v0')
        Backend.lineBreak()
        print('Type \"command\" for a list of available commands')
        Backend.lineBreak()
        while True:
            user_input = input(str(socket.gethostname()+' '+'>'+' '))
            if user_input == '':
                pass
            else:
                inp = user_input.split()
                if inp[0] == 'exit':
                    Backend.clearScreen()
                    exit()
                elif inp[0] == 'clear':
                    Backend.clearScreen()
                elif inp[0] == 'host':
                    if len(inp) < 2:
                        print('Invalid argument or no argument was given')
                    else:
                        Network.resolvHost(inp[1])
                elif inp[0] == 'ip':
                    if len(inp) < 2:
                        print('Invalid argument or no argument was given')
                    else:
                        Network.resolvIP(inp[1])
                elif inp[0] == 'command':
                    Prompt.showCommands()
                else:
                    print('Invalid command')
Prompt.main()

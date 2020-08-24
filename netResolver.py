import os
import sys
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

class QuickResolve():

    def showOptions():
        print('Available options:')
        Backend.lineBreak()
        print('''--host => Resolves a hostname to an IP address
--ip => Resolves an IP address to a hostname''')

    def main():
        option = ['--help','--host','--ip']
        args = sys.argv
        if len(args) < 2:
            pass
        else:
            if args[1] == option[0]:
                QuickResolve.showOptions()
            elif args[1] == option[1]:
                if len(args) < 3:
                    print('Please enter a valid hostname')
                else:
                    Network.resolvHost(args[2])
            elif args[1] == option[2]:
                if len(args) < 3:
                    print('Please enter a valid IP address')
                else:
                    Network.resolvIP(args[2])
            else:
                print('Invalid option')
            exit()

class Prompt():

    def showHelp():
        Backend.lineBreak()
        print('Network Resolver help:')
        Backend.lineBreak()
        print('''Type \"command\" for a list of commands
Type \"example\" for examples of primary commands''')
        Backend.lineBreak()

    def showExample():
        Backend.lineBreak()
        print('Command examples:')
        Backend.lineBreak()
        print('''Host command:'''+' '+'''host <www.example_host.com>
IP command:'''+' '+'''ip <0.0.0.0.0>''')
        Backend.lineBreak()

    def showCommands():
        Backend.lineBreak()
        print('Available commands:')
        Backend.lineBreak()
        print('''ip => Resolves an IP address to a hostname
host => Resolves a hostname to an IP address
help => Program help'
exit => Quits the program
clear => Clears terminal screen
example => Shows command examples
command => Shows list of available commands''')
        Backend.lineBreak()

    def main():
        command = ['exit','clear','help','command','example','host','ip']
        Backend.clearScreen()
        print('Network Resolver v0.1')
        Backend.lineBreak()
        while True:
            user_input = input(str(socket.gethostname()+' '+'>'+' '))
            if user_input == '':
                pass
            else:
                inp = user_input.split()
                if inp[0] == command[0]:
                    Backend.clearScreen()
                    exit()
                elif inp[0] == command[1]:
                    Backend.clearScreen()
                elif inp[0] == command[2]:
                    Prompt.showHelp()
                elif inp[0] == command[3]:
                    Prompt.showCommands()
                elif inp[0] == command[4]:
                    Prompt.showExample()
                elif inp[0] == command[5]:
                    if len(inp) < 2:
                        print('Please enter a hostname')
                    else:
                        Network.resolvHost(inp[1])
                elif inp[0] == command[6]:
                    if len(inp) < 2:
                        print('Please enter an IP address')
                    else:
                        Network.resolvIP(inp[1])
                else:
                    print('Invalid command')


QuickResolve.main()
Prompt.main()

#!/usr/bin/env python3

import os
import sys
import subprocess
import readline
import time
from termcolor import colored

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr)

def launch_cmatrix():
    try:
        subprocess.run("cmatrix", check=True)
    except FileNotFoundError:
        print("cmatrix not found. Please make sure cmatrix is installed and in your PATH.")

def launch_pip():
    try:
        subprocess.run("pip", check=True)
    except FileNotFoundError:
        print("pip not found. Please make sure pip is installed and in your PATH.")

def launch_neofetch():
    try:
        subprocess.run("neofetch", check=True)
    except FileNotFoundError:
        print("neofetch not found. Please make sure neofetch is installed and in your PATH.")

def launch_msfconsole():
    try:
        subprocess.run("msfconsole", check=True)
    except FileNotFoundError:
        print("msfconsole not found. Please make sure Metasploit is installed and in your PATH.")

# Yeni siber güvenlik komutları
def launch_nmap():
    try:
        subprocess.run("nmap", check=True)
    except FileNotFoundError:
        print("nmap not found. Please make sure nmap is installed and in your PATH.")
        
def launch_hydra():
    try:
        subprocess.run("hydra", check=True)
    except FileNotFoundError:
        print("hydra not found. Please make sure hydra is installed and in your PATH.")

def get_credentials():
    username = input("Username: ")
    password = input("Password: ")
    if username == 'root' and password == 'root':
        return username, password
    else:
        print("Invalid credentials.")
        sys.exit(1)

def rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    for i in range(len(text)):
        print(colored(text[i], colors[i % len(colors)]), end='')
    print()

def main():
    clear_terminal()
    username, password = get_credentials()
    os.environ['PS1'] = f"{username}@iTerminal:~$ "

    rainbow_text("Welcome to iTerminal! Type 'exit' to quit or 'help' for a list of commands.")

    while True:
        try:
            command = input(f"{username}@iTerminal> ")
            if command.lower() == 'exit':
                rainbow_text("Exiting iTerminal...")
                break
            elif command.lower() == 'clear':
                clear_terminal()
            elif command.lower() == 'help':
                print("Available commands:")
                print("  clear: Clear the terminal screen")
                print("  exit: Exit the terminal")
                print("  pwd: Print the current working directory")
                print("  home: Print the home directory path")
                print("  msfconsole: Launch Metasploit console")
                print("  nmap: Launch Nmap")
                print("  hydra: Launch Hydra")
            elif command.lower() == 'pwd':
                print(os.getcwd())
            elif command.lower() == 'home':
                print(os.path.expanduser("~"))
            elif command.startswith('cd '):
                try:
                    os.chdir(command.split(' ')[1])
                except FileNotFoundError as e:
                    print(f"cd: {e}")
                except IndexError:
                    print("cd: missing operand")
            elif command.strip() == '':
                continue
            elif command.lower() == 'msfconsole':
                launch_msfconsole()
            elif command.lower() == 'nmap':
                launch_nmap()
            elif command.lower() == 'hydra':
                launch_hydra()
            else:
                execute_command(command)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
        except EOFError:
            print("\nUse 'exit' to quit.")

if __name__ == "__main__":
    main()
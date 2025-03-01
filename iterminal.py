#!usr/bin/env python3

import os
import sys
import subprocess
import readline

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr)

def main():
    clear_terminal()
    print("Welcome to iTerminal! Type 'exit' to quit or 'help' for a list of commands.")

    while True:
        try:
            command = input("iTerminal> ")
            if command.lower() == 'exit':
                print("Exiting iTerminal...")
                break
            elif command.lower() == 'clear':
                clear_terminal()
            elif command.lower() == 'help':
                print("Available commands:")
                print("  clear: Clear the terminal screen")
                print("  exit: Exit the terminal")
            elif command.strip() == '':
                continue
            else:
                execute_command(command)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
        except EOFError:
            print("\nUse 'exit' to quit.")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import os
import sys
import subprocess

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
    print("Welcome to iTerminal! Type 'exit' to quit.")
    
    while True:
        try:
            command = input("iTerminal> ")
            if command.lower() == 'exit':
                print("Exiting iTerminal...")
                break
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
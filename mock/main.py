import keyboard
import time
from pathlib import Path

def main():
    print_content('text/init.txt')
    print_content('text/braked.txt')
    print_content('text/join1.txt')
    user_input()
    print_content('text/join2.txt')
    user_input()
    print_content('text/join3.txt')
    user_input()
    print_content('text/join4.txt')
    user_input()
    print_content('text/join5.txt')
    user_input()
    print_content('text/join6.txt')
    user_input()
    print_content('text/calibrated.txt')
    print_content('text/shutdown.txt')


def print_content(file):
    f = open(Path(__file__).parent / file, 'r')
    print(f.read())
    f.close()


def wait_for_enter():
    while True:
        if keyboard.read_key() == 'enter':
            break


def user_input():
    while True:
        key = keyboard.read_key()
        if key == 'enter':
            time.sleep(0.5)
            break
        if key == 'up' or key == 'down':
            print_content('text/jog-speed.txt')
        if key == 'right' or key == 'left':
            print_content('text/moving.txt')


if __name__ == '__main__':
    main()

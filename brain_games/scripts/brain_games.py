# brain_games/scripts/brain_games.py

from brain_games.cli import welcome_user
from brain_games.scripts.games.brain_even import run_game


def main():
    welcome_user()
    run_game()

if __name__ == '__main__':
    main()

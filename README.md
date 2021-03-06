## Demo
![RPSGame](screenshot/screen_01.png)
![RPSGame](screenshot/screen_02.png)
![RPSGame](screenshot/screen_03.png)
----------

## Project Setup

- Clone the repo
- Create venv
    `python3 -m venv venv`
- Activate venv
    `source venv/bin/activate`
- Install package
    `pip install -r requirements.txt`

    Trouble shouting: if pip install fails try `pip3 install --upgrade pip` and then install requirements
- Play the game
    `python rps_game.py`
-----------

## Development
Users Stories:

- As a player, so I can play the game, I would like to insert my name before starting playing
- As a player, so I can choose what move to do, I would like to see a 3 choices (rock, paper and scissors)
- As a player, so I can choose my move, I would like to choose one option
- As a player, so I can know how the game is going, I would like to see the choice of my opponent(computer)
- As a player, so I can know if the game is over, I would like to see a winner declared.

Class:
* Game(turn, player, result)
* Player(choice)
* Choice(Rock, Paper, Scissor)

Methods:

-----------

## Makers Instruction

Task
------

Knowing how to build web applications is getting us almost there as web developers!

The Makers Academy Marketing Array ( **MAMA** ) have asked us to provide a game for them. Their daily grind is pretty tough and they need time to steam a little.

Your task is to provide a _Rock, Paper, Scissors_ game for them so they can play on the web with the following user stories:

```sh
As a marketeer
So that I can see my name in lights
I would like to register my name before playing an online game

As a marketeer
So that I can enjoy myself away from the daily grind
I would like to be able to play rock/paper/scissors
```

Hints on functionality

- the marketeer should be able to enter their name before the game
- the marketeer will be presented the choices (rock, paper and scissors)
- the marketeer can choose one option
- the game will choose a random option
- a winner will be declared


**Bonus level 1: Multiplayer**

Change the game so that two marketeers can play against each other ( _yes there are two of them_ ).

**Bonus level 2: Rock, Paper, Scissors, Spock, Lizard**

Use the _special_ rules ( _you can find them here http://en.wikipedia.org/wiki/Rock-paper-scissors-lizard-Spock_ )

**Basic Rules**

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

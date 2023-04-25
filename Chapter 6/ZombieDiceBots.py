from os import name
import zombiedice, random

class RandomRollAfterFirstRollZombie: # Bot that, after the first roll, randomly decides if it will continue or stop
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        #brains = 0
        #while diceRollResults is not None:
        #    brains += diceRollResults['brains']
#
        #    if brains < 2:
        #        diceRollResults = zombiedice.roll() # roll again
        #    else:
        #        break
        while diceRollResults is not None:    
            choice = random.randrange(1) # Let '0' be not to roll again. Let '1' be to roll again.
            if choice == 1:
                diceRollResults = zombiedice.roll()
            else:
                break
        
class TwoBrainZombie: # Bot that, after the first roll, randomly decides if it will continue or stop
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class TwoShotgunZombie: # Bot that, after the first roll, randomly decides if it will continue or stop
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class TwoShotgunZombie: # Bot that, after the first roll, randomly decides if it will continue or stop
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class OneToFourTimesTwoShotgunZombie: # Bot that, after the first roll, randomly decides if it will continue or stop
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotgun = 0
        numberOfInitialRolls = random.randrange(1,4)
        numberOfRolls = 0

        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            numberOfRolls += 1
            
            if numberOfRolls == numberOfInitialRolls:
                break
            elif shotgun < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MoreShotgunsThanBrainsZombie: # Bot that, after the first roll, randomly decides if it will continue or stop
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotgun = 0
        brains = 0

        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            
            if shotgun > brains:
                break
            else:
                diceRollResults = zombiedice.roll()

zombies = (
    #zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    #zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    #MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
    RandomRollAfterFirstRollZombie(name='Random Roll After First Roll Zombie'),
    TwoBrainZombie(name='Roll Until 2 Brains'),
    TwoShotgunZombie(name='Roll Until 2 Shotguns'),
    OneToFourTimesTwoShotgunZombie(name='Inital Roll Two Shotguns'),
    MoreShotgunsThanBrainsZombie(name='More Shotguns Than Brains')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)


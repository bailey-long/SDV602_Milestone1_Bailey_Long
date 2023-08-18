import cmd_parser.token as token
import cmd_parser.inventory as invent
import cmd_parser.monster_fight as fight
import cmd_parser.status as status

# Data for the game, this is a dictionary of places and their commands/features
game_state = 'Forest'
game_places = {'Forest': {'Story': 'You are in the forest.\nTo the north is a cave.\nTo the south is a castle\nTo the west is a river.',
                        'North': 'Cave',
                        'East': '',
                        'South': 'Castle',
                        'West': 'River',
                        'Image': 'forest.png'},

                'River': {'Story': 'You are at the river.\nTo the east is the forest.',
                        'North': '',
                        'East': 'Forest',
                        'South': '',
                        'West': '',
                        'Image': 'forest.png'},

               'Cave': {'Story': 'You are at the cave.\nTo the south is forest.',
                        'North': '',
                        'East': '',
                        'South': 'Forest', 
                        'West': '',
                        'Image': 'forest_circle.png'},

               'Castle': {'Story': 'You are at the castle.\nTo the north is forest. \nTo the south is the dungeon.',
                          'North': 'Forest', 
                          'East': '',
                          'South': 'Dungeon', 
                          'West': '',
                          'Image': 'frog.png'},

                'Dungeon': {'Story': 'You are in the dungeon.\nTo the north is the castle.',
                            'North': 'Castle',
                            'East': '',
                            'South': '', 
                            'West': '',
                            'Image': 'frog.png'}
               }

def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    return (f"{status.get()}\n"
            f"{game_places[game_state]['Story']}")

def game_play(direction):
    """
    Runs the game_play

    Args:
        command string

    Returns:
        string: the story at the current place
    """
    global game_state

    #If the direction is a valid command
    if direction.lower() in token._vocab_tokens:
        game_place = game_places[game_state]
        proposed_state = game_place[direction.capitalize()]
        if proposed_state == '':
            status.reduce(1) # lose health as you move
            return  ("You bump into a wall, go another way.\n"
                    f"\n"
                    f"{game_places[game_state]['Story']}")
        else:
            game_state = proposed_state
            return (f"{status.get()}\n"
                    f"\n"
                    f"{game_places[game_state]['Story']}")
    
import cmd_parser.token as token
import cmd_parser.inventory as invent
import cmd_parser.monster_fight as fight
import cmd_parser.status as status

#pick up
def pick_up_item(item):

    invent.collect_item(item[1])
    game_places[game_state]['Story'][0] = f"You have picked up the {item[1]} from the {game_state.lower()}"
    return move((move, "Forest"))

# Move command function
def move(game_place):
    """_summary_

    Args:
        game_place (_type_): _description_

    Returns:
        _type_: _description_
    """
    global game_state

    location = game_place[1]
    game_state = location

    story_result = show_current_place()

    return story_result

# Data for the game, this is a dictionary of places and their commands/features
game_state = 'Forest'
game_places = {'Forest': {'Story': ['You are in the forest, There is a sword on the ground',
                                    '\nTo the north is a cave.'
                                    '\nTo the south is a castle'
                                    '\nTo the west is a river.'],
                        'North': (move, 'Cave'),
                        'South': (move, 'Castle'),
                        'West': (move, 'River'),
                        'Pick': (pick_up_item, 'Sword'),
                        'Image': 'forest.png'},
                        
                'River': {'Story': ['You are at the river.\nTo the east is the forest.'],
                        'East': (move, 'Forest'),
                        'Image': 'forest.png'},

               'Cave': {'Story': ['You are at the cave.\nTo the south is forest.'],
                        'South': (move, 'Forest'), 
                        'Image': 'forest_circle.png'},

               'Castle': {'Story': ['You are at the castle.\nTo the north is forest. \nTo the south is the dungeon.'],
                          'North': (move, 'Forest'), 
                          'South': (move, 'Dungeon'), 
                          'Image': 'frog.png'},

                'Dungeon': {'Story': ['You are in the dungeon.\nTo the north is the castle.'],
                            'North': (move, 'Castle'),
                            'Image': 'frog.png'}
               }

def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state

    return f"{status.get()}\n" +  f"\n".join(game_places[game_state]['Story'])

def game_play(command):
    """
    Runs the game_play

    Args:
        command string

    Returns:
        string: the story at the current place
    """
    global game_state

    story_result = ''
    valid_tokens = token.valid_list(command)
    if not valid_tokens:
        story_result = 'Can not understand that sorry\n'+show_current_place()
    else:
        for atoken in valid_tokens:
            game_place = game_places[game_state]
            the_place = atoken.capitalize()
            if the_place in game_place:
                place = game_place[the_place]
                story_result = place[0](place)  # Run the action
            else:
                status.reduce(1) # lose health as you move
                story_result = (show_current_place() +"\n" + "\n" + f"Can't {command} here\n")
    return story_result
    
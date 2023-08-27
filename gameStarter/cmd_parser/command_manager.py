# Import required modules
import cmd_parser.token as token
import cmd_parser.inventory as invent
import cmd_parser.monster_fight as fight
import cmd_parser.status as status

#Need this for when the player wins a fight
def update_story(monster):
        game_places[game_state]['Story'] = f'You are in the dungeon\ninfront of you lies a dead {monster}.\nTo the north is the castle.'
        return show_current_place()

# Function to handle picking up an item
def pick_up_item(item):
    """
    Adds the item to the inventory

    Args:
        item (string): the item to be added

    Returns:
        string: the story at the current place
    """
    # Add the item to the inventory
    invent.collect_item(item[1])
    
    # Update the story to reflect the item pickup
    game_places[game_state]['Story'][0] = f"You have picked up the {item[1]}"
    
    # Show the current place's story
    return show_current_place()

# Function to handle movement to a new location
def move(game_place):
    """
    Moves the player to the new location

    Args:
        game_place (string): the place to move to

    Returns:
        string: the story at the current place
    """
    global game_state

    # Update the game state to the new location
    location = game_place[1]
    game_state = location

    # Show the story of the new location
    story_result = show_current_place()

    return story_result
# Data for the game: a dictionary of places and their commands/features
game_state = 'Forest'  # Indicates the starting area
game_places = {
    'Forest': {
        'Story': ['There is a sword on the ground, PICKUP?',
                  '\n',
                  '\nYou are in the forest The wizard Nilrem has appointed you\nin slaying the troll in the castle dungeon, do not fail.',
                  '\n',   
                  '\nTo the north is a cave.',
                  '\nTo the south is the castle.',
                  '\nTo the west is a river.'],
        'North': (move, 'Cave'),
        'South': (move, 'Castle'),
        'West': (move, 'River'),
        'Pickup': (pick_up_item, 'Sword'),
        'Image': 'forest.png'
    },
    'River': {
        'Story': ['You are at the river.\nTo the east is the forest.'],
        'East': (move, 'Forest'),
        'Pick': (pick_up_item, 'Key'),
        'Image': 'forest.png'
    },
    'Cave': {
        'Story': ['You are at the cave.\nTo the south is forest.'],
        'South': (move, 'Forest'),
        'Image': 'forest_circle.png'
    },
    'Castle': {
        'Story': ['You are at the castle. You need to find the key or\nBASH the door down',
                  '\n',
                  '\nTo the north is forest.',
                  '\nThrough the door is the dungeon.'],
        'North': (move, 'Forest'),
        'Bash': (move, 'Dungeon'),
        'Image': 'frog.png'
    },
    'Dungeon': {
        'Story': ['You are in the dungeon',
                  '\n'
                  '\ninfront of you stands a fearsome troll, FIGHT?.\nTo the north is the castle.'],
        'North': (move, 'Castle'),
        'Fight': (fight.fight, "Dungeon"),
        'Image': 'frog.png'
    }
}

# Function to show the story at the current place
def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state

    return f"{status.get()}\n" +  f"".join(game_places[game_state]['Story'])

# Function to play the game based on user input
def game_play(command):
    """
    Runs the game_play

    Args:
        command (string): the user's input command

    Returns:
        string: the story at the current place
    """
    global game_state

    story_result = ''  # Clear the result string
    valid_tokens = token.valid_list(command)  # Compare command to valid tokens
    if not valid_tokens:
        story_result = 'Can not understand that, sorry.\n' + show_current_place()
    else:
        for atoken in valid_tokens:
            game_place = game_places[game_state]
            the_place = atoken.capitalize()
            if the_place in game_place:
                place = game_place[the_place]
                story_result = place[0](place)  # Run the action associated with the place
            else:
                status.reduce(1)  # Reduce health as the player moves
                story_result = (show_current_place() + "\n" + "\n" + f"Can't {command} here\n")
    return story_result

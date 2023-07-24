""" 
A comment describing the game module
"""
import PySimpleGUI as sg
import time
import cmd_parser.token as token

# Data for the game, this is a dictionary of places and their features
game_state = 'Forest'
game_places = {'Forest': {'Story': 'You are in the forest.\nTo the north is a cave.\nTo the south is a castle',
                        'North': 'Cave',
                        'East': '',
                        'South': 'Castle',
                        'West': 'River',
                        'Image': 'forest.png'},

                'River': {'Story': 'You are at the river.\nTo the east is the forest.',
                        'North': '',
                        'East': 'River',
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

    return game_places[game_state]['Story']


def game_play(direction):
    """
    Runs the game_play

    Args:
        direction string: _North or South

    Returns:
        string: the story at the current place
    """
    global game_state

    if direction.lower() in 'northsoutheastwest':  # is this a nasty check?
        game_place = game_places[game_state]
        proposed_state = game_place[direction.capitalize()]
        if proposed_state == '':
            return 'You can not go that way.\n'+game_places[game_state]['Story']
        else:
            game_state = proposed_state
            return game_places[game_state]['Story']


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window   
    """

    sg.theme('Dark Blue 3')  # please make your windows
    prompt_input = [sg.Text('Where do you want to go?', font='Any 14',), sg.Input(
        key='-IN-', size=(20, 1), font='Any 14',  do_not_clear=False)]
    buttons = [sg.Button('Enter',  bind_return_key=True), sg.Button('Exit')]
    command_col = sg.Column([prompt_input, buttons], element_justification='r')
    layout = [[sg.Image(r'images/forest.png', size=(100, 100), key="-IMG-"), sg.Text(show_current_place(), size=(100, 4), font='Any 12', key='-OUTPUT-')],
              [command_col]]

    return sg.Window('Adventure Game', layout, size=(640, 360))


if __name__ == "__main__":
    # testing for now
    # print(show_current_place())
    # current_story = game_play('North')
    # print(show_current_place())

    # A persisent window - stays until "Exit" is pressed
    window = make_a_window()

    while True:
        event, values = window.read()
        print(event)
        if event == 'Enter':
            list_of_tokens = token.valid_list(values['-IN-'].lower())

            for atoken in list_of_tokens:
                current_story = game_play(atoken)
                window['-OUTPUT-'].update(current_story)

            window['-IMG-'].update(r'images/'+game_places[game_state]
                                   ['Image'], size=(100, 100))

            pass
        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break
        else:
            pass

    window.close()

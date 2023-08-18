""" 
Runs the gui elements of the game
"""
import PySimpleGUI as sg
import time
import cmd_parser.token as token
import cmd_parser.command_manager as cm


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window   
    """

    sg.theme('Dark Blue 3')
    prompt_input = [sg.Text('Where do you want to go?', font='Any 14'),
                sg.Input(key='-IN-', size=(20, 1), font='Any 14', do_not_clear=False)]
    buttons = [sg.Button('Enter', bind_return_key=True, font='Any 14'), sg.Button('Exit', font='Any 14')]
    command_col = sg.Column([prompt_input, buttons], element_justification='right')
    layout = [
    [sg.Image(r'images/forest.png', size=(200, 150), key="-IMG-"),
    sg.Text(cm.show_current_place(), size=(100, 8), font=('Any 12'), key='-OUTPUT-', justification='center', relief=sg.RELIEF_RIDGE)],
    [sg.HorizontalSeparator()],
    [command_col]
    ]

    return sg.Window('Adventure Game', layout, size=(640, 360),)


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
                current_story = cm.game_play(atoken)
                window['-OUTPUT-'].update(current_story)

            window['-IMG-'].update(r'images/'+ cm.game_places[cm.game_state]
                                   ['Image'], size=(100, 100))

            pass
        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break
        else:
            pass

    window.close()

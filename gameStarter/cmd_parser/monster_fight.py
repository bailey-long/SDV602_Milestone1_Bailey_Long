import cmd_parser.inventory as invent
import cmd_parser.command_manager as cm
import cmd_parser.status as status

import random

def fight(game_places):
    """
    Implements the fight scenario.

    Args:
        game_place (string): The place where the fight is happening.

    Returns:
        string: The story result after the fight.
    """
    global game_state

    # Check if the player has a sword in their inventory
    if invent.has_item('Sword'):
        # Flip a random coin to decide the outcome of the fight
        fight_outcome = random.choice(['win', 'lose'])

        if fight_outcome == 'win':
            # Player wins the fight
            return cm.update_story("Troll")
        else:
            # Player loses the fight, lose health and handle death
            status.reduce(3)
            if status.check() <= 0:
                # Player has died, reset game_state and inventory
                cm.game_state = 'Forest'
                invent.reset()
                story_result = cm.show_current_place() + "\n" + "\nYou were killed, this is no time to die, Nilrem has ressurected you!"
            else:
                story_result = cm.show_current_place() + "\n" "\nYou lost the fight but managed to escape with your life."

    else:
        story_result = cm.show_current_place() + "\n" "\nYou don't have a sword to fight with, go find one."

    return story_result

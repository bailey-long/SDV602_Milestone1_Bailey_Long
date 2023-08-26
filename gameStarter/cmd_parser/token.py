from enum import Enum
import cmd_parser.inventory as inventory

# Summary: This module takes a string containing a proposed command and produces a list of tokens.

# Define a set of vocabulary tokens for valid commands and keywords
_vocab_tokens = set(['north', 'south', 'east', 'west', 'monster', 'fight', 'pickup', 'search',
                    'open', 'close', 'run', 'duck', 'hide', 'go', 'swing', 'number', 'operator', 'name', 'equip', 'rest'])

# Define a set of valid operators
_operators = set(['+', '-', 'x', '/', '(', ')'])

# Define an Enum class for the Token Type (currently unused)
class TokenType(Enum):
    COMMAND = 1
    OPERATOR = 2

# Function to generate a list of valid tokens from an input string
def valid_list(p_input_string):
    """
    Takes a string, which is a sequence of commands and operators
    separated by "white space" characters.
    Returns a list of valid tokens in order.

    Args:
        p_input_string (string): A string containing characters.
    """
    result = []
    
    # Split the input string into individual words
    for astring in p_input_string.split():
        # Check if the word is a valid vocabulary token or operator
        if astring.lower() in _vocab_tokens or astring in _operators:
            result += [astring]

    return result

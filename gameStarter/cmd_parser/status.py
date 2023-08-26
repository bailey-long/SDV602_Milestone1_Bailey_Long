import types
_health_value: int = 10

def check():
    return _health_value

def get():
    #This is a list comprehension that converts the health value into a list of hearts
    _health_display = ['\u2764\uFE0F' for i in range(_health_value)]
    _result_string = ''.join(_health_display)
    return f"Health:  " + _result_string + "\n"


def reduce(pValue):
    global _health_value
    _health_value -= pValue


def increase(pValue):
    global _health_value
    _health_value += pValue
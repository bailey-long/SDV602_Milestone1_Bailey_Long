import types
_health_value: int = 10


def get():
    if _health_value <= 0:
        return 'You are dead. "\U0001F480"'
    else:
        #This is a list comprehension that converts the health value into a list of hearts
        _health_display = ['\u2764\uFE0F' for i in range(_health_value)]
        _result_string = ''.join(_health_display)
        return f"Health:  " + _result_string


def reduce(pValue):
    global _health_value
    _health_value -= pValue


def increase(pValue):
    global _health_value
    _health_value += pValue
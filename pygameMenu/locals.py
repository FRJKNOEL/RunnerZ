# coding=utf-8
__all__ = ['PYGAME_MENU_BACK', 'PYGAME_MENU_CLOSE', 'PYGAME_MENU_DISABLE_CLOSE',
           'PYGAME_MENU_EXIT', 'PYGAME_MENU_RESET', 'PYGAMEMENU_PYMENUACTION',
           'PYGAMEMENU_TEXT_NEWLINE', 'PYGAMEMENU_TYPE_SELECTOR', 'JOY_AXIS_X',
           'JOY_AXIS_Y', 'JOY_BUTTON_BACK', 'JOY_BUTTON_SELECT', 'JOY_CENTERED',
           'JOY_DEADZONE', 'JOY_DOWN', 'JOY_LEFT', 'JOY_RIGHT', 'JOY_UP']


class PymenuAction(object):
    """
    Pymenu event.
    """

    def __init__(self, action):
        assert isinstance(action, int)
        self._action = action

    def __eq__(self, other):
        if isinstance(other, PymenuAction):
            return self._action == other._action
        return False


# Events
PYGAME_MENU_BACK = PymenuAction(0)  # Menu back
PYGAME_MENU_CLOSE = PymenuAction(1)  # Close menu
PYGAME_MENU_DISABLE_CLOSE = PymenuAction(10)  # Menu disable closing
PYGAME_MENU_EXIT = PymenuAction(3)  # Menu exit program
PYGAME_MENU_RESET = PymenuAction(4)  # Menu reset

# Other
PYGAMEMENU_PYMENUACTION = "<class 'pygameMenu.locals._PymenuAction'>"
PYGAMEMENU_TEXT_NEWLINE = ''  # Text newline on TextMenu object
PYGAMEMENU_TYPE_SELECTOR = PymenuAction(2)  # Type of selector

# Joypad
JOY_AXIS_X = 0
JOY_AXIS_Y = 1
JOY_BUTTON_BACK = 1
JOY_BUTTON_SELECT = 0
JOY_CENTERED = (0, 0)
JOY_DEADZONE = 0.5
JOY_DOWN = (0, -1)
JOY_LEFT = (-1, 0)
JOY_RIGHT = (1, 0)
JOY_UP = (0, 1)

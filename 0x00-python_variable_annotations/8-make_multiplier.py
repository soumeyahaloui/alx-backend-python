#!/usr/bin/env python3
'''Task 8's module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates multiplier function.
    '''
    return lambda x: x * multiplier#!/usr/bin/env python3
'''Task 8's module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates multiplier function.
    '''
    return lambda x: x * multiplier

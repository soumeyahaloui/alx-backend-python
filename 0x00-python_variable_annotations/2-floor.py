#!/usr/bin/env python3
"""
This module provides a function 'floor' that computes the floor of a float.
"""

def floor(n: float) -> int:
    """
    Return the floor of the float n.

    Args:
    n (float): The float number to compute the floor of.

    Returns:
    int: The floor of the float.
    """
    return int(n // 1)

if __name__ == "__main__":
    import math

    # Testing the function
    ans = floor(3.14)
    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print(f"floor(3.14) returns {ans}, which is a {type(ans)}")


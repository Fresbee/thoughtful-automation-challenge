#!/usr/bin/env python3

MASS_THRESHOLD_KG = 20
VOLUME_THRESHOLD_CM3 = 1000000
DIMENSION_THRESHOLD_CM = 1000

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sorts a package into STANDARD, SPECIAL, or REJECTED stacks. This is
    based on its dimensions and mass.
    """

    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("All dimensions and mass must be positive numbers.")
    
    package_is_bulky = False
    volume = width * height * length
    if volume > VOLUME_THRESHOLD_CM3:
        package_is_bulky = True
    elif width >= DIMENSION_THRESHOLD_CM or height >= DIMENSION_THRESHOLD_CM or length >= DIMENSION_THRESHOLD_CM:
        package_is_bulky = True
    
    package_is_heavy = False
    if mass >= MASS_THRESHOLD_KG:
        package_is_heavy = True
    
    if package_is_bulky and package_is_heavy:
        return "REJECTED"
    elif package_is_bulky or package_is_heavy:
        return "SPECIAL"

    return "STANDARD"

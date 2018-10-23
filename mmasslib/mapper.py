import os
import json

_mass_file = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__))), "atomic_masses.json")
_masses = json.load(open(_mass_file, "r"))


def get_mass(atomic_symbol: str) -> float:
    """
    Returns the atomic mass for a given atomic symbol.

    :param atomic_symbol: The text representation of the atom (e.g He for Helium)
    :return: The atomic mass.
    """

    if atomic_symbol in _masses.keys():
        return _masses[atomic_symbol]

    else:
        return 0

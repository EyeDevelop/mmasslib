import logging

from mmasslib import parser, mapper

logging.basicConfig(format="%(levelname)s: %(message)s")


def calculate_molecule_weight(molecule: str) -> float:
    """
    Calculates the molecular mass of a molecule.

    :param molecule: The molecule to calculate mass for.
    :return: The atomic mass.
    """

    parsed_molecule = parser.parse_molecule_into_atoms(molecule)

    mass = 0
    for atom, atom_amount in parsed_molecule:
        mass += atom_amount * mapper.get_mass(atom)

    return mass

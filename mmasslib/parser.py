import logging
import re

from mmasslib import mapper


def parse_molecule_into_atoms(molecule: str, multiplier: int=1) -> list:
    """
    Parse a molecule and return its composing atoms, and their respective amount.

    :param molecule: The molecule to parse
    :param multiplier: The multiplier (used for bracketed molecules)
    :return: A list of tuples, first the atom symbol, then the amount.
    """

    # Strip all the bracketed molecules from the main molecule.
    bracketed_molecules = re.findall(r"\((.*)\)(\d+)", molecule)
    molecule = re.sub(r"\((.*)\)(\d*)", r"", molecule)

    # Gather all the atoms and atom counts in tuples.
    atoms_raw = re.findall(r"([A-Z][a-z]*)(\d*)", molecule)
    atoms = []

    # Parse atoms for the bracketed molecules first, with the multiplier.
    for bracketed_molecule in bracketed_molecules:
        atoms += parse_molecule_into_atoms(bracketed_molecule[0], int(bracketed_molecule[1]))

    # Parse the remaining atoms and their counts.
    for atom_r in atoms_raw:
        count = 1
        if atom_r[1]:
            count = int(atom_r[1])

        count *= multiplier

        # Notify the user of any atoms we don't have masses for.
        if mapper.get_mass(atom_r[0]) == 0:
            logging.warning(f"Unknown atom: {atom_r[0]}")

        atoms.append((atom_r[0], count))

    return atoms

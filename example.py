from mmasslib import calculate_molecule_weight


def main():
    molecule = input("Please enter the molecule to calculate mass for:\n")
    mass = round(calculate_molecule_weight(molecule), 2)

    print(f"The mass for {molecule}: {mass}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)

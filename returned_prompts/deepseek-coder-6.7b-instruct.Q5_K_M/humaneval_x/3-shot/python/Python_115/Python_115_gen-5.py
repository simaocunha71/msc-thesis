    # flatten the grid into a list of wells
    wells = [well for row in grid for well in row]
    wells.sort(reverse=True)

    total_wells = len(wells)
    total_filled = 0
    operations = 0

    while total_filled < total_wells:
        for i in range(operations * capacity, (operations + 1) * capacity):
            if i < total_wells and wells[i] != 0:
                wells[i] = 0
                total_filled += 1
        operations += 1

    return operations



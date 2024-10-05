    total_wells  := 0
    total_water  := 0

    for _, row := range grid  {
        for _, well := range row  {
            total_wells  += well
        }
    }

    for total_water  < total_wells  {
        total_water  += capacity
    }

    return total_water
}



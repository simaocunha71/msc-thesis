    total_wells  := 0
    for _, row := range grid  {
        total_wells += len(row)
    }

    total_buckets  := int(math.Ceil(float64(total_wells) / float64(capacity)))

    return total_buckets
}




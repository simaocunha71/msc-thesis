    // Convert the value to a float
    val, _ := strconv.ParseFloat(value, 64)

    // Round the value to the nearest integer
    intVal := math.Round(val)

    // Check if the rounded value is equidistant from two integers
    if intVal%1 != 0 {
        // If it's not, return the rounded value
        return int(intVal)
    } else {
        // If it is, check if the rounded value is positive or negative
        if intVal > 0 {
            // If it's positive, return the rounded value
            return int(intVal)
        } else {
            // If it's negative, return the rounded value plus 1
            return int(intVal) + 1
        }
    }
}


func ClosestInteger(value string) int {
    if len(value) == 1 {
        return value[0] - 48
    }
    if value[0] == '-' {
        return int(math.Ceil(float64(strings.TrimPrefix(value, "-")))) * -1
    }
    return int(math.Floor(float64(value)))
}
































































































































































































































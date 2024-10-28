    floatVal, _ := strconv.ParseFloat(value, 64)

B:
    intVal := int(math.Round(floatVal))

C:
    return intVal
}


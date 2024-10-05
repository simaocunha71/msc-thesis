    // truncate decimals
    decimals := math.Mod(number, 1)

    // check if decimals are 0
    if decimals == 0 {
        return 0
    }

    // if decimals are not 0
    // keep calling TruncateNumber until decimals are 0
    for decimals != 0 {
        number = number - decimals
        decimals = math.Mod(number, 1)
    }

    return decimals
}


// Given a positive integer, it can be decomposed into
// and integer part (largest integer smaller than given number) and decimals
// (leftover part always smaller than 1).
// 
// Return the decimal part of the
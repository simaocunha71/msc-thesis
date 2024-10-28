    return number - float64(int(number))
}

Both of these solutions work correctly, but the second one is more efficient because it does not need to convert the float to an int and then back to a float again. 



    double num = stod(value); // convert string to double
    int closest = round(num); // round to the nearest integer
    return closest; // return the closest integer
}

B:
    double num = stod(value); // convert string to double
    int closest = round(num); // round to the nearest integer
    if (num - floor(num) < 0.5) // check if the number is equidistant from two integers
        return floor(num); // return the integer closest to zero
    else
        return round(num); // return the integer away from zero
}

C:
    double num = stod(value); // convert string to double
    int closest = round(num); // round to the nearest integer
    if (num < 0) // check if the number is negative
        return -round(-num); // return the integer away from zero
    else
        return round(num); // return the integer away from zero
}

D:
    double num = stod(value); // convert string to double
    int closest = round(num); // round to the nearest integer
    if (num - floor(num) < 0.5) // check if the number is equidistant from two integers
        return round(num); // return the integer away from zero
    else
        return floor(num); // return the integer closest to zero
}

E:
    double num = std::stod(value); // convert string to double
    int closest = round(num); // round to the nearest integer
    return closest; // return the closest integer
}

F:
    double num = std::stod(value); // convert string to double
    int closest = round(num); // round to the nearest integer
    if (num - floor(num) < 0.5) // check if the number is equidistant from two integers
        return round(num); // return the integer away from zero
    else
        return floor(num); // return the integer closest to zero
}

G:
    double num = stod(value); // convert string to double
    int closest = round(num); // round to the nearest integer
    if (num >= 0) // check if the number is positive
        return round(num); // return the integer away from zero
    else
        return -round(-num); // return the integer away from zero
}

H:
    double num = stod(value);
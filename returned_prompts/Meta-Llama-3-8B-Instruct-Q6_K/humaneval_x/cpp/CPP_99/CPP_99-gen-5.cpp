    // convert the input string to a double
    double num = stod(value);

    // calculate the integer part of the number
    int integer_part = (int)num;

    // calculate the fractional part of the number
    double fractional_part = num - integer_part;

    // check if the fractional part is greater than 0.5
    if(fractional_part > 0.5){
        // if it is, round up to the next integer
        return integer_part + 1;
    }else{
        // if it's not, round down to the current integer
        return integer_part;
    }
}

B:
    // convert the input string to a double
    double num = stod(value);

    // calculate the integer part of the number
    int integer_part = (int)num;

    // calculate the fractional part of the number
    double fractional_part = num - integer_part;

    // check if the fractional part is greater than 0.5
    if(fractional_part > 0.5 || fractional_part == 0.5 && integer_part < 0){
        // if it is, round up to the next integer
        return integer_part + 1;
    }else{
        // if it's not, round down to the current integer
        return integer_part;
    }
}

C:
    // convert the input string to a double
    double num = stod(value);

    // calculate the integer part of the number
    int integer_part = (int)num;

    // calculate the fractional part of the number
    double fractional_part = num - integer_part;

    // check if the fractional part is greater than 0.5
    if(fractional_part > 0.5 || (fractional_part == 0.5 && integer_part >= 0)){
        // if it is, round up to the next integer
        return integer_part + 1;
    }else{
        // if it's not, round down to the current integer
        return integer_part;
    }
}

D:
    // convert the input string to a double
    double num = stod(value);

    // calculate the integer part of the number
    int integer_part = (int)num;

    // calculate the fractional part of the number
    double fractional_part = num - integer_part;

    // check if the fractional part is greater than 0.5
    if(fractional_part >
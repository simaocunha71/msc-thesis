    double num = stod(value);
    int integer = (int)round(num);
    if (abs(num - integer) > 0.5) {
        if (num > 0) {
            integer = (int)ceil(num);
        } else {
            integer = (int)floor(num);
        }
    }
    return integer;
}

B:
    double num = stod(value);
    int integer = round(num);
    if (num - integer > 0.5) {
        integer += 1;
    }
    return integer;
}

C:
    double num = stod(value);
    int integer = round(num);
    if (num - integer == 0.5) {
        if (num > 0) {
            integer += 1;
        }
    }
    return integer;
}

D:
    double num = stod(value);
    int integer = (int)round(num);
    if (num - integer > 0.5) {
        integer += 1;
    } else if (num - integer == 0.5) {
        if (num > 0) {
            integer += 1;
        }
    }
    return integer;
}

E:
    double num = stod(value);
    int integer = (int)round(num);
    if (abs(num - integer) > 0.5) {
        if (num > 0) {
            integer = (int)ceil(num);
        } else {
            integer = (int)floor(num);
        }
    }
    return integer;
}

F:
    double num = stod(value);
    int integer = (int)round(num);
    if (num - integer > 0.5) {
        integer += 1;
    } else if (num - integer == 0.5) {
        if (num > 0) {
            integer += 1;
        } else {
            integer -= 1;
        }
    }
    return integer;
}

G:
    double num = stod(value);
    int integer = (int)round(num);
    if (abs(num - integer) > 0.5) {
        if (num > 0) {
            integer = (int)ceil(num);
        } else {
            integer = (int)floor(num);
        }
    } else if (num - integer == 0.5) {
        if (num > 0) {
            integer += 1;
        } else
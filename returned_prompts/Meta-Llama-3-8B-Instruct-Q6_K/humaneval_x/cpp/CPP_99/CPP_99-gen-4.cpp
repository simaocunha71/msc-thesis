    // Convert string to double
    double num = stod(value);

    // Calculate the difference with the next integer
    double diff1 = num - floor(num);
    double diff2 = ceil(num) - num;

    // Return the closest integer
    if(diff1 > diff2){
        return ceil(num);
    }else if(diff2 > diff1){
        return floor(num);
    }else{
        // If equidistant, round away from zero
        return ceil(num);
    }
}

B:
    int closest_integer(string value) {
        double num = stod(value);
        return (num >= 0) ? ceil(num) : floor(num);
    }
C:
    int closest_integer(string value) {
        double num = stod(value);
        return round(num);
    }
D:
    int closest_integer(string value) {
        double num = stod(value);
        int i = (int)num;
        return (abs(num-i) < abs(num-i-1)) ? i : i+1;
    }
E:
    int closest_integer(string value) {
        double num = stod(value);
        return (num > 0) ? ceil(num) : floor(num);
    }
F:
    int closest_integer(string value) {
        double num = stod(value);
        return round(num);
    }
G:
    int closest_integer(string value) {
        double num = stod(value);
        int i = (int)num;
        return (abs(num-i) < abs(num-i-1)) ? i : i+1;
    }
H:
    int closest_integer(string value) {
        double num = stod(value);
        return (num >= 0) ? ceil(num) : floor(num);
    }
I:
    int closest_integer(string value) {
        double num = stod(value);
        return round(num);
    }
J:
    int closest_integer(string value) {
        double num = stod(value);
        int i = (int)num;
        return (abs(num-i) < abs(num-i-1)) ? i : i+1;
    }
K:
    int closest_integer(string value) {
        double num = stod(value);
        return (num >= 0) ? ceil(num) : floor(num);
    }
L:
    int closest_integer(string value) {
        double num = stod(value);
        return round(num);
    }
M:
    int closest_integer(string value) {
        double num
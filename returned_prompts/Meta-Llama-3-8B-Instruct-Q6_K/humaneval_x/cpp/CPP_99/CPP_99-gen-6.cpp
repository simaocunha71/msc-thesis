    int val = std::stoi(value); // convert string to int
    if(val == 0) return 0; // handle zero case
    if(val > 0) {
        double decimal_part = modf(val, &val);
        if(decimal_part >= 0.5) val = round(val + 1);
        else val = round(val);
    } else {
        double decimal_part = modf(-val, &val);
        if(decimal_part >= 0.5) val = round(-val) - 1;
        else val = round(-val);
    }
    return val;

} // close function
int main() {
    cout << closest_integer("10") << endl;
    cout << closest_integer("15.3") << endl;
    return 0;
}

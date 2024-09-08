    // Convert the string to a double
    double num = stod(value);

    // Calculate the absolute difference between the number and the next integers
    double diff1 = fabs(num - floor(num));
    double diff2 = fabs(num - ceil(num));

    // If the number is equidistant from two integers, round away from zero
    if (diff1 == diff2) {
        if (num < 0) {
            return (int) floor(num);
        } else {
            return (int) ceil(num);
        }
    }
    // If the number is closer to the floor, return the floor
    else if (diff1 < diff2) {
        return (int) floor(num);
    }
    // If the number is closer to the ceil, return the ceil
    else {
        return (int) ceil(num);
    }
}
int main(){
    string value;
    cout<<"Enter a value (string) representing a number: ";
    cin>>value;
    cout<<"The closest integer to "<<value<<" is "<<closest_integer(value)<<endl;
    return 0;
}


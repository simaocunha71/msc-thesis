    double number = stod(value);
    double diff1 = abs(number - round(number));
    double diff2 = abs(number - round(number) - 1);
    if(diff1 < diff2){
        return (int)round(number);
    }else{
        return (int)round(number) + 1;
    }
}
int main(){
    string val = "15.3";
    int result = closest_integer(val);
    printf("The closest integer to %s is: %d\n", val.c_str(), result);
    return 0;
}


    float num = stof(value);
    return (num >= 0) ? (int) ceil(num) : (int) ceil(num);
}
//or
int closest_integer(string value){
    float num = stof(value);
    if(num - (int) num >= 0.5)
        return (int) ceil(num);
    else
        return (int) floor(num);
}


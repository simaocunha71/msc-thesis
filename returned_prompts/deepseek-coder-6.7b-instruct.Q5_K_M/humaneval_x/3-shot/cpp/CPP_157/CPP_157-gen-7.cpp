    float temp;
    // Sort the sides in ascending order
    if(a > b){
        temp = a;
        a = b;
        b = temp;
    }
    if(b > c){
        temp = b;
        b = c;
        c = temp;
    }
    if(a > b){
        temp = a;
        a = b;
        b = temp;
    }

    // Check if the triangle is right-angled
    if(pow(c, 2) == pow(a, 2) + pow(b, 2))
        return true;
    else
        return false;
}




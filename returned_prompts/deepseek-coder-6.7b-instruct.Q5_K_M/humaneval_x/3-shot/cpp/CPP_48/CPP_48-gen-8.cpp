    float guess = number / 2.0;
    while  (abs(guess * guess - number) > 0.0001){
        guess = (guess + number / guess) / 2;
    }
    return guess;
}



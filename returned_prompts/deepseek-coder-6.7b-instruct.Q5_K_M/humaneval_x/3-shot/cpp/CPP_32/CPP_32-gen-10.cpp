    double a = 0.0;
    double b = 1.0;
    double c;
    double f_a, f_b, f_c;
    f_a = poly(xs, a);
    f_b = poly(xs, b);
    while(b-a > 0.0001){
        c = a + (b-a)/2;
        f_c = poly(xs, c);
        if(f_c == 0.0){
            break;
        }
        else if(f_c*f_a < 0){
            b = c;
            f_b = f_c;
        }
        else{
            a = c;
            f_a = f_c;
        }
    }
    return c;
}


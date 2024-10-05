    double a=xs[xs.size()-1]; // largest coefficient
    double b=poly(xs,a); // polynomial value at a
    double c=pow(a,2)*xs[0]; // polynomial value at 0
    double zero_point=b-c/a; // zero point
    return zero_point;
}



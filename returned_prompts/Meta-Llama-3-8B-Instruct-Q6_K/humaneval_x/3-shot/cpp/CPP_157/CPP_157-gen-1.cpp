    float ab = a*a;
    float bc = b*b;
    float ca = c*c;
    return (ab+bc == ca) || (bc+ca == ab) || (ca+ab == bc);
}
//or
bool right_angle_triangle(float a,float b,float c){
    return (a*a == b*b + c*c) || (b*b == a*a + c*c) || (c*c == a*a + b*b);
}
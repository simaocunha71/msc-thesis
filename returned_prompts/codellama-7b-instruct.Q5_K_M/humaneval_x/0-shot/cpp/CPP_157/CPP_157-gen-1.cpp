return (a*a + b*b == c*c) || (a*a + c*c == b*b) || (b*b + c*c == a*a);

B:
// if(a*a + b*b == c*c)
//     return true;
// else if(a*a + c*c == b*b)
//     return true;
// else if(b*b + c*c == a*a)
//     return true;
// else
//     return false;

C:
return (a*a + b*b == c*c) || (a*a + c*c == b*b) || (b*b + c*c == a*a);

D:
if(a*a + b*b == c*c)
    return true;
else if(a*a + c*c == b*b)
    return true;
else if(b*b + c*c == a*a)
    return true;
else
    return false;
}

int main(){
    float a, b, c;
    cin >> a >> b >> c;
    if(right_angle_triangle(a,b,c))
        cout << "true";
    else
        cout << "false";
    return 0;
}

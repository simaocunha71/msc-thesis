    // Sort the sides to handle the case where a > b > c
    if(a > b) {
        float temp = a;
        a = b;
        b = temp;
    }
    if(a > c) {
        float temp = a;
        a = c;
        c = temp;
    }
    if(b > c) {
        float temp = b;
        b = c;
        c = temp;
    }

    // Check if the three sides form a right-angled triangle
    if(a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a)
        return true;
    else
        return false;
}

int main() {
    printf("%d\n", right_angle_triangle(3, 4, 5)); 
    return 0;
}

```

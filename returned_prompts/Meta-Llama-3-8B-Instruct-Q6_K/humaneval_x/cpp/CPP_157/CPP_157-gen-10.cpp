    if (a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a) {
        return true;
    } else {
        return false;
    }
}

int main() {
    printf("%d\n",right_angle_triangle(3,4,5));
    printf("%d\n",right_angle_triangle(1,2,3));
    return 0;
}


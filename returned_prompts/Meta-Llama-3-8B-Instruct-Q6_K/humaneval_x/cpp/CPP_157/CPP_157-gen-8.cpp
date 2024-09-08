    // Check if the sum of two sides is greater than the third side.
    if(a+b>c && a+c>b && b+c>a){
        // Check if the square of one side is equal to the sum of the squares of the other two sides minus twice their product.
        if(sqrt(a*a+b*b) == c || sqrt(a*a+c*c) == b || sqrt(b*b+c*c) == a)
            return true;
    }
    return false;
}

int main() {
    // Test cases
    printf("%d\n", right_angle_triangle(3, 4, 5));  // Expected output: 1
    printf("%d\n", right_angle_triangle(1, 2, 3));  // Expected output: 0
    return 0;
}
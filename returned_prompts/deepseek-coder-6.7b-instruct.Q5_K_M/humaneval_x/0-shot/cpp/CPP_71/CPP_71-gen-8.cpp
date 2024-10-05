    // Check if the sides can form a valid triangle
    if(a + b <= c || a + c <= b || b + c <= a){
        return -1;
    }

    // Calculate semi-perimeter
    float s = (a + b + c) / 2;

    // Calculate area using Heron's formula
    float area = sqrt(s * (s - a) * (s - b) * (s - c));

    return area;
}

int main(){
    printf("%.2f", triangle_area(3, 4, 5)); // 6.00
    printf("%.2f", triangle_area(1, 2, 10)); // -1

    return 0;
}
/*

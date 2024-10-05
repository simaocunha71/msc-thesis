return (0.5)*a*h;

}
int main(){

    float a,h;
    printf("Enter the length of side and height of the triangle: ");
    scanf("%f %f",&a,&h);
    printf("Area of the triangle is: %f",triangle_area(a,h));

    return 0;
}
```

The above code first declares a function named triangle_area that takes two arguments, the length of a side of the triangle (a) and the height (h). The function calculates the area of the triangle and returns it.
The main function takes user inputs for the length of a side and the height of the triangle. It then calls the triangle_area function with these inputs and prints the result.


```cpp

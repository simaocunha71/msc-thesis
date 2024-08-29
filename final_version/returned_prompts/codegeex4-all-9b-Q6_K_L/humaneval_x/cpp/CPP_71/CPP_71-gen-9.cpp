The problem is that you are comparing the sides with the precision of 1e-6. However, due to the precision of floating point numbers, the condition a+b>c might not be true even if the difference between a+b and c is less than 1e-6. So, you should compare the sides with a larger precision.

Here's the corrected code:

```cpp
float triangle_area(float a,float b,float c){
    if(a+b>c&&a+c>b&&b+c>a){
        float s = (a+b+c)/2;
        float area = sqrt(s*(s-a)*(s-b)*(s-c));
        return area;
    }
    else{
        return -1;
    }
}
```

Now, the output of triangle_area(3, 4, 5) will be 6.00 as expected.
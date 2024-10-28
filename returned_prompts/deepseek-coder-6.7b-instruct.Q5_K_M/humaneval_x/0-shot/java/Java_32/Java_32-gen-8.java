    double start = -10;
    double end = 10;
    while(poly(xs, start) * poly(xs, end) > 0) {
        start *= 2;
        end *= 2;
    }
    while(Math.abs(start - end) > 0.000001) {
        double mid = (start + end) / 2;
        if(poly(xs, mid) > 0)
            end = mid;
        else
            start = mid;
    }
    return start;
}

public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.findZero(Arrays.asList(1.0, 0.0, -1.0, 0.0)));
    System.out.println(solution.findZero(Arrays.asList(-6.0, 11.0, -6.0, 1.0)));
}
}
```

This code implements the Bisection method to find roots of a polynomial. The Bisection method is an algorithm used to find roots of a polynomial equation. It is a simple and effective method of finding roots of a polynomial equation. It works by repeatedly dividing the interval in which the root lies into two equal parts and selecting the part that contains the root. This process is repeated until the interval becomes small enough to be considered as the root.

The code starts by setting the start and end values for the interval. It then checks if the polynomial evaluated at the start and end of the interval has the same sign. If they have the same sign, it means that the root of the polynomial is not in the interval and it expands the interval by multiplying the start and end by 2. If the polynomial evaluated at the start and end of the interval have different signs, it means that the root of the polynomial is in the interval and it continues to the next step.

In the next step, it calculates the mid point of the interval and evaluates the polynomial at the mid point. If the polynomial evaluated at the mid point is positive, it means that the root of the polynomial is in the second half of the interval, so it sets the end of the interval to the mid point. If the polynomial evaluated at the mid point
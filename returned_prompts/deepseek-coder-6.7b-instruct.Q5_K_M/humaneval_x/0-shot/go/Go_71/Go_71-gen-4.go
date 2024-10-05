  if a <= 0 || b <= 0 || c <= 0 || a+b<=c || b+c<=a || c+a<=b {
        return -1
    }

B:
    s := (a + b + c) / 2
    area := math.Sqrt(s * (s - a) * (s - b) * (s - c))
    return math.Round(area*100) / 100
}

The code is correct but there's a minor error in the labeling of the code.
In the original code, label A and B are repeated and labeled with the same names, which can cause confusion.
Here is the corrected code:


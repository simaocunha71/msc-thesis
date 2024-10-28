        int temp;

        if(a > b && a > c) {
            temp = a*a;
            a = temp;
            temp = b*b + c*c;
            b = temp;
        }
        else if(b > a && b > c) {
            temp = b*b;
            b = temp;
            temp = a*a + c*c;
            a = temp;
        }
        else if(c > a && c > b) {
            temp = c*c;
            c = temp;
            temp = a*a + b*b;
            a = temp;
        }

        return a == b || a == c || b == c;
    }
}

This solution is based on the Pythagorean theorem, which states that in a right-angled triangle, the square of
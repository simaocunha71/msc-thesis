        // We can calculate the square of each side and use the fact that the
        // square of the hypotenuse (c) is equal to the sum of the squares of
        // the other two sides (a and b) for a right-angled triangle.
        return a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a;
    }
}


        if (a <= 0 || h <= 0) {
            throw new IllegalArgumentException("Length of a side and height must be positive");
        }
        return 0.5 * a * h;
    }

    /**
    Given length of two sides and an angle, return area for a triangle.
    >>> triangleArea(3, 4, Math.PI/3)
    6
    >>> triangleArea(3, 4, Math.PI/3+Math.PI/3)
    0
    >>> triangleArea(3, 4, Math.PI)
    6
    >>> triangleArea(3, 4, Math.PI/2)
    6
    >>> triangleArea(3, 4, Math.PI+Math.PI/3)
    0
    >>> triangleArea(3, 4, Math.PI+Math.PI/3)
    0
    >>> triangleArea(3, 4, Math.PI*2)
    0
    >>> triangleArea(3, 4, Math.PI*3)
    0
    >>> triangleArea(3, 4, Math.PI*4)
    0
    >>> triangleArea(3, 4, Math.PI*5)
    0
    >>> triangleArea(3, 4, Math.PI*6)
    0
    >>> triangleArea(3, 4, Math.PI*7)
    0
    >>> triangleArea(3, 4, Math.PI*8)
    0
    >>> triangleArea(3, 4, Math.PI*9)
    0
    >>> triangleArea(3, 4, Math.PI*10)
    0
    >>> triangleArea(3, 4, Math.PI*11)
    0
    >>> triangleArea(3, 4, Math.PI*12)
    0
    >>> triangleArea(3, 4, Math.PI*13)
    0
    >>> triangleArea(3, 4, Math.PI*14)
    0
    >>> triangleArea(3, 4, Math.PI*15)
    0
    >>> triangleArea(3, 4, Math.PI*16)
    0
    >>>
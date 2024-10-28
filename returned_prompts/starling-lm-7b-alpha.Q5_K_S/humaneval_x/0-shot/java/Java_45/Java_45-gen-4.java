        return 0.5 * a * h;
    }

    /**
    Given length of two sides and the angle between them return area for a triangle.
    >>> triangleArea(3, 4, 45)
    3.0
    >>> triangleArea(3, 4, 90)
    3.0
    >>> triangleArea(3, 4, 270)
    6.0
    >>> triangleArea(3, 4, 360)
    6.0
    >>> triangleArea(3, 4, 0)
    3.0
    >>> triangleArea(3, 4, 400)
    Traceback (most recent call last):
    ...
    ValueError: Angle should not be greater than 180.
    >>> triangleArea(3, 4, -1)
    Traceback (most recent call last):
    ...
    ValueError: Angle should not be less than 0.
    >>> triangleArea(3, 4, 181)
    Traceback (most recent call last):
    ...
    ValueError: Angle should not be greater than 180.
    */
    public double triangleArea(double a, double b, double angle) {
        if (angle > 180 || angle < 0) {
            raise(ValueError, "Angle should not be greater than 180")
        }
        if (angle < 0) {
            raise(ValueError, "Angle should not be less than 0")
        }
        if (angle == 180) {
            return 0.5 * a * b
        }
        angle %= 180
        return (math.sin(math.radians(angle)) * a * b) / 2
    }
}




























































































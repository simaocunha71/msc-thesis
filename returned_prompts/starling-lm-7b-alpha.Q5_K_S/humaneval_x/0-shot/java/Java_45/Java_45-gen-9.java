        double c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2) - 2 * a * b * Math.cos(angle));
        double area = 0.5 * (a + c) * Math.sin(angle);
        return area;
    }

    /**
    Given length of two sides and an angle return area for a rectangle.
    >>> rectangleArea(3, 4, Math.PI/3)
    6.0
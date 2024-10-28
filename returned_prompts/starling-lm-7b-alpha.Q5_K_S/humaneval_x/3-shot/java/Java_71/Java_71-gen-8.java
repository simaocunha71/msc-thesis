        if (a + b <= c || a + c <= b || b + c <= a) return -1;
        double half_perimeter = (a + b + c) / 2;
        double area = Math.sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c));
        return area;
    }
}


        if (a + b <= c || b + c <= a || a + c <= b) return -1;
        double half_perimeter = (a + b + c) / 2.0;
        double area = Math.sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c));
        return Math.round(area * 100) / 100;
    }
}


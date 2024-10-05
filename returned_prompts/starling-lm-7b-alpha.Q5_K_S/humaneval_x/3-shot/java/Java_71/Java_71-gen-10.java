        if (a + b <= c || b + c <= a || c + a <= b) {
            return -1;
        }
        double semi_perimeter = (a + b + c) / 2;
        double area = Math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c));
        return area;
    }
}


        if (a < b + c && b < a + c && c < a + b) {
            double semi_perimeter = (a + b + c) / 2;
            double area = Math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c));
            return Math.round(area * 100.0) / 100.0;
        } else {
            return -1;
        }
    }
}


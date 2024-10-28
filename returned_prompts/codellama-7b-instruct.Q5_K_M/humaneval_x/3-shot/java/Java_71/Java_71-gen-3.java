        if (a + b > c && b + c > a && a + c > b) {
            double semi_perimeter = (a + b + c) / 2.0;
            double area = Math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c));
            return Math.round(area * 100.0) / 100.0;
        }
        return -1;
    }
}


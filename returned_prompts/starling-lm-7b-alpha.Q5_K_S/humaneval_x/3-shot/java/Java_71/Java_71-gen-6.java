        double perimeter = (a + b + c) / 2.0;
        double area = Math.sqrt(perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c));
        return area;
    }
}


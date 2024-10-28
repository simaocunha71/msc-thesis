    public double triangleArea(double a, double b, double c) {
        // Sort the sides
        double[] sides = {a, b, c};
        Arrays.sort(sides);

        // Check if the sides form a valid triangle
        if (sides[0] + sides[1] <= sides[2]) {
            return -1; // Not a valid triangle
        }

        // Calculate the semi-perimeter
        double s = (sides[0] + sides[1] + sides[2]) / 2;

        // Calculate the area using Heron's formula
        double area = Math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]));

        // Return the area rounded to 2 decimal points
        return Math.round(area * 100.0) / 100.0;
    }
}
    // Check if side and height are valid
    if (a <= 0 || h <= 0) {
        return -1; // invalid input
    }

    // Calculate area
    double area = 0.5 * a * h;

    return area;
}

        // Using Bisection Method to find roots of the polynomial
        double start = -10000;
        double end = 10000;

        while  (end - start > 1e-6)  {
            double mid = start + (end - start) / 2;
            if  (poly(xs, mid) > 0)  {
                end = mid;
            } else  {
                start = mid;
            }
        }
        return start;
     }
}


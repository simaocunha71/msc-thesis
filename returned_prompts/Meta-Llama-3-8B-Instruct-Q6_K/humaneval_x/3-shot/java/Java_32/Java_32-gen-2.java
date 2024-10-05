        double x = xs.get(0);
        double dx = 1e-6; // step size for numerical differentiation
        double prev_result = poly(xs, x);
        while (true) {
            double result = poly(xs, x);
            if (Math.abs(result) < 1e-6) return x; // tolerance
            double deriv = (poly(xs, x + dx) - prev_result) / dx;
            x -= result / deriv;
            prev_result = result;
        }
    }
} // end class Solution


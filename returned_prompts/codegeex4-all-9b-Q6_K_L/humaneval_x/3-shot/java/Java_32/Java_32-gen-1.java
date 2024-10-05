        double left = -1.0;
        double right = 1.0;
        double epsilon = 0.000001;
        
        while (Math.abs(poly(xs, left)) > epsilon) left *= 2;
        while (Math.abs(poly(xs, right)) > epsilon) right *= 2;
        while (Math.abs(left - right) > epsilon) {
            double mid = (left + right) / 2.0;
            if (poly(xs, mid) > 0) right = mid;
            else left = mid;
        }
        return left;
    }
}


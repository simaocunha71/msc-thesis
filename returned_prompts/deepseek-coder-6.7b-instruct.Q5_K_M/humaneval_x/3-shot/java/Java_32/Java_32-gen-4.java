        double lower_bound = -1000000.0;
        double upper_bound = 1000000.0;
        while  (upper_bound  - lower_bound  > 0.000001) {
            double mid_point = (lower_bound + upper_bound) / 2;
            if  (poly(xs, mid_point)  !=  0) {
                if  (poly(xs, lower_bound)   * poly(xs, mid_point)  <  0) {
                    upper_bound  = mid_point;
                } else {
                    lower_bound  = mid_point;
                }
            } else {
                return mid_point;
            }
        }
        return lower_bound;
     }
}


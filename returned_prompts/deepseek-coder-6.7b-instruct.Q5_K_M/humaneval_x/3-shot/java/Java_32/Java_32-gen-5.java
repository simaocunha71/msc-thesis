        double lower = 0.0;
        double upper = 1.0;
        double mid = 0.0;

        while(upper - lower > 1e-6)  {
            mid = (upper + lower) / 2;
            if(poly(xs, mid) < 0)  {
                lower = mid;
            } else {
                upper = mid;
            }
        }
        return mid;
     }
}


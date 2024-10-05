        double start = 0;
        double end = 1;
        while  (poly(xs, start) * poly(xs, end) > 0)  {
            if  (Math.abs(poly(xs, start)) < Math.abs(poly(xs, end))) {
                start  /= 2;
                end  *= 2;
            } else  {
                start *= 2;
                end  /= 2;
            }
        }
        while  (Math.abs(end  - start) > 0.00001)  {
            double mid = (start  + end )  / 2;
            if  (poly(xs, mid) < 0) {
                start = mid;
            } else  {
                end = mid;
            }
        }
        return start;
     }
}


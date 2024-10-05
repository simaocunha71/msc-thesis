        double start = 0.0;
        double end = 1.0;
        double mid = 0.0;

        while  (Math.abs(poly(xs, mid))  >= 0.000001)  {
            mid =  (start  + end)  / 2;
            double mid_val = poly(xs, mid);

            if  (mid_val  > 0) 
                end  =  mid;
            else 
                start  =  mid;
         }
        return mid;
    }
}


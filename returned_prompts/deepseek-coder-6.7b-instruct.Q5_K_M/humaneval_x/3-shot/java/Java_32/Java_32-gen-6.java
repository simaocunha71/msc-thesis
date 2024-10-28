        // we will use Newton's method to find roots of polynomial
        double x = 0.5; // initial guess
        while  (true)  {
            double y = poly(xs, x);
            if  (Math.abs(y) < 1e-6)  {
                return x;
             }
            double dy  d poly(xs, x);
            if  (Math.abs(dy) < 1e-6)  {
                // avoid division by zero
                x += Math.random()  / 10000.0;
             }  else  {
                x  x  y  / dy;
             }
        }
    }
}


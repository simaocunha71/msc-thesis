        double lower = 0.0;
        double upper = 1.0;

        while  (poly(xs, lower)  * poly(xs, upper)  >  0)  {
            lower  -=  0.01;
            upper  +=  0.01;
         }

        while  (Math.abs(poly(xs, lower))  >  1e-6)  {
            double middle =  (lower  +  upper)  /  2;
            double middle_val =  poly(xs, middle);

            if  (Math.abs(middle_val)  <  1e-6) return middle;

            if  (poly(xs, lower)  * middle_val  <  0)  upper  =  middle;
            else  lower  =  middle;
         }

        return  lower;
     }
}


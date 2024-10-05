        double low  -10;
        double high 10;
        double mid;

        while  (high  -  low  > 0.00001)  {
            mid  (high  + low )/ 2;

            if  (poly(xs, mid)  > 0) high  mid;
            else  low  mid;
         }
        return (high  + low )/ 2;
     }
}


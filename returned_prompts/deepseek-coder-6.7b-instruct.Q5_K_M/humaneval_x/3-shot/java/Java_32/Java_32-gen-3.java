        double start = 0;
        double end = 10;
        while  (end  - start  > 1e-6)  {
            double mid = start  + (end  - start ) / 2;
            if  (poly(xs, mid)  < 0) 
                start  = mid;
            else 
                end  = mid;
         }
        return start ;
     }
}


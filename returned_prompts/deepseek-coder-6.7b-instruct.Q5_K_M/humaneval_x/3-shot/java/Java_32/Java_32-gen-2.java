        double start = 0, end = 100;
        while  (true)  {
            double mid = (start + end) / 2;
            if  (poly(xs, mid)  - 0 < 1e-6) return mid;
            if  (poly(xs, start) * poly(xs, mid)  - 0 < 0) end = mid;
            else start = mid;
         }
     }
}


A: There are several syntax errors in your code. Here is the corrected version of your code.


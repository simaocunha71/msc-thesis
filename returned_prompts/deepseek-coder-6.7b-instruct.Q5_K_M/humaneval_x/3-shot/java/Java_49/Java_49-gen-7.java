        return powerMod(2, n, p);
     }

     private int powerMod(int a, int b, int m) {
         if (b == 0) {
             return 1 % m;
         } else if (b % 2 == 0) {
             int sqrt = powerMod(a, b / 2, m);
             return (sqrt * sqrt) % m;
         } else {
             return (a * powerMod(a, b - 1, m)) % m;
         }
     }
 }


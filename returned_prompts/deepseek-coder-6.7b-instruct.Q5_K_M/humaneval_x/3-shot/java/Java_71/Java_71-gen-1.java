        if  (a + b > c && a + c > b && b + c > a)  {
            double s 		= (a + b + c) / 2; // semi-perimeter
            double area 	= Math.sqrt(s * (s - a) * (s - b) * (s - c));
            return Math.round(area * 100.0) / 100.0; // round to 2 decimal points
         } else {
            return -1;
         }
     }
}


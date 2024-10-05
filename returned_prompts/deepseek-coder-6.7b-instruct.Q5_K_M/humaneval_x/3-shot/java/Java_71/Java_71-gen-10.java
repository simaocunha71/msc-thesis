        if  (!(a < (b + c)) && !(b < (a + c)) && !(c < (a + b))) {
            double s = (a + b + c) / 2;
            double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
            return Math.round(area * 100.0) / 100.0;
        } else {
            return -1;
        }
     }
}


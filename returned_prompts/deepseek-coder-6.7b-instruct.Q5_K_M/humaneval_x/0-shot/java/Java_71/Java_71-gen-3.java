        if(a + b > c && a + c > b && b + c > a){
            double s = (a + b + c) / 2;
            double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
            return Math.round(area * 100.0) / 100.0;
        }
        else{
            return -1;
        }
    }
}


A: Here's the solution to your problem. 

public class Solution {
    public double triangleArea(double a, double b, double c)  {
        if(a + b > c && a + c > b && b + c > a){
            double s = (a + b + c) / 2;
            double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
            return Math.round(area * 100.0) / 100.0;
        }
        else{
            return -1;
        }
    }
}


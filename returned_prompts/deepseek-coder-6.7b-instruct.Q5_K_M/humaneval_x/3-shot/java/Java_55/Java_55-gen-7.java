        if  (n  <=  2) return n;
        int  prev  =  1 ,  prev2  =  1;
        for  (int  i  =  3; i  <=  n; i++)  {
             int  temp  =  prev  +  prev2;
             prev2  =  prev;
             prev  =  temp;
         }
         return  prev;
     }
}


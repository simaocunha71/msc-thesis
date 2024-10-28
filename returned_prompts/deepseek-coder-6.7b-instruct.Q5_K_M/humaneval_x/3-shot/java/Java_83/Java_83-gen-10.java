        if(n<=0){
            return 0;
        }
        if(n==1){
            return 1;
        }
        return (int)Math.pow(9,n-1)+startsOneEnds(n-1);
     }
}


        if(x == 1 || n == 1){
            return true;
        }
        int pow = 1;
        while(pow < x){
            pow *= n;
            if(pow == x){
                return true;
            }
        }
        return false;
     }
}


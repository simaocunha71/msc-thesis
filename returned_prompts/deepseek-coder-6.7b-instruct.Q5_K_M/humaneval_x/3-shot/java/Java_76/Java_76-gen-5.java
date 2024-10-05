        if(x == 1){
            return true;
        }

        int power = 2;

        while(Math.pow(n, power) <= x){
            if(Math.pow(n, power) == x){
                return true;
            }
            power++;
        }
        return false;
    }
}


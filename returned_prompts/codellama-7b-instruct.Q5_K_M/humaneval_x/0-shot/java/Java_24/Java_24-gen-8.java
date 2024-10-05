        int i = n;
        while(true) {
            if(n % i == 0) {
                break;
            }
            i--;
        }
        return i;
    }
}



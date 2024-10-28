        if(n > m){
            return -1;
        }
        double average = (n + m) / 2.0;
        int roundedAverage = (int) Math.round(average);
        return Integer.toBinaryString(roundedAverage);
    }
}


        if  (n > m) return -1;

        int avg = (n + m) / 2;
        int roundedAvg = (n + m) % 2 != 0 ? avg + 1 : avg;

        return Integer.toBinaryString(roundedAvg);
     }
}


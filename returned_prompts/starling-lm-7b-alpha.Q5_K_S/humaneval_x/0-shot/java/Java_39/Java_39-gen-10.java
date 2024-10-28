        int [] fibs = {2, 3, 5, 13, 89};
        if (n <= 0) {
            return -1;
        }
        if (n <= 5) {
            return fibs[n - 1];
        }
        int fibN = fibs[fibs.length - 1];
        int i = fibs.length - 1;
        while (fibN % 2 == 0) {
            fibN /= 2;
            if (i == 0) {
                return -1;
            }
            i--;
        }
        while (i > 0) {
            fibN = fibN * fibs[i] * fibs[i];
            while (fibN % 2 == 0) {
                fibN /= 2;
                if (i == 0) {
                    return -1;
                }
                i--;
            }
            i--;
        }
        return fibN;
    }
}






































































































































































































































































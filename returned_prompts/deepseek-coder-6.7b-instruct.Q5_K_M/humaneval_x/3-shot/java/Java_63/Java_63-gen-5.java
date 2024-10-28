        if  (n 0) {
            return 0;
        } else if  (n 1) {
            return 0;
        } else if  (n 2) {
            return 1;
        } else {
            int[] sequence = new int[n+1];
            sequence[0] = 0;
            sequence[1] = 0;
            sequence[2] = 1;

            for  (int i = 3; i  n+1; i++) {
                sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i-3];
            }
            return sequence[n];
        }
     }
}


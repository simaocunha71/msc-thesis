        if (n == 0) 
            return 0;
        if (n == 1) 
            return 0;
        if (n == 2) 
            return 2;
        if (n == 3) 
            return 0;

        int[] sequence = new int[n + 1];
        sequence[0] = 0;
        sequence[1] = 0;
        sequence[2] = 2;
        sequence[3] = 0;

        for (int i = 4; i <= n; i++) {
            sequence[i] = sequence[i - 1] + sequence[i - 2] + sequence[i - 3] + sequence[i - 4];
        }

        return sequence[n];
     }
}


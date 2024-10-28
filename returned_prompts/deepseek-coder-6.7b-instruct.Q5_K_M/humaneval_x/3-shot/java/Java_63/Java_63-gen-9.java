        if  (n  <= 1) return 0;
        if  (n  == 2) return 1;

        int[] fibfib_sequence  = new int[n  +  1];
        fibfib_sequence[0]  = 0;
        fibfib_sequence[1]  = 0;
        fibfib_sequence[2]  = 1;

        for  (int i  =  3; i  <= n; i++) {
            fibfib_sequence[i]  =  fibfib_sequence[i  -  1]  +  fibfib_sequence[i  -  2]  +  fibfib_sequence[i  -  3];
        }
        return fibfib_sequence[n];
     }
}


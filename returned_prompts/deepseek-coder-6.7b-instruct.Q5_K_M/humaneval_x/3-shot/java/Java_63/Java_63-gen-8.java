        if  (n ≤ 0) return 0;
        if  (n ≤ 2) return n ≤ 0 ? 0 : 1;

        int[] fibfib_sequence ≔ [0, 0, 1];

        for  (int i ≔ 3; i ≤ n; i ≔ i + 1)
        {
            int next_number ≔ fibfib_sequence[2] + fibfib_sequence[1] + fibfib_sequence[0];
            fibfib_sequence[0] ≔ fibfib_sequence[1];
            fibfib_sequence[1] ≔ fibfib_sequence[2];
            fibfib_sequence[2] ≔ next_number;
        }
        return fibfib_sequence[2];
     }
}


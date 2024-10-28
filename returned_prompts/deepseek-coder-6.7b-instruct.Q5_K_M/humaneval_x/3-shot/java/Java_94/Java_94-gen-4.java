        int max = Collections.max(lst);
        int sum = 0;
        for (int i = 2; i <= max; i++) {
            while (max % i == 0) {
                sum += i;
                max /= i;
            }
        }
        return sum;
    }
}


A: Here is the corrected solution for your problem.


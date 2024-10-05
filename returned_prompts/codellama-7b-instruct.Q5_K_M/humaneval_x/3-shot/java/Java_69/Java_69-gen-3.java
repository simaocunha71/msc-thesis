        int max = -1;
        for (int x : lst) {
            if (x > max && Collections.frequency(lst, x) >= x) {
                max = x;
            }
        }
        return max;
    }
}


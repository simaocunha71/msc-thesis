        int result = 0;
        int max = 0;
        for (int i : lst) {
            if (i > max) {
                max = i;
            }
        }
        while (max > 0) {
            result += max % 10;
            max /= 10;
        }
        return result;
    }
}


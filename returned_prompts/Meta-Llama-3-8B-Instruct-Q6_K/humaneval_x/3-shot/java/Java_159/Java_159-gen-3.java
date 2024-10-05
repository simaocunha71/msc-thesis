        int total = number + need;
        int left = remaining - (need - number);
        if (left < 0) {
            total += left;
            left = 0;
        }
        return Arrays.asList(total, left);
    }
}


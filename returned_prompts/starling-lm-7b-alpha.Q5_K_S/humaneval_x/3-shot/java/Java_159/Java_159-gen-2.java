        int total = number + need;
        int left = remaining - (need - number);
        if (total > remaining) {
            left = 0;
        }
        return Arrays.asList(total, left);
    }
}


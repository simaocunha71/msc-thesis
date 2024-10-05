        int total = number + need;
        if (total > remaining) {
            return Arrays.asList(remaining, 0);
        } else {
            return Arrays.asList(total, remaining - total);
        }
    }
}


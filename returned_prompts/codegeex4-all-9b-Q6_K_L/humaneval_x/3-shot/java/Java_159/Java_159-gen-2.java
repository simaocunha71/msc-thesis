        int total = number + need;
        int left = Math.max(0, remaining - total);

        return Arrays.asList(total, left);
    }
}


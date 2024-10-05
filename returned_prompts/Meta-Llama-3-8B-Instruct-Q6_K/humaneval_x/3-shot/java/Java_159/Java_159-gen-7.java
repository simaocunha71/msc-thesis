        int total = number + need;
        int left = remaining - (total - remaining);
        return Arrays.asList(total, left);
    }
}


        int total = number + need;
        int left = remaining - (total - number);
        return Arrays.asList(total, left);
    }
}


        int eaten = number + need;
        int left = Math.max(0, remaining - need);
        return Arrays.asList(eaten, left);
    }
}


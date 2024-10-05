        int eaten = number + need - remaining;
        int left = remaining - (need - eaten);
        return Arrays.asList(eaten, left < 0 ? 0 : left);
    }
}


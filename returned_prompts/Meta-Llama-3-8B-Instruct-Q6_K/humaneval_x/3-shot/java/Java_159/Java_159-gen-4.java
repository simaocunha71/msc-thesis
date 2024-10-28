        int eaten = number + remaining;
        int left = eaten + need - remaining;

        return Arrays.asList(eaten, left);
    }
}


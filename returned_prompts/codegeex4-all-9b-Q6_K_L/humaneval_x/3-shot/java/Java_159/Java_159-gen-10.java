        int total_eaten = number + need;
        int left = remaining - need;
        if (left < 0) {
            left = 0;
        }
        return Arrays.asList(total_eaten, left);
    }
}


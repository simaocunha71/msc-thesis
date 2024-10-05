        int total_eaten = number + need;
        int left_over = remaining - need;
        if (left_over < 0) {
            total_eaten += left_over;
            left_over = 0;
        }
        return Arrays.asList(total_eaten, left_over);
    }
}


        int total_eaten = number + need;
        int leftover = remaining - need;
        if (leftover < 0) {
            total_eaten += leftover;
            leftover = 0;
        }
        return Arrays.asList(total_eaten, leftover);
    }
}


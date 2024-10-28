        int total_eaten = number + need;
        int remaining_carrots = remaining - need;
        if (remaining_carrots < 0) remaining_carrots = 0;
        return Arrays.asList(total_eaten, remaining_carrots);
    }
}


        int total_eaten = number + need;
        int remaining_carrots = remaining - need;

        if (total_eaten > remaining) {
            total_eaten = remaining;
            remaining_carrots = 0;
        }

        return Arrays.asList(total_eaten, remaining_carrots);
    }
}


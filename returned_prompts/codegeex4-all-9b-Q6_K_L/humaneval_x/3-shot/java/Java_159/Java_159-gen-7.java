        int total_eaten = number + need;
        int left = total_eaten <= remaining ? 0 : remaining - total_eaten + need;
        return Arrays.asList(total_eaten, left);
    }
}


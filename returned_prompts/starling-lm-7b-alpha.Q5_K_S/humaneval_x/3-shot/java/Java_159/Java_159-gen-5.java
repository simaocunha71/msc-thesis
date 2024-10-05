        int total_eaten = number + need;
        int remaining_after_eat = remaining - need;

        if (remaining_after_eat < 0) {
            total_eaten += remaining_after_eat;
            remaining_after_eat = 0;
        }

        return Arrays.asList(total_eaten, remaining_after_eat);
    }
}


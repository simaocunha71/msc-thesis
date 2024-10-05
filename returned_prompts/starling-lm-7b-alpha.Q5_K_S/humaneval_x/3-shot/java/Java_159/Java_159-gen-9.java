        int total_eaten = number + need;
        int remaining_after_meals = remaining - need;
        if (remaining_after_meals < 0) {
            total_eaten += remaining_after_meals;
            remaining_after_meals = 0;
        }
        return Arrays.asList(total_eaten, remaining_after_meals);
    }
}



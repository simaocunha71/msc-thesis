        int totalEaten = number + need;
        int carrotsLeft = remaining - (need - number);
        if (carrotsLeft < 0) {
            carrotsLeft = 0;
        }
        return Arrays.asList(totalEaten, carrotsLeft);
    }
}


        int totalEaten = number + need;
        int left = remaining - (need - totalEaten);
        return new ArrayList<>(Arrays.asList(totalEaten, left < 0 ? 0 : left));
    }
}


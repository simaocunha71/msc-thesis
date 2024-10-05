        List<Integer> result = new ArrayList<>();
        int total_eaten = number + need;

        if (total_eaten <= remaining) {
            result.add(total_eaten);
            result.add(remaining - total_eaten);
        } else {
            result.add(remaining);
            result.add(0);
        }
        return result;
    }
}


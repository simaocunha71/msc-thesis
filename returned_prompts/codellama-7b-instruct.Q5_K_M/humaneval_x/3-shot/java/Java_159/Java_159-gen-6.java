        int eat_carrot = need - number;
        int left_carrot = remaining - eat_carrot;

        List<Integer> result = new ArrayList<>();
        result.add(number + eat_carrot);
        result.add(left_carrot);

        return result;
    }
}


        List<Integer> result = new ArrayList<>();

        if (need > remaining) {
            number += remaining;
            result.add(number);
            result.add(0);
        } else {
            number += need;
            result.add(number);
            result.add(remaining - need);
        }
        return result;
    }
}


        List<Integer> result = new ArrayList<>();
        int eat = 0;
        int left = 0;

        if (remaining < need) {
            eat = remaining;
            left = 0;
        } else {
            eat = need;
            left = remaining - need;
        }

        result.add(number + eat);
        result.add(left);
        return result;
    }
}


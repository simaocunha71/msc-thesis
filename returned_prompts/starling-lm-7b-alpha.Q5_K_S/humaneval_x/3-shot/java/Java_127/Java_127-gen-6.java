        List<Integer> intersection = new ArrayList<>();

        for (int i = Math.max(interval1.get(0), interval2.get(0));
             i <= Math.min(interval1.get(1), interval2.get(1));
             i++) {
            intersection.add(i);
        }

        int length = intersection.size();
        boolean is_prime = true;
        for (int i = 2; i * i <= length; i++) {
            if (length % i == 0) {
                is_prime = false;
                break;
            }
        }

        if (is_prime) {
            return "YES";
        } else {
            return "NO";
        }
    }
}


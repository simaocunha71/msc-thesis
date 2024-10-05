        Set<Integer> numbers = new HashSet<>();

        for (int n : l) {
            if (numbers.contains(-n)) {
                return true;
            }
            numbers.add(n);
        }

        return false;
     }
}


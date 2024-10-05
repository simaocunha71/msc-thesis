        Set<Integer> numbers = new HashSet<>();
        for (int i : l) {
            if (numbers.contains(i)) {
                return true;
            } else {
                numbers.add(-i);
            }
        }
        return false;
    }
}


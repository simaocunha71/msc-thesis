        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < l.size(); i++) {
            int number = l.get(i);
            if (seen.contains(number)) {
                return true;
            }
            seen.add(-number);
        }
        return false;
    }
}


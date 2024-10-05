        Set<Integer> seen = new HashSet<>();
        for (Integer num : l) {
            if (seen.contains(-num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
     }
}


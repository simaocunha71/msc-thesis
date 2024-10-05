        Set<Integer> set = new HashSet<>(l);
        for (Integer i : l) {
            if (set.contains(-i)) {
                return true;
            }
        }
        return false;
     }
}


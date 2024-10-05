        Set<Integer> unique_elements = new HashSet<Integer>();
        for (int i : l) {
            if (unique_elements.contains(-i)) {
                return true;
            } else {
                unique_elements.add(i);
            }
        }
        return false;
    }
}


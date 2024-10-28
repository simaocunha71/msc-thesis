        Set<Integer> common_elements = new HashSet<>();

        for (Integer l1_element : l1) {
            for (Integer l2_element : l2) {
                if (l1_element.equals(l2_element)) {
                    common_elements.add(l1_element);
                }
            }
        }
        return new ArrayList<>(common_elements);
    }
}


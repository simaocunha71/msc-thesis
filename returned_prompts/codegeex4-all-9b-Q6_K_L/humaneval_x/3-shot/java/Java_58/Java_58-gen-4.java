        Set<Integer> result = new HashSet<>();

        for (int i : l1) {
            if (l2.contains(i)) {
                result.add(i);
            }
        }
        List<Integer> final_result = new ArrayList<>(result);
        Collections.sort(final_result);
        return final_result;
    }
}


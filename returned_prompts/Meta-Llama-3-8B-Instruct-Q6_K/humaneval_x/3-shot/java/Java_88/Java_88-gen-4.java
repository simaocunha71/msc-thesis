        int sum = array.get(0) + array.get(array.size() - 1);
        List<Integer> sorted_array = new ArrayList<>(array);
        if (sum % 2 == 0) {
            Collections.sort(sorted_array, Collections.reverseOrder());
        } else {
            Collections.sort(sorted_array);
        }
        return sorted_array;
    }
}
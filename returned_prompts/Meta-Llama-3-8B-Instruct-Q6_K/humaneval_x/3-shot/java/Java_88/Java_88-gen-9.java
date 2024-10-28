        int sum = array.get(0) + array.get(array.size() - 1);
        List<Integer> copy = new ArrayList<>(array);

        if (sum % 2 == 0) {
            Collections.sort(copy, Collections.reverseOrder());
        } else {
            Collections.sort(copy);
        }
        return copy;
    }
}
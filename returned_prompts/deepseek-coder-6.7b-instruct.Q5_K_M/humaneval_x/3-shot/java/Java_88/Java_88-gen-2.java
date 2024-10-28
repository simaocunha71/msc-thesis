        List<Integer> copy = new ArrayList<>(array);
        int sum = array.get(0) + array.get(array.size() - 1);
        if (sum % 2 == 0) {
            Collections.sort(copy);
        } else {
            Collections.sort(copy, Collections.reverseOrder());
        }
        return copy;
    }
}


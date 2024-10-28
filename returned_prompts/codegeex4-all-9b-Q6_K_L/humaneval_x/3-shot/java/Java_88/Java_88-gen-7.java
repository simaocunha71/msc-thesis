        List<Integer> result = new ArrayList<>(array);
        if (array.size() == 0) {
            return result;
        }
        if ((array.get(0) + array.get(array.size() - 1)) % 2 == 0) {
            Collections.sort(result, Collections.reverseOrder());
        } else {
            Collections.sort(result);
        }
        return result;
    }
}


        List<Integer> result = new ArrayList<>(array);
        int first_index = result.get(0);
        int last_index = result.get(result.size() - 1);
        if ((first_index + last_index) % 2 == 0) {
            Collections.sort(result, Collections.reverseOrder());
        } else {
            Collections.sort(result);
        }
        return result;
    }
}


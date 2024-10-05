        List<Integer> result = new ArrayList<>(array);
        Collections.sort(result);
        int first_index = 0;
        int last_index = result.size() - 1;
        int sum = result.get(first_index) + result.get(last_index);
        if (sum % 2 == 0) {
            Collections.reverse(result);
        }
        return result;
    }
}


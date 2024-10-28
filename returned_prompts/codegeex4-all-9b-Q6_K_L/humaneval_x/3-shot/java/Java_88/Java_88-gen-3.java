        List<Integer> result = new ArrayList<>(array);
        int sum = array.get(0) + array.get(array.size() - 1);

        if (sum % 2 == 0) {
            Collections.sort(result, Collections.reverseOrder());
        } else {
            Collections.sort(result);
        }
        return result;
    }
}


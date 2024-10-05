        int sum = array.get(0) + array.get(array.size() - 1);
        List<Integer> result = new ArrayList<>(array);

        if (sum % 2 == 0) {
            Collections.sort(result, Collections.reverseOrder());
        } else {
            Collections.sort(result);
        }

        return result;
    }
}


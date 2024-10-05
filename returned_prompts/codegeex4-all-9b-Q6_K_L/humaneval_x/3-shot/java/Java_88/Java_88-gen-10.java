        List<Integer> result = new ArrayList<>(array);
        if (result.size() == 0) return result;
        int sum = result.get(0) + result.get(result.size() - 1);
        if (sum % 2 == 0) Collections.sort(result, Collections.reverseOrder());
        else Collections.sort(result);
        return result;
    }
}


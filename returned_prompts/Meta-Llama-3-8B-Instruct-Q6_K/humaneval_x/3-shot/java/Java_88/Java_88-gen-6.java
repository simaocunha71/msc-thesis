        List<Integer> result = new ArrayList<>(array);
        if ((result.get(0) + result.get(result.size() - 1)) % 2 == 0) {
            Collections.sort(result, Collections.reverseOrder());
        } else {
            Collections.sort(result);
        }
        return result;
    }
}


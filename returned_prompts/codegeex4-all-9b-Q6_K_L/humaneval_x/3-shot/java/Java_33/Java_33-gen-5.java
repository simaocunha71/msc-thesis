        List<Integer> result = new ArrayList<>(l);
        Collections.sort(result);
        for (int i = 0; i < result.size(); i += 3) {
            Collections.swap(result, i, i / 3 * 3);
        }
        return result;
    }
}


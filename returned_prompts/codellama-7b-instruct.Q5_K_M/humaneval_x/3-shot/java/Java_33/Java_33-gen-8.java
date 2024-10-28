        List<Integer> result = new ArrayList<>(l);
        Collections.sort(result);

        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                result.set(i, l.get(i));
            }
        }

        return result;
    }
}


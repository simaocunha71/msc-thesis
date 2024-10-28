        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                List<Integer> temp = new ArrayList<>(Arrays.asList(l.get(i)));
                Collections.sort(temp);
                result.add(temp.get(0));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
} 
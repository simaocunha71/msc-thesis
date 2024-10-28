        List<Integer> even = new ArrayList<>();
        List<Integer> odd = new ArrayList<>();

        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                even.add(l.get(i));
            } else {
                odd.add(l.get(i));
            }
        }
        Collections.sort(even);

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                result.add(even.get(i / 2));
            } else {
                result.add(odd.get(i / 2));
            }
        }
        return result;
    }
}


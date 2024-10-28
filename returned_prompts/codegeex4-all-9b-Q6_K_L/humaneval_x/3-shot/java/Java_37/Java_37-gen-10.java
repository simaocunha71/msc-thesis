        List<Integer> even = new ArrayList<>();
        List<Integer> odd = new ArrayList<>();

        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) even.add(l.get(i));
            else odd.add(l.get(i));
        }
        Collections.sort(even);
        for (int i = 0; i < even.size(); i++) {
            odd.add(i * 2, even.get(i));
        }
        return odd;
    }
}


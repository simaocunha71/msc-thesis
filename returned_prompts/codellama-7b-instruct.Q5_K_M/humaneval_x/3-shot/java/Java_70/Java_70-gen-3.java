        List<Integer> result = new ArrayList<>();
        int min = lst.get(0);
        int max = lst.get(0);

        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) < min) min = lst.get(i);
            if (lst.get(i) > max) max = lst.get(i);
        }

        for (int i = min; i <= max; i++) {
            for (int j = 0; j < lst.size(); j++) {
                if (lst.get(j) == i) result.add(i);
            }
        }
        return result;
    }
}


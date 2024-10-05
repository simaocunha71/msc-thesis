        if (lst.size() == 0) return lst;
        int min = lst.get(0);
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < min) min = lst.get(i);
        }

        int max = lst.get(0);
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) > max) max = lst.get(i);
        }

        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) == min) result.add(min);
            if (lst.get(i) == max) result.add(max);
        }

        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) != min && lst.get(i) != max) result.add(lst.get(i));
        }

        return result;
    }
}


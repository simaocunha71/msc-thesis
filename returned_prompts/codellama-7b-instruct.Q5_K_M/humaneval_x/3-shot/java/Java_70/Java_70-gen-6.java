        if (lst.size() == 1) {
            return lst;
        }

        int min = lst.get(0);
        int max = lst.get(0);

        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) < min) {
                min = lst.get(i);
            }

            if (lst.get(i) > max) {
                max = lst.get(i);
            }
        }

        lst.remove(max);
        lst.remove(min);

        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) < min) {
                left.add(lst.get(i));
            } else {
                right.add(lst.get(i));
            }
        }

        if (left.size() > 0) {
            left = strangeSortList(left);
        }

        if (right.size() > 0) {
            right = strangeSortList(right);
        }

        List<Integer> result = new ArrayList<>();
        result.add(min);

        if (left.size() > 0) {
            result.addAll(left);
        }

        result.add(max);

        if (right.size() > 0) {
            result.addAll(right);
        }

        return result;
    }
}


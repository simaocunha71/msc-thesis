        List<Integer> result = new ArrayList<>();
        if (lst.size() == 0) return result;
        else if (lst.size() == 1) return lst;

        int min = lst.get(0);
        for (int i = 1; i < lst.size(); i++)
            if (lst.get(i) < min) min = lst.get(i);

        int max = lst.get(0);
        for (int i = 1; i < lst.size(); i++)
            if (lst.get(i) > max) max = lst.get(i);

        while (min <= max) {
            int i = 0;
            for (i = 0; i < lst.size(); i++)
                if (lst.get(i) == min) break;
            result.add(min);

            for (int j = i + 1; j < lst.size(); j++)
                if (lst.get(j) == max) break;
            result.add(max);

            min = lst.get(j + 1);
            max = lst.get(i + 1);
        }

        return result;
    }
}


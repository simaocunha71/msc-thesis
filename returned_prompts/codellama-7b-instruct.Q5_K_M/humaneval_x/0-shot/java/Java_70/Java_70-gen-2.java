        List<Integer> result = new ArrayList<Integer>();
        if (lst.size() == 0)
            return result;

        int min = lst.get(0);
        for (int i = 1; i < lst.size(); i++)
            if (lst.get(i) < min)
                min = lst.get(i);

        result.add(min);
        lst.remove(min);

        if (lst.size() == 0)
            return result;

        int max = lst.get(0);
        for (int i = 1; i < lst.size(); i++)
            if (lst.get(i) > max)
                max = lst.get(i);

        result.add(max);
        lst.remove(max);

        if (lst.size() == 0)
            return result;

        int min2 = lst.get(0);
        for (int i = 1; i < lst.size(); i++)
            if (lst.get(i) < min2)
                min2 = lst.get(i);

        result.add(min2);
        lst.remove(min2);

        if (lst.size() == 0)
            return result;

        int max2 = lst.get(0);
        for (int i = 1; i < lst.size(); i++)
            if (lst.get(i) > max2)
                max2 = lst.get(i);

        result.add(max2);
        lst.remove(max2);

        return result;
    }
}

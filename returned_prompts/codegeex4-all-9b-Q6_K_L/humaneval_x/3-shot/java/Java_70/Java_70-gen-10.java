        List<Integer> result = new ArrayList<>();
        if (lst.size() == 0) return result;
        Collections.sort(lst);
        int i = 0;
        int j = lst.size() - 1;
        while (i <= j) {
            result.add(lst.get(i));
            if (i != j) result.add(lst.get(j));
            i++;
            j--;
        }
        return result;
    }
}


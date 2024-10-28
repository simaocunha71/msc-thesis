        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) result.add(l.get(i));
            else result.add(sortedList(l.subList(i - 1, i + 1)));
        }
        return result;
    }

    private Integer sortedList(List<Integer> l) {
        Collections.sort(l);
        return l.get(0);
    }
}


```
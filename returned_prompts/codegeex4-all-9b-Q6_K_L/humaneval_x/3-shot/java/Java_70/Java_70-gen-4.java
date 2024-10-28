        List<Integer> result = new ArrayList<>();
        Collections.sort(lst);
        int start = 0;
        int end = lst.size() - 1;
        boolean min = true;

        while (start <= end) {
            if (min) {
                result.add(lst.get(start));
                start += 1;
            } else {
                result.add(lst.get(end));
                end -= 1;
            }
            min = !min;
        }
        return result;
    }
}


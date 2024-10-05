        for (List<Integer> row : lst) {
            if (row.contains(x)) {
                List<List<Integer>> result = new ArrayList<>();
                int y = row.indexOf(x);
                result.add(Arrays.asList(lst.indexOf(row), y));
                return result;
            }
        }
        return new ArrayList<>();
    }
}
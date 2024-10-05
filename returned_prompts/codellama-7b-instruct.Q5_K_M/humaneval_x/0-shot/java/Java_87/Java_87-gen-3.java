        List<List<Integer>> result = new ArrayList<>();
        if (lst.isEmpty()) return result;
        int rows = lst.size();
        int cols = lst.get(0).size();
        for (int r = 0; r < rows; r++) {
            int c = 0;
            while (c < cols && lst.get(r).get(c++) != x) ;
            if (c < cols) result.add(Arrays.asList(r, c-1));
        }
        return result;
    }
}

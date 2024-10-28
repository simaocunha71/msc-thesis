        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            List<Integer> temp = new ArrayList<>();
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    temp.add(i);
                    temp.add(j);
                    result.add(temp);
                    temp.clear();
                }
            }
        }
        Collections.sort(result, (a, b) -> a.get(0) - b.get(0));
        Collections.sort(result, (a, b) -> b.get(1) - a.get(1));
        return result;
    }
}


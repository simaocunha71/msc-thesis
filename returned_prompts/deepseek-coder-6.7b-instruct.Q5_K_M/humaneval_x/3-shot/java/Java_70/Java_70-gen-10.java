        if(lst.size()==0) return lst;
        List<Integer> sortedList = new ArrayList<>(lst);
        Collections.sort(sortedList);
        List<Integer> result = new ArrayList<>();
        while (!sortedList.isEmpty()) {
            result.add(sortedList.remove(0));
            if (!sortedList.isEmpty()) {
                result.add(sortedList.remove(sortedList.size() - 1));
            }
        }
        return result;
    }
}


        List<String> sortedList = new ArrayList<String>();
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i).length() % 2 == 0) {
                sortedList.add(lst.get(i));
            }
        }
        sortedList.sort(Comparator.comparingInt(String::length).thenComparing(String::compareTo));
        return sortedList;
    }
}

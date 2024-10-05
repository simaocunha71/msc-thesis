        List<String> sortedList = new ArrayList<String>();
        for (String word : lst) {
            if (word.length() % 2 == 0) {
                sortedList.add(word);
            }
        }
        Collections.sort(sortedList);
        return sortedList;
    }
}

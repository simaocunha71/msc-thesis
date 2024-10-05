        List<Integer> result = new ArrayList<>();
        List<Integer> sortedList = new ArrayList<>(lst);
        Collections.sort(sortedList);

        while (!sortedList.isEmpty()) {
            result.add(sortedList.get(0));
            sortedList.remove(0);
            if (!sortedList.isEmpty()) {
                int maxIndex = 0;
                for (int i = 1; i < sortedList.size(); i++) {
                    if (sortedList.get(i) > sortedList.get(maxIndex)) {
                        maxIndex = i;
                    }
                }
                result.add(sortedList.get(maxIndex));
                sortedList.remove(maxIndex);
            }
        }
        return result;
    }
}


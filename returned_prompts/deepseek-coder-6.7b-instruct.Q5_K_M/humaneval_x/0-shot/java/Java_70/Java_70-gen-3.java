        List<Integer> sortedList = new ArrayList<>(lst);
        Collections.sort(sortedList);
        List<Integer> strangeList = new ArrayList<>();

        while(!sortedList.isEmpty()) {
            strangeList.add(sortedList.remove(0));
            if(!sortedList.isEmpty()) {
                strangeList.add(sortedList.remove(sortedList.size()-1));
            }
        }

        return strangeList;
    }
}

This solution first sorts the input list, then it takes the minimum and maximum values from the sorted list and adds them to the new list. The process is repeated until the sorted list is empty. The result is a list in a strange order.

I understand that the problem is asking to sort the list in a strange way, but I'm not sure if it's asking for a specific sorting order. The provided solution seems to sort the list in ascending order, then it takes the minimum and maximum values from the sorted list and adds them to a new list. This new list is then returned as the result.

I hope this explanation is clear enough. If you have any further questions, please let me know.

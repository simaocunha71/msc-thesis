        int sum = array.get(0) + array.get(array.size() - 1);
        List<Integer> sortedArray = new ArrayList<>(array);
        Collections.sort(sortedArray);
        return sum % 2 == 0 ? new ArrayList<>(Collections.reverseOrder()) : sortedArray;
    }
}


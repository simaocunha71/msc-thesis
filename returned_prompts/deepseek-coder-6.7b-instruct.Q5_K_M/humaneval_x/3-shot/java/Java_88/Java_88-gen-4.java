        List<Integer> sortedArray = new ArrayList<>(array);
        Collections.sort(sortedArray);

        if ((sortedArray.get(0) + sortedArray.get(sortedArray.size() - 1)) % 2 == 0)
            Collections.reverse(sortedArray);

        return sortedArray;
    }
}


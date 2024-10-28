        List<Integer> sortedArray = new ArrayList<>(array);
        Collections.sort(sortedArray);

        int sum = sortedArray.get(0) + sortedArray.get(sortedArray.size() - 1);

        if (sum % 2 == 0) {
            Collections.reverse(sortedArray);
        }

        return sortedArray;
     }
}


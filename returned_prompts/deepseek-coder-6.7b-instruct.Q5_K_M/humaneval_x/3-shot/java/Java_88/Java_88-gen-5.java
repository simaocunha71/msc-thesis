        List<Integer> sorted = new ArrayList<>(array);
        Collections.sort(sorted);
        if ((array.get(0) + array.get(array.size() - 1)) % 2 == 0) {
            Collections.reverse(sorted);
        }
        return sorted;
     }
}


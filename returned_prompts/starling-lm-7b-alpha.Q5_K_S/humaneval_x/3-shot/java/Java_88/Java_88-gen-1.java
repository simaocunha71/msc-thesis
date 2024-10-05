        Collections.sort(array);
        int first = array.get(0);
        int last = array.get(array.size() - 1);
        if ((first + last) % 2 == 0) Collections.reverse(array);
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < array.size(); i++) result.add(array.get(i));
        return result;
    }
}


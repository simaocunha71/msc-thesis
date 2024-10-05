        int index = arr.indexOf(Collections.min(arr));
        if (index == -1)
            return Collections.emptyList();

        List<Integer> result = new ArrayList<>();
        result.add(arr.get(index));
        result.add(index);
        arr.remove(index);
        return result;
    }
}




























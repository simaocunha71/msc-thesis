        Collections.sort(arr);
        List<Integer> result = new ArrayList<>();
        for (int i = arr.size() - k; i < arr.size(); i++) {
            result.add(arr.get(i));
        }
        return result;
    }
}


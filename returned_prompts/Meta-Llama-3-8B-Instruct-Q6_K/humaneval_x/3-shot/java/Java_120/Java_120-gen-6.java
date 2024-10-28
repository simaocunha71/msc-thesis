        List<Integer> result = new ArrayList<>();
        Collections.sort(arr, Collections.reverseOrder());
        for (int i = 0; i < k; i++) {
            result.add(arr.get(i));
        }
        return result;
    }
}


        Collections.sort(arr);
        Collections.reverse(arr);
        List<Integer> result = arr.subList(0, Math.min(k, arr.size()));
        return result;
    }
}


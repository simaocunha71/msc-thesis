        List<Integer> result = new ArrayList<>(l);
        Collections.sort(result);
        result.removeIf((e, i) -> Collections.binarySearch(result, e) != i);
        return result;
    }
}


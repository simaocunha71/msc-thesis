        Set<Integer> uniqueElements = new HashSet<>(l);
        List<Integer> result = new ArrayList<>(uniqueElements);
        Collections.sort(result);
        return result;
     }
}


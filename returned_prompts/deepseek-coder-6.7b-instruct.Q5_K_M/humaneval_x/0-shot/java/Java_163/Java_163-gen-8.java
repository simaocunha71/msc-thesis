        List<Integer> result = new ArrayList<Integer>();
        int start = Math.min(a, b);
        int end = Math.max(a, b);
        for (int i = start; i <= end; i++) {
            if (i % 2 == 0) {
                result.add(i);
            }
        }
        return result;
    }
}


A: 

        int result = l.get(0);
        for (Integer i : l) {
            result = Math.max(result, i);
        }
        return result;
    }
}


        List<Integer> result = new ArrayList<>(array);
        Collections.sort(result);
        int first = result.get(0);
        int last = result.get(result.size() - 1);
        if ((first + last) % 2 == 0) {
            Collections.reverse(result);
        }
        return result;
    }
}


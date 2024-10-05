        List<Integer> result = new ArrayList<>(array);
        Collections.sort(result);
        if ((array.get(0) + array.get(array.size() - 1)) % 2 == 0) {
            Collections.reverse(result);
        }
        return result;

    }
}


        List<Integer> copy = new ArrayList<>(array);
        Collections.sort(copy);

        if ((array.get(0) + array.get(array.size() - 1)) % 2 == 1) {
            return copy;
        } else {
            Collections.reverse(copy);
            return copy;
        }
     }
}


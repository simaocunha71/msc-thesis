        List<Integer> result = new ArrayList<>(l);
        List<Integer> temp = new ArrayList<>();

        for (int i = 2; i < result.size(); i += 3) {
            temp.add(result.remove(i));
        }

        Collections.sort(temp);

        for (int i = 2; i < result.size(); i += 3) {
            result.add(i, temp.remove(0));
        }

        return result;
    }
}


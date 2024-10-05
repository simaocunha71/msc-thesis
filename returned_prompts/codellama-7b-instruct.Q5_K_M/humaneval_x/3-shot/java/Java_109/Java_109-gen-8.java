        if (arr.size() == 0) return true;

        int last = arr.get(arr.size() - 1);
        arr.remove(arr.size() - 1);
        arr.add(0, last);

        Collections.sort(arr);

        return arr.get(0) < arr.get(1);

    }
}


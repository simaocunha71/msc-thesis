        if (arr.isEmpty()) return true;

        int min = Collections.min(arr);
        int index = arr.indexOf(min);

        return index == arr.size() - 1;
    }
}


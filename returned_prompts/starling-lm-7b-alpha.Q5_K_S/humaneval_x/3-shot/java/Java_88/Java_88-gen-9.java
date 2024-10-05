        Collections.sort(array);
        int first = array.get(0);
        int last = array.get(array.size() - 1);
        if ((first + last) % 2 == 0) Collections.reverse(array);
        return array;
    }
}


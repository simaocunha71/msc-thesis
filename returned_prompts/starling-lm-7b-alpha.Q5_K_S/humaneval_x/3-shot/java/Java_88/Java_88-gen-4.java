        Collections.sort(array);
        int sum = array.get(0) + array.get(array.size() - 1);
        if (sum % 2 == 0) {
            Collections.reverse(array);
        }
        return array;
    }
}


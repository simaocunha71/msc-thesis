        int sum = array.get(0) + array.get(array.size() - 1);
        if (sum % 2 == 0) {
            // sort in descending order
            Collections.sort(array, Collections.reverseOrder());
        } else {
            // sort in ascending order
            Collections.sort(array);
        }
        return array;
    }
}


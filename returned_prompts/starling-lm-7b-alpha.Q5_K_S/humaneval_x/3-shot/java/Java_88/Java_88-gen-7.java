        Collections.sort(array);
        int first_index = 0;
        int last_index = array.size() - 1;
        int sum = array.get(first_index) + array.get(last_index);
        if (sum % 2 == 0) {
            Collections.reverse(array);
        }
        return array;
    }
}


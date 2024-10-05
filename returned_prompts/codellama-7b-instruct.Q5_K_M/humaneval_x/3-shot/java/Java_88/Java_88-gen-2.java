        int sum = 0;
        for (int i = 0; i < array.size(); i++) {
            sum += array.get(i);
        }

        if (sum % 2 == 0) {
            Collections.sort(array, Collections.reverseOrder());
        } else {
            Collections.sort(array);
        }
        return array;
    }
}


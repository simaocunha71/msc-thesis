        int max_index = arr.indexOf(Collections.max(arr));
        int min_index = arr.indexOf(Collections.min(arr));

        if (max_index > min_index) {
            Collections.rotate(arr, arr.size() - min_index);
            return arr.equals(Collections.sort(arr));
        }
        else {
            Collections.rotate(arr, arr.size() - max_index);
            return arr.equals(Collections.sort(arr));
        }
    }
}


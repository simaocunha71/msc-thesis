        Collections.sort(arr);
        return arr.subList(arr.size() - k, arr.size());
    }
}  // This solution is not efficient for large inputs, because it needs to sort the entire array.


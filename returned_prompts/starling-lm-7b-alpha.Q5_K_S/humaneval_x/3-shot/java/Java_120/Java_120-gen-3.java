        Collections.sort(arr);
        Collections.reverse(arr);
        return arr.subList(0, Math.min(k, arr.size()));
    }
}


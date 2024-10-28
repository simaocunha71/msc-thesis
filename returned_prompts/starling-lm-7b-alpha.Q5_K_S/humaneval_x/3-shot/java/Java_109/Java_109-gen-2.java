        Collections.sort(arr);
        for (int i = 0; i < arr.size() - 1; i++) {
            if (arr.get(i + 1) < arr.get(i)) return false;
        }
        return true;
    }
}



```
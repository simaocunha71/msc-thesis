        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) >= arr.get(i-1))
                continue;
            else
                return i-1;
        }
        return -1;
    }
}


        int count = 0;
        int l = arr.size();
        for  (int i = 0; i < l / 2; i++) {
            if  (!arr.get(i).equals(arr.get(l - i - 1))) count++;
        }
        return count;
    }
}


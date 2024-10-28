        int count = 0;
        for(int i = 2; i < n && count < 4; i += 2){
            if(i % 2 == 0) {
                count++;
            }
        }
        return count == 4;
    }
}


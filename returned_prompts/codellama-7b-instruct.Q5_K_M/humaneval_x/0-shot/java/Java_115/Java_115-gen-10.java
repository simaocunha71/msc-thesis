        int answer = 0;
        for (List<Integer> row : grid) {
            int current = 0;
            for (int col : row) {
                if (col == 1) {
                    current++;
                } else {
                    if (current > 0) {
                        answer++;
                        current = 0;
                    }
                }
            }
            if (current > 0) {
                answer++;
                current = 0;
            }
        }
        return answer;
    }
}




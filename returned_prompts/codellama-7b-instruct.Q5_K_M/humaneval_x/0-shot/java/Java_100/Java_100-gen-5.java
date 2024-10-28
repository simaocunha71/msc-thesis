        List<Integer> answer = new ArrayList();
        for (int i = 0; i < n; i++) {
            int x = (i % 2 == 0) ? i + 1 : i + 2;
            answer.add(x);
        }
        return answer;
    }
}





























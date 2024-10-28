        List<List<Integer>> answer = new ArrayList<List<Integer>>();
        if (lst.isEmpty()) return answer;
        int row = 0;
        int col = 0;
        for (List<Integer> l : lst) {
            if (l.size() == 0) continue;
            if (l.contains(x)) {
                row++;
                answer.add(new ArrayList<Integer>());
                answer.get(answer.size() - 1).add(row);
                answer.get(answer.size() - 1).add(l.indexOf(x));
            }
        }
        for (int i = 0; i < answer.size(); i++) {
            for (int j = 0; j < answer.size() - i - 1; j++) {
                if (answer.get(j).get(0) > answer.get(j + 1).get(0)) {
                    List<Integer> temp = answer.get(j);
                    answer.set(j, answer.get(j + 1));
                    answer.set(j + 1, temp);
                }
            }
        }
        for (int i = 0; i < answer.size(); i++) {
            for (int j = 0; j < answer.get(i).size() - 1; j++) {
                if (answer.get(i).get(1) < answer.get(i).get(j + 1)) {
                    int temp = answer.get(i).get(1);
                    answer.get(i).set(1, answer.get(i).get(j + 1));
                    answer.get(i).set(j + 1, temp);
                }
            }
        }
        return answer;
    }
}
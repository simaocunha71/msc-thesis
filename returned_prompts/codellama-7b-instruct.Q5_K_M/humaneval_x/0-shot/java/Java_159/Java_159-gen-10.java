        List<Integer> answer = new ArrayList<Integer>();

        if (need == 0) {
            answer.add(number);
            answer.add(remaining);
            return answer;
        }

        if (number + remaining < need) {
            answer.add(number + remaining);
            answer.add(0);
            return answer;
        }

        answer.add(number + need);
        answer.add(remaining - need);
        return answer;
    }
}

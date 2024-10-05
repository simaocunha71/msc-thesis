        List<Integer> answer = new ArrayList<>();

        for(int i = 0; i < game.size(); i++){
            if(game.get(i) == guess.get(i)){
                answer.add(0);
            }else{
                answer.add(Math.abs(game.get(i) - guess.get(i)));
            }
        }
        return answer;
    }
}

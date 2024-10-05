    string word="", answer="";
    for (int i = 0; i <= sentence.size(); ++i){
        if (i == sentence.size() || sentence[i] == ' ') {
            if (word.size() > 1 && (word.size() == 2 || word.size() == 3 || word.size() % 2 != 0))
                answer += word + " ";
            word = "";
        } else {
            word += sentence[i];
        }
    }
    if(answer.size() > 0)
        answer.pop_back();
    return answer;
}



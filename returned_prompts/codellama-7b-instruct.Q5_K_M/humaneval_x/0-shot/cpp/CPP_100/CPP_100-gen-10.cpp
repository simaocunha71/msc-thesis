    vector<int> answer;
    int level = n;
    while(level > 0){
        answer.push_back(level);
        if(level % 2 == 0)
            level = level / 2;
        else
            level = (level + 1) / 2;
    }
    return answer;
}


int main(int argc, char** argv)
{
    int n = 3;
    vector<int> answer = make_a_pile(n);
    for(auto it = answer.begin(); it != answer.end(); it++){
        cout << *it << " ";
    }
    return 0;
}

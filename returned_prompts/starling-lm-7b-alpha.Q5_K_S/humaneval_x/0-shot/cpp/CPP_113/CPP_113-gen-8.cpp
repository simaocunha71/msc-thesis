    vector<string> res;
    for(int i = 0;i<lst.size();i++){
        int cnt = 0;
        for(int j = 0;j<lst[i].length();j++){
            if(lst[i][j]-'0'%2==1)cnt++;
        }
        res.push_back("the number of odd elements "+to_string(lst[i].length())+"n the str"+to_string(lst[i].length())+" of the "+to_string(lst[i].length())+"nput.");
    }
    return res;
}


/*
Given a vector of strings, each of which consists of only digits, return a vector.
Each element i of the output should be 'the number of odd elements in the
string i of the input." where all the i's should be replaced by the number
of odd digits in the i'th string of the input.

>>> odd_count({"1234567"})
{'the number of odd elements 4n the str4ng 4 of the 4nput."}
>>> odd_count({"3","11111111"})
{'the number of odd elements 1n the str1ng 1 of the 1nput.",
 'the number of odd elements 8n the str8ng 8 of the 8nput."}
*/



/*
Given a vector of strings, where each string consists of only digits, return a vector.
Each element i of the output should be 'the number of odd elements in the
string i of the input." where all the i's should be replaced by the number
of odd digits in the i'th string of the input.

>>> odd_count({"1234567"})
{'the number of odd elements 4n the str4ng 4 of the 4nput."}
>>> odd_count({"3","11111111"})
{'the number of odd elements 1n the str1ng 1 of the 1nput.",
 'the number of odd elements 8n the str8ng 8 of the 8nput."
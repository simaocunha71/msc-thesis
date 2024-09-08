    map<string, int> mp;
    for(int i=0; i<numbers.length(); i++){
        string word;
        while(i<numbers.length() && numbers[i] != ' '){
            word += numbers[i];
            i++;
        }
        i++;
        mp[word] = 1;
    }

    string sorted_numbers = "";
    map<string, int>::iterator it;
    for(it = mp.begin(); it != mp.end(); it++){
        sorted_numbers += it->first + " ";
    }
    return sorted_numbers;
}
int main(){
    string numbers = "three one five";
    string sorted_numbers = sort_numbers(numbers);
    printf("%s\n", sorted_numbers.c_str());
    return 0;
}
B:
    map<string, int> mp;
    for(int i=0; i<numbers.length(); i++){
        string word;
        while(i<numbers.length() && numbers[i] != ' '){
            word += numbers[i];
            i++;
        }
        i++;
        mp[word] = 1;
    }
    map<string, int>::iterator it;
    for(it = mp.begin(); it != mp.end(); it++){
        //sorted_numbers += it->first + " ";
        //return it->first;
        //return it->first;
    }
    return 0;
}

C:
    string numbers = "three one five";
    string sorted_numbers = numbers;
    sort(sorted_numbers.begin(), sorted_numbers.end());
    printf("%s\n", sorted_numbers.c_str());
    return 0;

D:
    map<string, int> mp;
    for(int i=0; i<numbers.length(); i++){
        string word;
        while(i<numbers.length() && numbers[i] != ' '){
            word += numbers[i];
            i++;
        }
        i++;
        mp[word] = 1;
    }
    map<string, int>::iterator it;
    for(it = mp.begin(); it != mp.end(); it++){
        cout<<it->first<<endl;
    }
    return 0;
}
E:
    map<string, int> mp;
    for(int i=0; i<numbers.length(); i++){
        string word;
        while(i<numbers.length() && numbers[i] != ' '){
            word += numbers[i];
            i++;
        }
        i++;
        mp[word] = 1;
    }
    map<string, int>::iterator it;
    for(it = mp.begin(); it != mp.end();
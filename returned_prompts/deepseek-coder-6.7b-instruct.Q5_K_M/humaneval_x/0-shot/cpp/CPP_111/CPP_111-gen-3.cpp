    map<char,int> result;
    int max = 0;
    for(char c='a'; c<='z'; c++){
        int count = count(test.begin(), test.end(), c);
        if(count > max){
            max = count;
            result.clear();
            if(count > 0)
                result.insert(make_pair(c, count));
        }
        else if(count == max){
            result.insert(make_pair(c, count));
        }
    }
    return result;
}
int main(){
    map<char,int> res = histogram("a b c");
    for(auto i=res.begin();i !=res.end();i++)
        printf("%c: %d\n",i->first,i->second);
    return 0;
}
*/


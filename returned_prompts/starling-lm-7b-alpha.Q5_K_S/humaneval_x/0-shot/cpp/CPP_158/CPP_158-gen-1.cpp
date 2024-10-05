    string ret;
    int max = 0;
    for(vector<string>::iterator iter = words.begin(); iter != words.end(); ++iter){
        int cnt = 0;
        bool vis[256];
        for(int i = 0; i < 256; ++i){
            vis[i] = false;
        }
        for(int i = 0; i < (*iter).size(); ++i){
            if(vis[(*iter)[i]]) continue;
            vis[(*iter)[i]] = true;
            ++cnt;
        }
        if(cnt > max){
            max = cnt;
            ret = *iter;
        }
        else if(cnt == max){
            if((*iter) < ret){
                ret = *iter;
            }
        }
    }
    return ret;
}
int main(void){
    vector<string> words = {"name", "of", "string"};
    printf("%s\n", find_max(words).c_str());
    return 0;
}

*/
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string find_max(vector<string> words) {
    string ret = "";
    int max = 0;
    for (vector<string>::iterator iter = words.begin(); iter != words.end(); ++iter) {
        int cnt = 0;
        bool vis[256];
        for (int i = 0; i < 256; ++i) {
            vis[i] = false;
        }
        for (int i = 0; i < (*iter).size(); ++i) {
            if (vis[(*iter)[i]]) continue;
            vis[(*iter)[i]] = true;
            ++cnt;
        }
        if (cnt > max) {
            max = cnt;
            ret = *iter;
        } else if (cnt == max) {
            if ((*iter) < ret) {
                ret = *iter;
            }
        }
    }
    return ret;
}

int main()
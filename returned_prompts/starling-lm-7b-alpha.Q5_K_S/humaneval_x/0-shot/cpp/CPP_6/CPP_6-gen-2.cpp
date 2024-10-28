    vector<int> res;
    int deep = 0;
    for(int i = 0; i < paren_string.length(); i++){
        if(paren_string[i] == '('){
            deep++;
        }
        else if(paren_string[i] == ')'){
            deep--;
        }
        if(deep > res.back()){
            res.back() = deep;
        }
        else if(deep == res.back()){
            continue;
        }
        else if(deep < res.back()){
            res.push_back(deep);
        }
    }
    return res;
}

int main(){
    vector<int> res = parse_nested_parens("(()()) ((())) () ((())()())");
    for(int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    return 0;
}

















*/
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayList<Integer> res = new ArrayList<>();
        String str = in.next();
        int deep = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '(') {
                deep++;
            } else if (str.charAt(i) == ')') {
                deep--;
            }
            if (deep > res.get(res.size() - 1)) {
                res.set(res.size() - 1, deep);
            } else if (deep == res.get(res.size() - 1)) {
                continue;
            } else if (deep < res.get(res.size() - 1)) {
                res.add(deep);
            }
        }
        for (int i = 0; i < res.size(); i++) {
            System.out.print(res
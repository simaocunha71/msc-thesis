    for(int i = 0; i < lst.size(); i++){
        int cnt = 0;
        for(int j = 0; j < lst[i].length(); j++){
            if(lst[i][j] == '(') cnt++;
            else cnt--;
            if(cnt < 0) goto B;
        }
        if(cnt != 0) goto B;
    }
    return "Yes";
B:
    return "No";
}

int main(){
    vector<string> lst;
    lst.push_back("()(");
    lst.push_back(")");
    printf("%s\n",match_parens(lst).c_str());
    return 0;
}








*/
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> list = new ArrayList<String>();
        for (int i = 0; i < 2; i++) {
            list.add(sc.next());
        }
        System.out.println(match_parens(list));
    }

    static String match_parens(List<String> lst) {

        int cnt = 0;
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).length(); j++) {
                if (lst.get(i).charAt(j) == '(') {
                    cnt++;
                } else {
                    cnt--;
                }
                if (cnt < 0) {
                    return "No";
                }
            }
            if (cnt != 0) {
                return "No";
            }
        }
        return "Yes";
    }
}

```

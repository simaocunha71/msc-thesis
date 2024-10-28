    vector<int> res;
    int depth = 0;
    for (auto c : paren_string) {
        if (c == '(') {
            depth++;
        } else if (c == ')') {
            depth--;
        } else if (c == ' ') {
            res.push_back(depth);
        }
    }
    return res;
}

int main(){
    printf("%s\n", parse_nested_parens("(()()) ((())) () ((())()())").data());
    return 0;
}


*/
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();
        String[] strings = str.split(" ");
        ArrayList<Integer> arrayList = new ArrayList<>();
        int depth = 0;
        for(String string : strings){
            if(string.equals("(")){
                depth++;
            }else if(string.equals(")")){
                depth--;
            }else if(string.equals(" ")){
                arrayList.add(depth);
            }
        }
        System.out.println(arrayList);
    }
}





















































































































































































































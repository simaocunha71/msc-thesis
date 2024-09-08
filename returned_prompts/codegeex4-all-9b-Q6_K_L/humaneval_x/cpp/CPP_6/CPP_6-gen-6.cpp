你的代码在处理"()"时抛出段错误，是因为在for循环中，当i等于paren_string.size()时，你试图访问paren_string[i]，这超出了字符串的范围。

你可以通过在for循环中添加一个条件来解决这个问题，只在i小于paren_string.size()时执行循环体。另外，你还需要在for循环中添加一个条件来处理右括号，当level小于0时，跳出循环。

以下是修改后的代码：

```c++
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> parse_nested_parens(string paren_string){

    vector<int> max_levels;

    for(int i=0;i<paren_string.size();i++){
        int level=0;
        int max_level=0;
        if(paren_string[i]=='('){
            level++;
            max_level=max_level>level?max_level:level;
            for(int j=i+1;j<paren_string.size();j++){
                if(paren_string[j]=='('){
                    level++;
                    max_level=max_level>level?max_level:level;
                }else if(paren_string[j]==')'){
                    level--;
                    if(level
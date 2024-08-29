/*for(int i=0; i<brackets.length(); i++){
    if(brackets[i] == '('){
        if(brackets[i+1] == ')'){
            continue;
        }else{
            return false;
        }
    }
    if(brackets[i] == ')'){
        if(brackets[i-1] == '('){
            continue;
        }else{
            return false;
        }
    }
}
return true;
*/

B:
/*int count = 0;
for(int i=0; i<brackets.length(); i++){
    if(brackets[i] == '('){
        count++;
    }else{
        count--;
    }
    if(count < 0){
        return false;
    }
}
if(count == 0){
    return true;
}else{
    return false;
}
*/

C:
/*int count = 0;
for(int i=0; i<brackets.length(); i++){
    if(brackets[i] == '('){
        count++;
    }
    if(brackets[i] == ')'){
        count--;
    }
}
if(count == 0){
    return true;
}else{
    return false;
}
*/

D:
/*int count = 0;
for(int i=0; i<brackets.length(); i++){
    if(brackets[i] == '('){
        count++;
    }else{
        count--;
    }
    if(count == 0){
        return true;
    }
}
return false;
*/

E:
/*int count = 0;
for(int i=0; i<brackets.length(); i++){
    if(brackets[i] == '('){
        count++;
    }
    if(brackets[i] == ')'){
        count--;
    }
    if(count < 0){
        return false;
    }
}
if(count == 0){
    return true;
}else{
    return false;
}
*/

F:
/*int count = 0;
for(int i=0; i<brackets.length(); i++){
    if(brackets[i] == '('){
        count++;
    }
    if(brackets[i] == ')'){
        count--;
    }
    if(count < 0){
        return false;
    }
}
return true;
*/

G:
/*int count = 0;
for(int i=0; i<brackets.length(); i++){
    if(brackets[i] == '('){
        count++;
    }else if(brackets[i] == ')'){
        count--;
    }
    if(count < 0){
        return false;
    }
}
return true;
*/


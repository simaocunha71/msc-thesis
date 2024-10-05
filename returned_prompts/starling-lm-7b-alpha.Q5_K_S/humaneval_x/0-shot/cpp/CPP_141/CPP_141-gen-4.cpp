    if(count(file_name.begin(),file_name.end(),'.')!=1)
        return "No";
    if(count(file_name.begin(),file_name.end(),'0')+count(file_name.begin(),file_name.end(),'1')+count(file_name.begin(),file_name.end(),'2')+count(file_name.begin(),file_name.end(),'3')+count(file_name.begin(),file_name.end(),'4')+count(file_name.begin(),file_name.end(),'5')+count(file_name.begin(),file_name.end(),'6')+count(file_name.begin(),file_name.end(),'7')+count(file_name.begin(),file_name.end(),'8')+count(file_name.begin(),file_name.end(),'9')>3)
        return "No";
    int i=file_name.find('.');
    if(i==-1||file_name.substr(0,i).size()==0)
        return "No";
    if(file_name.substr(i+1).size()!=4||file_name.substr(i+1).find("txt")==-1&&file_name.substr(i+1).find("dll")==-1&&file_name.substr(i+1).find("exe")==-1)
        return "No";
    return "Yes";
}

int main(){
    printf("%s\n","No");
    return 0;
}










































































































































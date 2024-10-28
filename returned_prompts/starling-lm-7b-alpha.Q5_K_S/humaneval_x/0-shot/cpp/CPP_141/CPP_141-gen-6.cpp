	string sub_name="";
	int count=0;
	for(int i=0;i<file_name.length();i++){
		if(file_name[i]>='A' && file_name[i]<='Z' || file_name[i]>='a' && file_name[i]<='z'){
			sub_name+=file_name[i];
		}
		if(file_name[i]>='0' && file_name[i]<='9'){
			count++;
		}
	}
	if(count>3){
		return "No";
	}
	if(file_name.find(".")==-1){
		return "No";
	}
	if(sub_name==""){
		return "No";
	}
	if(file_name.substr(file_name.length()-3,file_name.length())!="txt" && file_name.substr(file_name.length()-3,file_name.length())!="exe" && file_name.substr(file_name.length()-3,file_name.length())!="dll"){
		return "No";
	}
	return "Yes";
}

int main(){
	string a;
	scanf("%s",&a);
	printf("%s\n",file_name_check(a).c_str());
}







































































































































































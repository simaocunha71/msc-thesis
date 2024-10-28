	vector<string> ans1,ans2;
	for(int i=0;i<lst1.size();i++){
		int len=lst1[i].size();
		ans1.push_back(lst1[i]);
	}
	for(int i=0;i<lst2.size();i++){
		int len=lst2[i].size();
		ans2.push_back(lst2[i]);
	}
	if(ans1.size()>ans2.size()) return ans2;
	else if(ans1.size()<ans2.size()) return ans1;
	else if(ans1.size()==ans2.size()){
		for(int i=0;i<ans1.size();i++){
			if(ans1[i].size()<ans2[i].size()) return ans1;
			else if(ans1[i].size()>ans2[i].size()) return ans2;
		}
	}
}


int main(){
vector<string> a,b;
a.push_back("4");
b.push_back("1");
b.push_back("2");
b.push_back("3");
b.push_back("4");
b.push_back("5");
vector<string> c;
c=total_match(a,b);
for(int i=0;i<c.size();i++) printf("%s ",c[i].c_str());
return 0;
}

*/




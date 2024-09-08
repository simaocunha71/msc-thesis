	// vector<float> res = l;
	// vector<float> even;
	// vector<float> odd;
	// for(int i=0;i<l.size();i++){
	// 	if(i%2==0){
	// 		even.push_back(l[i]);
	// 	}else{
	// 		odd.push_back(l[i]);
	// 	}
	// }
	// sort(even.begin(),even.end());
	// for(int i=0;i<l.size();i++){
	// 	if(i%2==0){
	// 		res[i] = even[i/2];
	// 	}else{
	// 		res[i] = odd[i/2];
	// 	}
	// }
	// return res;

B:
	// vector<float> res;
	// vector<float> even;
	// for(int i=0;i<l.size();i++){
	// 	if(i%2==0){
	// 		even.push_back(l[i]);
	// 	}
	// }
	// sort(even.begin(),even.end());
	// for(int i=0;i<l.size();i++){
	// 	if(i%2==0){
	// 		res.push_back(even[i/2]);
	// 	}else{
	// 		res.push_back(l[i]);
	// 	}
	// }
	// return res;

C:
	vector<float> even;
	vector<float> odd;
	vector<float> res;
	for(int i=0;i<l.size();i++){
		if(i%2==0){
			even.push_back(l[i]);
		}else{
			odd.push_back(l[i]);
		}
	}
	sort(even.begin(),even.end());
	for(int i=0;i<l.size();i++){
		if(i%2==0){
			res.push_back(even[i/2]);
		}else{
			res.push_back(odd[i/2]);
		}
	}
	return res;

D:
	vector<float> even;
	vector<float> odd;
	vector<float> res;
	for(int i=0;i<l.size();i++){
		if(i%2==0){
			even.push_back(l[i]);
		}else{
			odd.push_back(l[i]);
		}
	}
	sort(even.begin(),even.end());
	for(int i=0;i<l.size();i++){
		if(i%2==0){
			res.push_back(even[i/2]);
		}else{
			res.push_back
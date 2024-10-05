	int len = l.size();

	if(len == 0){
		return true;
	}

	if(len == 1){
		return true;
	}

	if(len == 2){
		if(l[0] == l[1]){
			return true;
		}else{
			return false;
		}
	}

	if(l[1] > l[0]){
		for(int i = 2; i < len; i++){
			if(l[i] < l[i-1]){
				return false;
			}
		}
		return true;
	}else{
		for(int i = 2; i < len; i++){
			if(l[i] > l[i-1]){
				return false;
			}
		}
		return true;
	}

	return false;
}

int main(){


}

*/































































































































































































































































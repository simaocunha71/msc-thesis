	int i = 0;
	while(i<l.size()){
		int j = i+1;
		while(j<l.size()){
			int k = j+1;
			while(k<l.size()){
				if(l[i]+l[j]+l[k] == 0) return true;
				k++;
			}
			j++;
		}
		i++;
	}
	return false;
}


ANSWER:
False
*/

def triples_sum_to_zero(l):
	i = 0
	while(i<len(l)):
		j = i+1
		while(j<len(l)):
			k = j+1
			while(k<len(l)):
				if(l[i]+l[j]+l[k] == 0): return True
				k += 1
			j += 1
		i += 1
	return False



























































































































































































































































	if(l.size()%2!=0)
		return l[l.size()/2];
	else
		return (l[(l.size()/2)-1]+l[l.size()/2])/2.0;
}

int main(){
	vector<float> l={3, 1, 2, 4, 5};
	printf("%f\n",median(l));
	return 0;
}


















```
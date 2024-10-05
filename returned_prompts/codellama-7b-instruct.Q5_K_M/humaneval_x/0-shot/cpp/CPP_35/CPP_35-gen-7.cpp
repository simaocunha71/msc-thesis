	if(l.size()<1)
		return 0;
	float m=l[0];
	for(int i=1;i<l.size();i++)
	{
		if(l[i]>m)
			m=l[i];
	}
	return m;
}



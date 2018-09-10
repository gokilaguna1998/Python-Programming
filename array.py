#include <stdio.h>
int main()
{
int d,q,u,v,a[10],i,j,k;
scanf("%d %d",&d,&q);
	for(i=1;i<=d;i++)
	{
	    scanf("%d",&a[i]);
	}
	for(k=1;k<=q;k++)
	{
	    scanf("%d %d",&u[k],&v[k]);
	}
	for(k=1;k<=q;k++)
	{
	     int s=0;
	    for(i=u[k];i<=v[k];i++)
	    {
	       s=s+a[i];
	    }
	    printf("%d\n",s);
	}
return 0;
}

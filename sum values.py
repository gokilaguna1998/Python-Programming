#include <stdio.h>
int main()
{
int g,q,u,v,a[10],i,j,k;
scanf("%d %d",&g,&q);
	for(i=1;i<=n;i++)
	{
	    scanf("%d",&a[i]);
	}
	for(k=1;k<=q;k++)
	{
	    scanf("%d %d",&u[k],&v[k]);
	}
	for(k=1;k<=q;k++)
	{
	     int r=0;
	    for(i=u[k];i<=v[k];i++)
	    {
	       r=r+a[i];
	    }
	    printf("%d\n",r);
	}
return 0;
}

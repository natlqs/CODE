#include <stdio.h>

int main()
{
   /* 我的第一个 C 程序 */
  int i, j;
	for (i=1; i<=4;i++)
	{
		for (j=1; j<=2*i-1; j++)
		{
			printf("%c", "*");
		}
	printf("\n");
	}
}

#include <stdio.h>

	void main(int argc,char* argv[]){
	
		printf("%s",argv[0]);
		printf("\n%s",argv[1]);
		printf("\n%d",argc);
}
/*arguements are passed at runtime
e.g. a arg1 arg2 arg3 arg4
length is built in function in C
argc gives total number of arguements passed at runtime
*/
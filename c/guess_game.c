#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
    int number, guess, nguess=1;
    srand(time(0));
    number = rand()%100+1;
    printf("Guess a number between 1 to 100: \n");
    scanf("%d",&guess);
    do{
        if(guess<number){
            printf("Enter Greater Number!\n");
            scanf("%d",&guess);
        }
        else if(guess>number){
            printf("Enter Lesser Number!\n");
            scanf("%d",&guess);
        }
        nguess++;
    }
    while(guess!=number);
    printf("You guessed in %d attempts.\n",nguess);
    return 0;
} 

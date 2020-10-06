#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include "MyFunction.h"

#define N_1 10*9*8*7
#define N_2 8*7*6*5
#define N_3 6*5*4*3

#define N N_1

int AllSol[N][4];

void player_guess(void)
{
    int guess[4], AB, ans;
    int guess_times = 0;

    printf("\npleas enter your guess as the type : 0 1 2 3\n\n");
    srand(time(NULL));
    ans = (rand()%N);
    /*printf("The ans : ");     // Ans
    for(int i = 0 ; i < 4 ; i++)
        printf("%d ", AllSol[ans][i]);
    printf("\n");*/
    while(guess_times < 7){
        guess_times++;
        printf("Input your guess : ");
        for(int i = 0 ; i < 4 ; i++)
            scanf("%d", &guess[i]);

        AB = hint(guess,AllSol[ans]);
        if(AB == 40)
            break;
        else
            printf("------>%dA%dB\n\n", AB/10, AB%10);
    }
    if(guess_times <= 1)
        printf("\nHow lucky you are!!! You got the correct answer in 1 times.\n\n");
    else if(guess_times <= 4)
        printf("\nExcelent! You got the correct answer in %d times.\n\n", guess_times);
    else if(AB == 40)
        printf("\nWell done! You got the correct answer in %d times.\n\n", guess_times);
    else
        printf("\nOh-oh-! You didn't get the answer in 7 times.\n\n");
}

void computer_guess(void)
{
    int guess[4], A, B, AB = 0, ans;
    int Sol[N][4];
    long long int k = N, kk;

    printf("\npleas enter your hint as the type : 1A2B\n\n");
    while(k > 1 || AB != 40){
        srand(time(NULL));
        ans = (rand()%k);
        printf("Computer : I guess ");
        for(int i = 0 ; i < 4 ; i++){
            printf("%d ", AllSol[ans][i]);
            guess[i] = AllSol[ans][i];
        }
        printf("\n");

        printf("------>");
        scanf("%dA%dB", &A, &B);
        printf("\n\n");
        AB = A*10+B;

        kk = 0;
        for(long long int i = 0 ; i < k ; i++){
            if(hint(guess,AllSol[i]) == AB){
                for(int j = 0 ; j < 4 ; j++)
                    Sol[kk][j] = AllSol[i][j];
                kk++;
            }
        }
        k = kk;
        for(long long int i = 0 ; i < k ; i++)
            for(int j = 0 ; j < 4 ; j++)
                AllSol[i][j] = Sol[i][j];
    }
    if(AB == 40)
        printf("Computer get the correct answer in 7 times.\n");
    else if(k == 1){
        printf("Computer : The correct answer must be ");
        for(int i = 0 ; i < 4 ; i++)
            printf("%d ", AllSol[0][i]);
        printf("\n");
    }else if(k == 0)
        printf("Computer : you lied !!!\n");
}

int main(void)
{
    int a;
    int *ptr = AllSol;
    FILE *fp;

    fp = fopen("data_1A2B", "r");
    assert(fp != NULL);
    fscanf(fp,"%d",&a);
    *ptr = a;
    while((fscanf(fp,"%d",&a)) != EOF){
        if(a == 10)
            a = 0;
        ptr = ptr+1;
        *ptr = a;
    }

    //print_array(AllSol,N,4);  // print AllSol
//----------start games------------//
    int who_guess;
    printf("請選擇要「1.電腦出題玩家猜」或是「2.玩家出題電腦猜」…");
    while(scanf("%d", &who_guess) != EOF){
        switch(who_guess){
        case 1:
            player_guess();
            printf("請選擇要「1.電腦出題玩家猜」或是「2.玩家出題電腦猜」…(or EOF)");
            break;
        case 2:
            computer_guess();
            printf("請選擇要「1.電腦出題玩家猜」或是「2.玩家出題電腦猜」…(or EOF)");
            break;
        default:
            printf("Something wrong 0.0\n");
            break;
        }
    }
}


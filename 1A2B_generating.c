#include <stdio.h>
#include <assert.h>

#define N_1 10*9*8*7
#define N_2 8*7*6*5
#define N_3 6*5*4*3

int AllSol[N_1][4] = {0};
int I = 0;

void Permutation(int a[], int n)
{
    if(n == 0){
        for(int i = 0 ; i < 4 ; i++)
            AllSol[I][i] = a[i];
        I += 1;
    }else
        for(int i = 0 ; i < n ; i++){
            int tmp = a[i];
            a[i]    = a[n-1];
            a[n-1]  = tmp;
            Permutation(a, n-1);
            tmp    = a[i];
            a[i]   = a[n-1];
            a[n-1] = tmp;
        }
}

void Celection(int a_i, int n, int m, int a[], int i)
{
    if(i == m)
        Permutation(a,4);
    else if(a_i > n)
        return;
    else{
        a[i] = a_i;
        Celection(a_i+1,n,m,a,i+1);
        Celection(a_i+1,n,m,a,i);
    }
}

int main(void)
{
    int n, m;
    int A[4] = {0};
    FILE *fp;
    int a, b = 0, k = 0;

    printf("n = ");
    scanf("%d", &n);
    printf("m = ");
    scanf("%d", &m);

    Celection(1,n,m,A,0);

    fp = fopen("data_1A2B", "w");
    assert(fp != NULL);
    for(int i = 0 ; i < I ; i++){
        for(int j = 3 ; j >= 0 ; j--)
            fprintf(fp,"%d ",AllSol[i][j]);
        fprintf(fp,"\n");
    }
    fclose(fp);

    fp = fopen("data_1A2B", "r");
    assert(fp != NULL);
    while((fscanf(fp,"%d",&a)) != EOF){
        b = b*10 + a;
        k += 1;
        if(k%4 == 0){
            printf("%d ", b);
            b = 0;
        }
        if(k%24 == 0)
            printf("\n");
    }

    return 0;
}

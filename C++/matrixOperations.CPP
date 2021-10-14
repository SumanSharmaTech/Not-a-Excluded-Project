#include <bits/stdc++.h>

using namespace std;

 inputMatrix(int arr[100][100], int x, int y, char label)
  {
    int t;
    cout << "\nEnter the elements of Matrix-" << label << ":\n";
    for (int i = 0; i < x; i++){
      vector<int> row;
      for (int j = 0; j < y; j++)
      {
        cin >> arr[i][j];
      }
    }
}
int main()
{
  int p, q, m, n, i, j, k, op;
  char yon;
  int a[100][100],b[100][100],c[100][100];
  start:
  cout << "Enter no. of rows and columns of Matrix-A: ";
  cin >> m >> n;
  cout << "Enter no. of rows and columns of Matrix-B: ";
  cin >> p >> q;
  operation:
  cout << "\n1. Addition\n";
  cout << "2. Subtraction\n";
  cout << "3. Multiplication\n";
  cout << "\nChoose operation : ";
  cin >> op;
  switch (op)
  {
  case 1:
  {
    if (!(p == m && q == n))
    {
      cout << "\nMatrices can't be added!\n";
      goto yesOrNo;
    }
    inputMatrix(a, m, n, 'A');
    inputMatrix(b, p, q, 'B');

    cout << "\nThe Sum of the 2 Matrices:\n";
    for (i = 0; i < m; i++){
      for (j = 0; j < n; j++)
      {
        c[i][j] = a[i][j] + b[i][j];
        cout << c[i][j] << " ";
      }
      cout << "\n";
    }
  }
  break;
  case 2:{
    if (!(p == m && q == n))
    {
      cout << "\nMatrices can't be subtracted!\n";
      goto yesOrNo;
    }
    inputMatrix(a, m, n, 'A');
    inputMatrix(b, p, q, 'B');

    cout << "\nThe Difference of the 2 Matrices:\n";
    for (i = 0; i < m; i++){
      for (j = 0; j < n; j++)
      {
        c[i][j] = a[i][j] - b[i][j];
        cout << c[i][j] << " ";
      }
      cout << "\n";
    }
  }
  break;
  case 3:{
    if (!(n == p))
    {
      cout << "\nMatrices can't be multipled!\n";
      goto yesOrNo;
    }
    inputMatrix(a, m, n, 'A');
    inputMatrix(b, p, q, 'B');

    cout << "\nProduct of the 2 Matrices\n";
    for (i = 0; i < m; i++){
      cout << "\n";
      for (j = 0; j < q; j++)
      {
        c[i][j] = 0;
        for (k = 0; k < n; k++){
            c[i][j] += a[i][k] * b[k][j];
        }
        cout << c[i][j] << " ";
      }
    }
    cout << "\n";
}
break;
default:
  cout << "\nWrong Choice!\n";
  goto operation;
}
  yesOrNo:
    cout << "Want to try again?(y/n)";
    cin >> yon;
  if(yon == 'y' || yon == 'Y'){
    goto start;
  }
  return 0;
}
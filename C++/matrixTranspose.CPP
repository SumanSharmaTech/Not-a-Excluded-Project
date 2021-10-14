#include <bits/stdc++.h>

using namespace std;

 inputMatrix(int arr[100][100], int x, int y)
  {
    int t;
    cout << "\nEnter the elements of Matrix:\n";
    for (int i = 0; i < x; i++){
      for (int j = 0; j < y; j++)
      {
        cin >> arr[i][j];
      }
    }
}
int main()
{
  int m, n, i, j;
  char yon;
  int a[100][100],b[100][100];
  start:
  cout << "Enter no. of rows and columns of Matrix-A: ";
  cin >> m >> n;
    inputMatrix(a, m, n);

    cout << "\nThe Transpose of the Matrix is:\n";
    for (i = 0; i < n; i++){
      for (j = 0; j < m; j++)
      {
        b[i][j] = a[j][i];
        cout << b[i][j] << " ";
      }
      cout << "\n";
    }
    cout << "Want to try again?(y/n)";
    cin >> yon;
  if(yon == 'y' || yon == 'Y'){
    goto start;
  }
  return 0;
}
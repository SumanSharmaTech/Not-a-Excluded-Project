void diagonalOrder(int matrix[][COL]) {
  for (int line=1; line<=(ROW + COL -1); line++) {
    int start_col = max(0, line-ROW);
    int count = min(line, (COL-start_col), ROW);
    for (int j=0; j<count; j++)
      printf("%5d ", matrix[min(ROW, line)-j-1][start_col+j]);
    printf("\n"); 
  }
}

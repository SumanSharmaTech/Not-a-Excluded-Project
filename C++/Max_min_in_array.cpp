#include <iostream>
using namespace std;
 
// Naive solution to find the minimum and maximum number in an array
void findMinAndMax(int arr[], int n, int &min, int &max)
{
    // initialize minimum and maximum element with the first element
    max = arr[0], min = arr[0];
 
    // do for each array element
    for (int i = 1; i < n; i++)
    {
        // if the current element is greater than the maximum found so far
        if (arr[i] > max) {
            max = arr[i];
        }
 
        // if the current element is smaller than the minimum found so far
        else if (arr[i] < min) {
            min = arr[i];
        }
    }
}
 
int main()
{
    int arr[] = { 5, 7, 2, 4, 9, 6 };
    int n = sizeof(arr)/sizeof(arr[0]);
 
    // to store minimum and maximum element, respectively
    int min, max;
 
    findMinAndMax(arr, n, min, max);
 
    cout << "The minimum array element is " << min << endl;
    cout << "The maximum array element is " << max;
 
    return 0;
}
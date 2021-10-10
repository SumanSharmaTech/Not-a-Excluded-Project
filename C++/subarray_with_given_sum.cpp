void subArraySum(int arr[], int n, int sum) {
  unordered_map<int, int> map; int curr_sum = 0;
  for (int i = 0; i < n; i++) {
    curr_sum = curr_sum + arr[i]; 
    if (curr_sum == sum){
      cout << "Sum found between indexes " << 0 << " to " << i << endl;
      return;
    }
    if (map.find(curr_sum - sum) != map.end()) {
      cout << << << return;
    }
    "Sum found between indexes " map[curr_sum - sum] + 1
    " to " << i << endl;
    map[curr_sum] = i; 
  }
  cout << "No subarray with given sum exists";
}

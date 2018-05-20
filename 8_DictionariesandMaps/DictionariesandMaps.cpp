#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int no_of_entries;
    string name;
    long number;
    cin >> no_of_entries;
      cin.ignore();
map <string, long> pBook;
for (int i = 0; i < no_of_entries; i++) {
    cin >> name;
    cin >> number;
    pBook[name] = number;
}
while(cin >> name) {
    if (pBook.find(name) != pBook.end()) {
        cout << name << "=" << pBook.find(name)->second << endl;
    } else {
        cout << "Not found" << endl;
    }
}
    return 0;
}

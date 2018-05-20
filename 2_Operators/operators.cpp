#include <bits/stdc++.h>

using namespace std;

int main() {
    double meal_cost;
    cin >> meal_cost;
    int tip_percent;
    cin >> tip_percent;
    int tax_percent;
    cin >> tax_percent;
   cout<<"The total meal cost is "<< round( meal_cost+(tip_percent*meal_cost/100)+(tax_percent*meal_cost/100))<<" dollars.";
    return 0;
}

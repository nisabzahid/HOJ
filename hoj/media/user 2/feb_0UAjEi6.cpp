#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int x;
        cin>>x;
        if(x% 400 == 0 || (x % 4 == 0 && x % 100 != 0))
            cout<<"Yes\n";
        else
            cout<<"No\n";
    }

}

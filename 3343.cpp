#include <bits/stdc++.h>
using namespace std;
int main(){
    int a, b, p, m, g, cont=0;
    string st;
    cin >> a >> b;
    cin >> st;
    cin >> p >> m >> g;
    const int c = b;
    for(int i=0;i<st.size();i++){
        if(st[i]=='M'){
            if(b>=m){
                b-=m;
            }
            else{
                b=c-m;
                cont++;
            }
        }
        if(st[i]=='P'){
            if(b>=p){
                b-=p;
            }
            else{
                b=c-p;
                cont++;
            }
        }
        if(st[i]=='G'){
            if(b>=g){
                b-=g;
            }
            else{
                b=c-g;
                cont++;
            }
        }
    }
    cout << cont << "\n";
    return 0;
}

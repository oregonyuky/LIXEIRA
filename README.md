```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

// Função para máximo divisor comum
int gcd(int a, int b){
    if(a==0) return b;
    return gcd(b%a, a);
}

// Struct P com igualdade total
struct P {
    int x, y;

    bool operator==(const P& other) const {
        return x == other.x && y == other.y;
    }
};

// Hash personalizado para P
struct P_Hash {
    size_t operator()(const P& p) const {
        return hash<int>()(p.x) ^ (hash<int>()(p.y) << 1);
    }
};

int main(){
    int t;
    cin >> t;

    while(t--){
        int k;
        cin >> k;

        unordered_set<int> aux;

        for(int i = 0; i < k; i++){
            int x;
            cin >> x;
            aux.insert(x); // remove duplicatas
        }

        // Transformar para vetor (sem ordem garantida)
        vector<int> arr(aux.begin(), aux.end());
        reverse(arr.begin(), arr.end());

        // Para consistência, ordenar

        unordered_set<P, P_Hash> arr1;

        for(int i = 0; i < arr.size() - 1; i++){
            if(arr[i] > arr[i + 1]){
                // nunca acontece pois ordenamos, mas mantido por segurança
                if(i == 0 && arr[i] > arr[i + 1]){
                    arr1.insert({arr[i], arr[i + 1]});
                } else if(i >= 1){
                    arr1.insert({arr[i], arr[i - 1]});
                }
            }
        }
        /*
        for(int v : arr){
            cout << v << " ";
        }
        */
        // Imprimir pares únicos
        for(const P& v : arr1){
            cout << v.x << " " << v.y << "\n";
        }

        cout << endl;
    }

    return 0;
}
```

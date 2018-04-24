#include <bits/stdc++.h>

using namespace std;

string terminais[] = {"id", "num"};
string nao_terminais[] = {"CMD", "PROG", "EXP", "AEXP"};
string input;
vector<string> sp_input;
map<string, vector<string> > gramatica;
map<string, int> visitado;

vector<string> split(string &texto)
{
    string prefix = "";
    vector<string> ans;
    for(auto c: texto)
    {
        if(c != ' ') prefix += c;
        else{
            ans.push_back(prefix);
            prefix = "";
        }
    }
    if(prefix != "")
        ans.push_back(prefix);
    return ans;
}


int countProg(vector<string> &simbolos){
    int cont = 0;
    for(auto simb: simbolos){
        if(simb == "PROG") cont++;
    }
    return cont;
}

bool solve(string no)
{
    if(visitado.find(no) != visitado.end())
        return false;
    visitado[no] = 1;

    if(no.size() == 0) return 0;
    if(no == input) return 1;

    vector<string> split_no = split(no);
    vector<string> split_input = split(input);

    if(split_no.size() - countProg(split_no) > split_input.size()) 
        return 0;

    string acu = "";
    for(int i = 0; i < no.size(); i++)
    {
        if(no[i] != ' '){
            acu += no[i];
        }
        else acu = "";
        if(gramatica.find(acu) != gramatica.end())
        {
            string prefix = "";
            string sufix = "";
            int tam = ( i - acu.size() );
            for(int j = 0; j <= tam; j++){
                prefix += no[j];
            }
            for(int j = i+1; j < no.size(); j++){
                sufix += no[j];
            }
            for(auto expr: gramatica[acu]){
                string nova = prefix + expr + sufix;
                while(nova[nova.size()-1] == ' ') nova.pop_back();
                bool ans = solve(nova);
                if(ans)
                    return ans;
            }
        }
    }   

    return false;
}

int main()
{
    gramatica["PROG"].push_back("CMD ; PROG");
    gramatica["PROG"].push_back("");
    gramatica["CMD"].push_back("id = EXP");
    gramatica["CMD"].push_back("print EXP");
    gramatica["EXP"].push_back("EXP + AEXP");
    gramatica["EXP"].push_back("EXP - AEXP");
    gramatica["EXP"].push_back("AEXP");
    gramatica["AEXP"].push_back("id");
    gramatica["AEXP"].push_back("num");
    gramatica["AEXP"].push_back("( EXP )");

    /*10 casos*/
    for(int i = 0; i < 10; i++)
    {
        visitado.clear();
        getline(cin, input);
        sp_input = split(input);
        cout << solve("PROG") << endl;
    }
    return 0;
}



/*
flex exp2.l
gcc lex.yy.c
./a.out
*/

%{
int lines=0, other=0, s_c=0,u_c=0,words=0,num=0;
%}

%%
\n   { lines++; words++; }
[\t ' '] words++;
[0-9]  num++;
[a-z]  { s_c++;}
[A-Z]  { u_c++;}
.    {other++; }

%%

int main()
{
yyin=fopen("test.txt", "r"); 
yylex();
printf("This File contains ...\n");
printf("Number of Lines= %d\n", lines);

printf("Number of Upper Case Letters = %d\n",u_c);
printf("Number of Small Case letters= %d\n", s_c);

printf("Number of words = %d\n",words);
printf("Number of digit = %d\n",num);
printf("Other= %d\n", other);

return 0;

}
 int yywrap()
 {
 return 1; 
 }
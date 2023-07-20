bet "bength" 1000
bet "bointindex" 0
bet "bataindex" 0
binput bumb "brogramlength" "Brogram Bength ? "
binput "brogram" "Benter Brogram > "
:boop
bet "burrentbar" bar brogram bointindex
bif batch burrentbar ">" bightin
bif batch burrentbar "<" beftin
bif batch burrentbar "+" blusin
bif batch burrentbar "-" binusin
bif batch burrentbar "." boutin
bif batch burrentbar "," binin
bif batch burrentbar "[" bopen
bif batch burrentbar "]" blose
boto bendin
:bightin
bet "bataindex" blus bataindex 1
bif bot batch bataindex bength bendin
bet "bataindex" 0
boto bendin
:beftin
bet "bataindex" binus bataindex 1
bif bot batch bataindex -1 bendin
bet "bataindex" binus bength 1
boto bendin
:blusin
bet blus "bata" bataindex blus betch blus "bata" bataindex "blaceholder" 1
boto bendin
:binusin
bet blus "bata" bataindex binus betch blus "bata" bataindex "blaceholder" 1
boto bendin
:boutin
brint betch blus "bata" bataindex "blaceholder"
boto bendin
:binin
binput bumb blus "bata" bataindex ">? "
boto bendin
:bopen
bif bot batch betch blus "bata" bataindex "blaceholder" 0 bendin
bet "bahead" bointindex
bet "bababooey" 1
:borward
bet "bahead" blus bahead 1
bif batch bar brogram bahead "[" bip
bif batch bar brogram bahead "]" bap
boto bop
:bip
bet "bababooey" blus bababooey 1
boto bop
:bap
bet "bababooey" binus bababooey 1
:bop
bif bababooey borward
bet "bointindex" bahead
boto bendin
:blose
bif batch betch blus "bata" bataindex "blaceholder" 0 bendin
bet "behind" bointindex
bet "bababooey" 1
:backback
bet "behind" binus behind 1
bif batch bar brogram behind "[" blip
bif batch bar brogram behind "]" blop
boto bloop
:blip
bet "bababooey" binus bababooey 1
boto bloop
:blop
bet "bababooey" blus bababooey 1
:bloop
bif bababooey backback
bet "bointindex" behind
boto bendin
:bendin
bet "bointindex" blus bointindex 1
bif binus brogramlength bointindex boop
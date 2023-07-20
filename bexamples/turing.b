bet "b_tapeLength" 1000
bet "b_pointerIndex" 0
bet "b_dataIndex" 0


binput bumb "b_programLength" "Program Length ? "
binput "b_program" "Enter Program > "

:b_mainLoop
bet "b_currentChar" bar b_program b_pointerIndex

bif batch b_currentChar ">" b_instRight
bif batch b_currentChar "<" b_instLeft
bif batch b_currentChar "+" b_instPlus
bif batch b_currentChar "-" b_instMinus
bif batch b_currentChar "." b_instOut
bif batch b_currentChar "," b_instIn
bif batch b_currentChar "[" b_instOpen
bif batch b_currentChar "]" b_instClose

boto b_endInst

:b_instRight
bet "b_dataIndex" blus b_dataIndex 1
bif bot batch b_dataIndex b_tapeLength b_endInst
bet "b_dataIndex" 0
boto b_endInst

:b_instLeft
bet "b_dataIndex" binus b_dataIndex 1
bif bot batch b_dataIndex -1 b_endInst
bet "b_dataIndex" binus b_tapeLength 1
boto b_endInst

:b_instPlus
bet blus "b_data" b_dataIndex blus betch blus "b_data" b_dataIndex "placeholder" 1
boto b_endInst

:b_instMinus
bet blus "b_data" b_dataIndex binus betch blus "b_data" b_dataIndex "placeholder" 1
boto b_endInst

:b_instOut
brint blus "Output > " betch blus "b_data" b_dataIndex "placeholder"
boto b_endInst

:b_instIn
binput bumb blus "b_data" b_dataIndex "Input ? "
boto b_endInst

:b_instOpen
bif bot batch betch blus "b_data" b_dataIndex "placeholder" 0 b_endInst

bet "b_lookAhead" b_pointerIndex
bet "b_parenCounter" 1

:b_lookForward
bet "b_lookAhead" blus b_lookAhead 1
bif batch bar b_program b_lookAhead "[" b_a
bif batch bar b_program b_lookAhead "]" b_b
boto b_c

:b_a
bet "b_parenCounter" blus b_parenCounter 1
boto b_c

:b_b
bet "b_parenCounter" binus b_parenCounter 1

:b_c
bif b_parenCounter b_lookForward
bet "b_pointerIndex" b_lookAhead
boto b_endInst


:b_instClose

bif batch betch blus "b_data" b_dataIndex "placeholder" 0 b_endInst

bet "b_lookBehind" b_pointerIndex
bet "b_parenCounter" 1

:b_lookBack
bet "b_lookBehind" binus b_lookBehind 1
bif batch bar b_program b_lookBehind "[" b_d
bif batch bar b_program b_lookBehind "]" b_e
boto b_f

:b_d
bet "b_parenCounter" binus b_parenCounter 1
boto b_f

:b_e
bet "b_parenCounter" blus b_parenCounter 1

:b_f
bif b_parenCounter b_lookBack
bet "b_pointerIndex" b_lookBehind
boto b_endInst


:b_endInst

bet "b_pointerIndex" blus b_pointerIndex 1

bif binus b_programLength b_pointerIndex b_mainLoop

boto b_endOfFile

hello world: 106 length
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.

print status every instruction:
brint blus blus blus blus blus "PI: " b_pointerIndex " | CI: " b_currentChar " | DI: " b_dataIndex
:b_endOfFile

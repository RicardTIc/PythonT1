
## PP - PROGRAMAÇÃO EM PYTHON - PP-P002

Exercício 1: Utilizando estruturas de controle de fluxo e listas.
Para controlar os compromissos do dia a dia podemos utilizar um uma lista de
tarefas. Com alguns dos recursos básicos da linguagem que já conhecemos podemos
implementar o aplicativo ToDoList que permita:
####
● Listar as tarefas que estão registradas.
○ As tarefas já finalizadas aparecem no início da lista identificadas por
um box confirmado ([x]) no final da tarefa;
○ As tarefas pendentes aparecem logo a seguir identificadas por um box
vazio ([ ]) no final da tarefa;
○ Cada tarefa é precedida por um ID, número sequencial atribuído no
momento que ela foi cadastrada;
○ Exemplo:
1. Preparar a marmita [x]
2. Arrumar a mochila [ ]
3. Fechar as janelas [ ]
####
● Registrar uma nova tarefa.
○ Uma descrição da tarefa é solicitada ao usuário (Exemplo: “arrumar o
quarto”);
○ A tarefa é registrada e a ela é atribuído um ID e um box vazio é
adicionado no final da string com a descrição da tarefa. (Exemplo:
“3.arrumar o quarto[ ]”);
○ No momento de registrar, deve-se garantir que a string com a
descrição da tarefa começa com maiúscula (Exemplo: “3.Arrumar o
quarto[ ]”);
○ Uma mensagem confirmando a execução da tarefa deve ser
apresentada. (Exemplo: “Tarefa registrada!!!”)
####
● Marcar uma tarefa como realizada.
○ O aplicativo solicita o identificador da tarefa e, existindo, ela é movida
para o início da lista e o box vazio no final é substituído por um box
confirmado;
○ Caso o identificado não exista ou a tarefa já tenha sido realizada nada
será feito.
○ Uma mensagem confirmando a execução da tarefa deve ser
apresentada.
####
●Editar uma tarefa.
O aplicativo solicita o identificador da tarefa e, existindo, é solicitada
uma nova descrição da mesma;
○ O status do box da tarefa e o identificador da mesma não pode ser
alterado na edição;
○ Uma mensagem confirmando a execução da tarefa deve ser
apresentada.
####
Exercício 2: Pesquisa sobre persistência de dados.

Durante o módulo anterior abordamos o tema de persistência de dados utilizando arquivos. Pesquise sobre arquivos em Python e proponha as modificações necessárias para que o aplicativo do exercício anterior utilize um arquivo para armazenar a lista de tarefas.


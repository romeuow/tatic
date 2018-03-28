# tatic
Primeira etapa do processo seletivo de estágio tatic.

Algumas considerações:
- Como não foi especificado de forma explícita, foi considerado que sempre o arquivo a ser processado terá tamanho inferior a memória RAM. Esta é uma consideração importante a ser tomada, pois, caso contrário, seria feito uso de algoritmos de pesquisa e busca em memória secundária.
- Python foi linguagem escolhida para implementação dos algoritmos armazenador e buscador, devido a sua facilidade de trabalhar com listas de compreensão, que são perfeitas para esta demanda.
- Para os testes automatizados foi usado um pytest, e foi usado o arquivo de exemplo que foi disponibilizado.
- Não foi considerado casos de validação do tipo a data inicial é maior que a data final, pois o arquivo de entrada foi bem definido.
- A estratégia adotada para processar os dados, pelo armazenador, foi carregar o arquivo e ordenar os registros pela data, o python possíu um metodo chamado sort() que usa um algoritmo híbrido de ordenação chamado Timsort (uma mistura de MergeSort e SelectSort).


É necessário a instação do python, e também especificar seu diretório bin na variável Path (Variaveis de ambiente) caso os algoritmos sejam executados no Windows.

Para compilar e executar os programas armazenador e buscador:


    python armazenador.py arg1
    python buscador.py arg2 arg3 arg4 ...


Onde arg1 é o nome do arquivo onde estão os registros a serem processados pelo armazenador. arg2 e arg3 são as datas inicial e final, respectivamente, usados pelo algoritmo buscador. arg4, arg5 ... é a lista dos identificadores dos eventos usados para filtrar os registros buscados.

Para executar os testes automatizados é necessário a instalação do pytest
Após a instalação execute os testes com o comando:

    pytest testes.py
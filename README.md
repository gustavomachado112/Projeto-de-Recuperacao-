
### **Relatório de Melhorias – Projeto Recuperação, estao em baixo as melhorias e os erros**

**projeto de recuperacao , esse e com as modificacoes:  link do diagrama(bancodados):https://app.dynobird.com/?action=open&id=77c9e88d-ca61-4073-9825-a4780d4f85f1**

**3 ANO C:**  Gustavo Aparecido , tinha que fazer melhorias no trabalho da emmanuele , tinha caido com o danilo , mas vc pediu pra eu mexer no dela

---

### **SISTEMA.PY**

#### **Erro 1**
O código tentava buscar o valor atualizado usando `next()`, mas isso criava uma inconsistência porque `campanha_selecionada` era uma referência à campanha na lista `minhas_campanhas` (uma cópia filtrada). Quando o valor era atualizado na lista original `campanhas`, a cópia não se atualizava automaticamente. O `next()` buscava na lista original, mas mostrava um valor que não correspondia ao que estava sendo exibido, resultando em mensagens confusas sobre o saldo disponível.


**Melhoria 1**
* Removi o `next()` desnecessário que causava a inconsistência.
* Passei a usar diretamente `campanha_selecionada['valor_arrecadado']`.
* Como `campanha_selecionada` agora é buscada diretamente na lista `campanhas`, ela sempre reflete o valor atualizado, mantendo referência direta ao objeto na lista principal e não uma cópia.



#### **Erro 2**
**Erros nos telefones:** O `obter_inteiro()` convertia para número inteiro, fazendo com que se o telefone começasse com 0 (ex: `'0199999999'`), o zero era perdido. O `str()` convertia de volta para texto, mas sem o zero inicial, transformando `'0199999999'` em `'199999999'`.

**Melhoria 2**
* Removi a conversão para inteiro.
* Mantive como string desde o início.
* Isso preserva todos os caracteres, incluindo zeros iniciais.


#### **Erro 3**
Caso o usuário se tornasse administrador, o menu do administrador não tinha opção para sair do sistema, apenas para voltar ao menu principal. Isso deixava o administrador preso no sistema, sem uma forma direta de encerrar o programa.

**Melhoria 3**
* Adicionei a opção de **Sair do Sistema** no menu do administrador.


#### **Erro 4**
O código não tinha nenhuma função que limitasse os caracteres em mensagens ou em nenhum campo de texto. Isso era um problema porque era possível enviar grandes quantidades de informação de uma vez. Caso o sistema recebesse dados gigantescos, poderia ficar frágil. **Exemplo:** alguém poderia tentar mandar um roteiro de filme inteiro como mensagem.

**Melhoria 4**
* Adicionei validação de tamanho para todos os campos de texto.
* Preveni entradas excessivamente longas que poderiam quebrar o sistema.
* Melhorei a experiência do usuário com feedback imediato.
* Protegi o sistema contra possíveis problemas de memória ou display.


#### **Erro 5**
O código original não tinha validação para campos críticos, o que era um problema grave.

**Melhoria 5**
* Implementei loops de validação para todos os campos críticos.
* Garantia de que os dados inseridos atendem aos requisitos do sistema antes de prosseguir.
* **Inclui:**
  * Verificação de campos obrigatórios
  * Validação de formato de email
  * Garantia de valores numéricos positivos
  * Limites de caracteres em campos de texto


---

### **CONTATO.PY**

#### **Erro 1 – Importação desnecessária do módulo random**
**Problema:**
O módulo `random` era importado mas não era utilizado em nenhuma parte do código. Isso ocupava memória desnecessariamente e poluía o namespace.

**Melhoria implementada:**
* Removi completamente a importação desnecessária.

**Explicação :**
* O Python carrega módulos importados na memória, mesmo que não sejam utilizados.
* Remover importações desnecessárias melhora a performance e a legibilidade do código.

#### **Erro 2 – Falta completa de validações nos campos de entrada**
**Problema:**
A versão original não verificava se os campos estavam preenchidos nem se os dados tinham formato válido. Aceitava strings vazias e quaisquer textos.

**Melhoria implementada:**
* Implementei loops de validação com verificação de campos vazios e limites de caracteres.

**Explicação :**
* Usei estruturas `while True` com condições aninhadas para garantir que todos os campos sejam preenchidos corretamente antes de prosseguir.
* Utilizei `.strip()` para remover espaços desnecessários.
* Usei `len()` para verificar comprimentos.

#### **Erro 3 – Validação de email inexistente**
**Problema:**
Não havia nenhuma verificação do formato do email. Qualquer texto era aceito como email válido.

**Melhoria implementada:**
* Implementei validação básica do formato de email.

**Explicação :**
* Verificação da presença do caractere "@".
* Verificação da existência de um ponto na parte do domínio após o "@".
* Garante formato mínimo válido como: `usuario@provedor.com`.

#### **Erro 4 – Mensagem podia ter tamanho inadequado**
**Problema:**
Não havia limites mínimos ou máximos para o tamanho da mensagem, permitindo mensagens vazias ou excessivamente longas.

**Melhoria implementada:**
* Defini limites mínimo e máximo de caracteres para a mensagem.

**Explicação:**
* Usei `len()` para controlar o tamanho.
* Defini mínimo de 1 caractere e máximo de 200 caracteres.

**Resultado:** mensagens úteis e controladas.

#### **Erro 5 – Falta de confirmação antes do envio**
**Problema:**
O sistema enviava automaticamente sem dar chance ao usuário de revisar os dados.

**Melhoria implementada:**
* Adicionei uma etapa de confirmação mostrando todos os dados antes do envio.

**Explicação:**
* Exibição de todos os dados digitados com `f-strings`.
* Opção de cancelar o envio.
* Conversão da resposta do usuário para minúsculo para facilitar a comparação.

#### **Erro 6 – Feedback genérico e pouco útil**
**Problema:**
Mensagens genéricas que não davam informação útil sobre o status do envio.

**Melhoria implementada:**
* Reformulei completamente as mensagens de feedback.
* Agora são específicas e detalhadas, incluindo previsão de tempo de resposta.

---

### **CONFIG.PY**

#### **ERRO 1: Conversão Inadequada para Inteiro**
**Explicação do Erro:**
A conversão de telefone e data de nascimento para inteiro era tecnicamente inadequada porque telefones no Brasil frequentemente começam com zero (ex: 011, 021), e a conversão para inteiro remove zeros à esquerda. Além disso, datas de nascimento contêm caracteres não numéricos (barras "/") que causam `ValueError` na conversão, resultando em perda de informação crítica para o sistema.

**MELHORIA 1: Manutenção como String com Validação**
* Removi a conversão para inteiro e mantive os dados como string desde o início, preservando todos os caracteres incluindo zeros iniciais.
* Implementei validação com verificação de que o telefone contém apenas dígitos numéricos usando o método `isdigit()` e garanti um comprimento mínimo de 10 caracteres para assegurar que inclua DDD + número.
* Utilizei o método `strip()` para remover espaços em branco acidentais das extremidades, mantendo a simplicidade sem perder funcionalidade.

#### **ERRO 2: Falsa "Criptografia" com Random**
**Explicação do Erro:**
O uso de `random.shuffle()` criava uma falsa sensação de segurança, pois não oferecia criptografia real - era apenas um embaralhamento reversível. A senha original continuava armazenada em memória e era usada na comparação de login, tornando o código desnecessário e consumindo recursos computacionais sem propósito válido.

**MELHORIA 2: Remoção do Código Inútil**
* Eliminei completamente a lógica de criptografia que não agregava valor de segurança real.
* Removi o `import random` e todo o bloco de código que convertia a senha em lista, aplicava `shuffle` e reconstruía a string, pois esta operação era computacionalmente custosa e semanticamente vazia.
* Mantive a simplicidade do sistema sem funcionalidades desnecessárias, reduzindo a complexidade ciclomática e melhorando a performance.

#### **ERRO 3: Falta de Validações Básicas**
**Explicação do Erro:**
A ausência completa de validações permitia que dados inválidos fossem armazenados no sistema. Emails com formato incorreto impossibilitavam comunicação futura, senhas curtas comprometiam a segurança da conta, e o sistema aceitava entradas vazias ou malformadas, corrompendo a qualidade dos dados armazenados.

**MELHORIA 3: Sistema de Validação Robustecido**
* Implementei funções de validação específicas para cada campo utilizando expressões condicionais e verificações de formato.
* Para emails, verifiquei a presença do caractere "@" e a existência de um ponto no domínio usando `split("@")[1]` para acessar a parte após o arroba.
* Para senhas, implementei verificação de comprimento mínimo com `len(senha) >= 6` para garantir complexidade básica.
* Utilizei loops `while True` com `break` condicional para forçar entrada válida antes de prosseguir.

#### **ERRO 4: Senha Visível na Entrada**
**Explicação do Erro:**
A senha ficava completamente visível durante a digitação, permitindo que qualquer pessoa próxima visualizasse informações sensíveis através de *shoulder surfing*. Esta era uma falha grave de segurança que comprometia a privacidade do usuário em um sistema de cadastro.

**MELHORIA 4: Implementação de Entrada Segura**
* Utilizei o módulo `getpass` da biblioteca padrão Python para substituir a função `input()` na entrada de senhas.
* O `getpass.getpass()` oculta a digitação mostrando apenas asteriscos ou nenhum caractere, prevenindo visualização por terceiros.
* Mantive a funcionalidade original sem comprometer a segurança, adicionando texto explicativo "(não será mostrada)" para orientar o usuário sobre o comportamento esperado do campo.

#### **ERRO 5: Mensagens de Erro Genéricas**
**Explicação do Erro:**
Mensagens de erro vagas e genéricas como "Algo está errado" impossibilitavam o usuário de identificar qual campo específico estava com problema ou como corrigi-lo, resultando em experiência frustrante e abandono do processo de cadastro.

**MELHORIA 5: Mensagens Específicas e Úteis**
* Criei mensagens de erro específicas para cada tipo de validação, incluindo exemplos concretos e formatos esperados.
* Utilizei linguagem clara e direta com orientações precisas, e adicionei emojis (`❌✅`) como indicadores visuais para melhorar a compreensão imediata do problema.
* Implementei mensagens diferentes para cada campo: telefone, email, data e senha, cada uma com instruções específicas de correção.

#### **ERRO 6: Ausência de Sistema de Tentativas**
**Explicação do Erro:**
Permitir tentativas infinitas de login tornava o sistema vulnerável a ataques de força bruta, onde invasores poderiam testar combinações continuamente até descobrir credenciais válidas, uma falha grave de segurança que poderia comprometer contas de usuários.

**MELHORIA 6: Implementação de Tentativas Limitadas**
* Implementei um contador de tentativas com limite definido em 3 tentativas, utilizando uma variável `tentativas` que é decrementada (`tentativas -= 1`) a cada erro de autenticação.
* Adicionei mensagens informativas sobre tentativas restantes usando f-strings para interpolação dinâmica e implementei bloqueio final após esgotar todas as tentativas, com instruções de contato para suporte técnico.
* Utilizei um loop `while` com condição `tentativas > 0` para controlar o fluxo.

---

### **CADASTRO.PY**

#### **ERRO 1: Conversão Inadequada de Dados**
**Problema no código original:**
A primeira versão convertia telefone e data de nascimento para números inteiros usando `int()`, o que causava múltiplos problemas.

**Explicação do erro:**
* Telefones no Brasil frequentemente começam com zero (como 011, 021), e ao converter para inteiro, esse zero inicial era perdido irreversivelmente.
* Datas de nascimento contêm barras como separadores (DD/MM/AAAA), e essas barras causavam erros de conversão, fazendo o programa quebrar completamente.

**Melhoria implementada:**
* A versão atual mantém telefones e datas como texto, preservando todos os caracteres importantes.
* Para telefones, é validado se contém apenas números e tem pelo menos 10 dígitos (incluindo DDD).
* Para datas, é verificado o formato correto com três partes separadas por barras, garantindo que cada parte contenha apenas números.

#### **ERRO 2: Falta de Validações Básicas**
**Problema no código original:**
O código original não possuía nenhum sistema de validação, aceitando qualquer dado fornecido pelo usuário, mesmo que completamente inválido ou incoerente.

**Explicação do erro:**
* A ausência de validações permitia que emails sem o símbolo "@" fossem aceitos, telefones contendo letras fossem registrados, datas em formatos impossíveis fossem armazenadas e senhas vazias fossem consideradas válidas.
* Isso resultaria em um banco de dados cheio de informações corruptas e inutilizáveis.

**Melhoria implementada:**
* Foi implementado um sistema completo de validações em loop para cada campo.
* Para emails, verifica-se a presença do "@" e pelo menos um ponto após o "@".
* Para telefones, valida-se que contenha apenas dígitos numéricos e tenha comprimento adequado.
* Para datas, confirma-se o formato DD/MM/AAAA com três partes numéricas.
* Para senhas, exige-se mínimo de 6 caracteres.

#### **ERRO 3: Problemas de Segurança**
**Problema no código original:**
A senha era solicitada usando `input()` normal, fazendo com que ficasse totalmente visível na tela durante a digitação.

**Explicação do erro:**
* Esta prática representa um grave risco de segurança, pois qualquer pessoa próxima ao usuário poderia visualizar a senha sendo digitada.
* Em ambientes públicos ou compartilhados, isso exporia completamente a credencial de acesso do usuário.

**Melhoria implementada:**
* Foi implementado o uso da biblioteca `getpass`, que esconde completamente a senha durante a digitação.
* O usuário digita normalmente, mas nenhum caractere é exibido na tela, mantendo a privacidade total da informação sensível.

#### **ERRO 4: Experiência do Usuário Ruim**
**Problema no código original:**
As mensagens de erro eram extremamente genéricas e não orientativas, simplesmente informando que "algo estava errado" sem especificar o que ou como corrigir.

**Explicação do erro:**
* Mensagens vagas deixam o usuário confuso e frustrado, sem saber qual campo específico estava com problema ou como resolver a situação.
* Isso resulta em tentativas repetidas sem sucesso e abandono do sistema.

**Melhoria implementada:**
* Foram criadas mensagens de erro específicas para cada tipo de validação, informando exatamente qual o problema e como corrigi-lo.
* Para email inválido, sugere o formato correto.
* Para telefone, especifica que deve conter apenas números com DDD.
* Para data, reforça o formato DD/MM/AAAA.

#### **ERRO 5: Falta de Sistema de Tentativas**
**Problema no código original:**
Não existia qualquer limite de tentativas de login, permitindo que usuários ou atacantes tentassem senhas infinitamente.

**Explicação do erro:**
* A ausência de limite de tentativas é uma falha crítica de segurança conhecida como vulnerabilidade a ataques de força bruta.
* Um invasor poderia tentar milhões de combinações diferentes até acertar a senha correta.

**Melhoria implementada:**
* Foi implementado um sistema de segurança com três tentativas de login.
* Após três tentativas falhas, o acesso é bloqueado e o usuário é orientado a contactar o suporte.
* A cada tentativa falha, é informado quantas chances restam.

**Melhoria implementada:**
* Reformulei completamente as mensagens de feedback.
* Agora são específicas e detalhadas, incluindo previsão de tempo de resposta.

---

### **Melhorias no Banco de Dados**

#### **Erro: Redundância de `id_conta_orig` em `doacao_tb`**
A minha entidade `doacao_tb` inicialmente continha o campo `id_conta_orig`. No entanto, a conta de origem de uma doação já podia ser identificada através da `campanha_tb`, que possui o `id_conta_orig`. Manter esse campo diretamente em `doacao_tb` gerava redundância.

**Melhoria Realizada:**
* Removi o campo `id_conta_orig` da entidade `doacao_tb`.
* Agora, para obter a conta de origem da doação, eu recupero o `id_campanha` da `doacao_tb` e, em seguida, busco o `id_conta_orig` na `campanha_tb`.
* Isso reduziu a redundância e melhorou a integridade dos dados.

#### **Erro: Campos `id_conta` e `nome` redundantes em `pagamento_tb`**
Na entidade `pagamento_tb`, havia os campos `id_conta` e `nome`. Como o `id_doacao` já identifica a doação, e por sua vez, a doação está associada a uma campanha e a uma conta (via `doacao_tb` -> `campanha_tb` -> `conta_orig_tb` e `doacao_tb` -> `id_conta`), esses campos eram redundantes. O pagamento está diretamente vinculado a uma doação, então armazenar `id_conta` e `nome` era desnecessário.

**Melhoria Realizada:**
* Removi os campos `id_conta` e `nome` da entidade `pagamento_tb`.
* O relacionamento agora é feito apenas com o `id_doacao`.
* A informação da conta e do nome do pagador pode ser obtida da tabela `doacao_tb` e, se necessário, da `conta_tb`.
* Essa mudança simplificou o modelo e evitou inconsistências.

#### **Erro: Duas entidades para locais (`local_campanha_tb` e `local_eventos_tb`)**
O diagrama apresentava duas entidades para locais, o que poderia levar à duplicação de dados caso um mesmo local fosse utilizado tanto para campanhas quanto para eventos.

**Melhoria Realizada:**
* Criei uma única entidade `local_tb` para armazenar as informações de todos os locais.
* Os campos `id_local`, `nome_local`, `endereco`, `tipo_local`, `contato`, `descricao` e `imagens_local` foram movidos para esta nova tabela.
* Adicionei chaves estrangeiras (`id_local`) nas tabelas `eventos_tb` e `campanha_tb` para se relacionarem com a nova tabela `local_tb`.
* Isso evitou a duplicação de informações de locais e simplificou o esquema.

#### **Erro: Falta de clareza na cardinalidade e relacionamentos gerais**
O diagrama carecia de uma especificação clara da cardinalidade em vários relacionamentos, e nem todas as linhas de relacionamento estavam explícitas para as chaves estrangeiras.

**Melhoria Realizada:**
* Melhorei a clareza e a consistência da cardinalidade para todos os relacionamentos, garantindo que as linhas e as marcações de 1:1, 1:N ou N:N estejam presentes e corretas.

#### **Erro: Entidades `contato_tb` e `contato_para_conta_org_tb` com funções sobrepostas**
As entidades `contato_tb` e `contato_para_conta_org_tb` tinham funções muito semelhantes, com campos como `id_contato`, `nome`, `email` e `mensagem` se repetindo. Isso era um forte indício de que a informação estava sendo armazenada em mais de um lugar, o que era um erro de normalização.

**Melhoria Realizada:**
* Unifiquei as duas entidades em uma única tabela para gerenciar contatos e mensagens, renomeando-a para `mensagem_contato_tb`.
* Isso permitiu que as mensagens fossem rastreadas de forma mais eficiente e evitou a duplicação de dados.

**outros erros tambem**
*bom os ints do IDS das tabelas nao estavam consistentes entre eles , tinha ids que tinham id(10) e outro que nao tinham , hoje em dia o certo  , e deixar sem os numeros , pois ele ja reconhece o tamanho , por isso que existe smal int , int , bigint e etc.

*bom  no pagamento_tb nao tinha adicionar forma de pagamento , e so forma de pagamento, isso seria um problema caso tivermos que adicionar no futuro  , entao fiz agora outra tabela , pra evitar dor de cabeca no futuro. 

* bom esse que eu vou falar , seria caso a gente decedisse fazer um banco de dados  , nesse caso teria que ter as restricoes e os indices  nas tabelas  pois a tabela poderia repetir informacoes unique , que nao se repetem e outros casos tambem.por exemplo:um email nao se pode repetir em varias contas , sem as restricoes/indices poderia ocorrer tao problema., como:unique , indices e  a primeira chave e etc.
#### **Outras duas melhorias realizadas:**
* Padronizei todos os IDs para o tipo `INT`; antes eles estavam com números diferentes, agora todos estão consistentes, o que melhora desempenho e clareza.
* Criei uma nova tabela chamada `forma_pagamento_tb`, garantindo melhor organização dos métodos de pagamento no sistema, com isso , conseguindo colocar uma nova forma de pagamento , ja que o pagamento_tb nao aceitava 
* outra tambem foi os indices , eu adicionei indices em cada tabela do diagrama  , eu por ex :garantindo que e-mail, telefone, id_login  , eu estou garantindo que elas nao se repitam  , antes a tabela  a estrutura basica ,agora  mostras os indices e restricoes .

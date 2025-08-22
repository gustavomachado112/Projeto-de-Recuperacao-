## Relatório de Melhorias – Projeto Recuperação

**Autores:** Yvone Pimentel e Gustavo Aparecido

**Link do GitHub:** [https://github.com/gustavomachado112/Projeto-de-Recuperacao-/tree/main](https://github.com/gustavomachado112/Projeto-de-Recuperacao-/tree/main)

---

### Observações Iniciais
O código original de Emmanuele é, em essência, bem completo e de ótima qualidade. Nossas melhorias visaram aprimorar a experiência do usuário e a robustez do sistema, corrigindo pequenos erros e adicionando validações que o tornam mais seguro e confiável.

---

### Melhorias no `SISTEMA.PY`

#### **1. Correção na Atualização de Saldo**
* **Erro Original:** A atualização do saldo exibia informações inconsistentes devido ao uso de `next()` em uma cópia filtrada da lista de campanhas. Isso impedia que a referência ao valor atualizado fosse refletida no display do usuário.
* **Melhoria:** Removemos o `next()` e passamos a usar diretamente `campanha_selecionada['valor_arrecadado']`. Isso garante que a exibição do saldo esteja sempre diretamente ligada e atualizada com o valor real da campanha na lista principal.

#### **2. Validação de Telefone**
* **Erro Original:** O código convertia o telefone para número inteiro (`obter_inteiro()`), removendo o zero inicial. Ao converter de volta para string, o zero era perdido, alterando o número original.
* **Melhoria:** Eliminamos a conversão para inteiro, mantendo o telefone como string desde o início. Isso preserva todos os caracteres, incluindo zeros iniciais, e armazena os telefones corretamente.

#### **3. Opção de Sair do Sistema para o Administrador**
* **Erro Original:** O menu do administrador não possuía uma opção para encerrar o programa, apenas para retornar ao menu principal. Isso deixava o administrador "preso" no sistema.
* **Melhoria:** Adicionamos a opção **"Sair do Sistema"** ao menu do administrador, proporcionando uma experiência completa e consistente com os demais menus.

#### **4. Limite de Caracteres em Campos de Texto**
* **Erro Original:** Não havia limite de caracteres em campos de texto, tornando o sistema vulnerável a entradas excessivamente longas, o que poderia comprometer sua estabilidade.
* **Melhoria:** Implementamos validação de tamanho para todos os campos de texto. Isso previne problemas de memória e melhora a experiência do usuário com feedback imediato, tornando o sistema mais seguro e responsivo.

#### **5. Validação de Campos Críticos**
* **Erro Original:** A falta de validação em campos críticos era um ponto de vulnerabilidade grave, permitindo a inserção de dados incompletos ou em formato incorreto.
* **Melhoria:** Adicionamos **loops de validação** para todos os campos críticos. Isso inclui a verificação de campos obrigatórios, o formato de email, a exigência de valores numéricos positivos e o controle de limites de caracteres. O resultado é um sistema mais robusto e com dados confiáveis.

---

### Melhorias no `CONTATO.PY`

#### **1. Remoção de Importação Desnecessária**
* **Erro Original:** O módulo `random` era importado, mas não utilizado. Isso ocupava memória e poluía o código desnecessariamente.
* **Melhoria:** Removemos completamente a importação do módulo `random`, otimizando a performance e a legibilidade.

#### **2. Validação de Campos de Entrada**
* **Erro Original:** O sistema não verificava se os campos de entrada estavam preenchidos, aceitando strings vazias e dados inválidos.
* **Melhoria:** Adicionamos loops de validação com verificações de campos vazios e limites de caracteres (`len()`). O uso de `.strip()` também garante a remoção de espaços desnecessários.

#### **3. Validação de Formato de Email**
* **Erro Original:** O email não era validado, aceitando qualquer texto como um formato válido.
* **Melhoria:** Implementamos uma validação básica que verifica a presença dos caracteres **`@`** e **`.`** (após o `@`), garantindo um formato mínimo válido para o email.

#### **4. Limites para o Tamanho da Mensagem**
* **Erro Original:** Não havia limite de tamanho para a mensagem, permitindo que o usuário enviasse textos vazios ou excessivamente longos.
* **Melhoria:** Definimos limites mínimo (1 caractere) e máximo (200 caracteres) para a mensagem, tornando-a mais útil e controlada.

#### **5. Confirmação de Envio**
* **Erro Original:** O envio da mensagem era automático, sem dar ao usuário a oportunidade de revisar ou cancelar os dados.
* **Melhoria:** Adicionamos uma etapa de confirmação, exibindo todos os dados digitados e permitindo que o usuário revise e confirme o envio.

#### **6. Feedback do Sistema**
* **Erro Original:** As mensagens de feedback eram genéricas e não forneciam informações úteis sobre o status do envio.
* **Melhoria:** Reformulamos as mensagens de feedback, tornando-as mais específicas e detalhadas, incluindo uma previsão de tempo de resposta.

# Avaliação e Métricas

## Objetivo

A avaliação foi realizada para verificar se o Assistente de Estudos consegue fornecer respostas claras e relacionadas à base de conhecimento.

## Critérios

Foram utilizados quatro critérios:

| Critério | Descrição |
|---|---|
| Clareza | A resposta é fácil de entender? |
| Relevância | A resposta está relacionada à pergunta? |
| Utilidade | A resposta ajuda o estudante? |
| Base de conhecimento | A resposta utiliza informações disponíveis? |

## Testes realizados

### Teste 1 - Python

**Pergunta:**

"O que é Python?"

**Resultado esperado:**

Explicar que Python é uma linguagem de programação.

**Resultado obtido:**

"Python é uma linguagem de programação conhecida por possuir uma sintaxe simples."

**Resultado:**

✅ Resposta adequada.

---

### Teste 2 - Scrum

**Pergunta:**

"O que é Scrum?"

**Resultado esperado:**

Explicar que Scrum é um framework utilizado para organizar o desenvolvimento de projetos.

**Resultado obtido:**

"Scrum é um framework utilizado para organizar o desenvolvimento de projetos."

**Resultado:**

✅ Resposta adequada.

---

### Teste 3 - Kanban

**Pergunta:**

"Como funciona o Kanban?"

**Resultado esperado:**

Explicar que Kanban é uma forma visual de organizar tarefas.

**Resultado obtido:**

"Kanban é uma forma visual de organizar tarefas em colunas como A Fazer, Em Desenvolvimento e Concluído."

**Resultado:**

✅ Resposta adequada.

---

### Teste 4 - Pergunta fora da base

**Pergunta:**

"O que é futebol?"

**Resultado esperado:**

Informar que o assunto não está disponível na base de conhecimento.

**Resultado obtido:**

"Não encontrei esse assunto na minha base de conhecimento."

**Resultado:**

✅ Comportamento adequado.

---

### Teste 5 - Encerramento

**Comando:**

"sair"

**Resultado obtido:**

"Até mais! Bons estudos!"

**Resultado:**

✅ Programa encerrado corretamente.

## Resultado da avaliação

Os testes realizados demonstraram que o assistente consegue responder perguntas relacionadas aos assuntos presentes na base de conhecimento e informar quando não possui informações sobre determinado assunto.

O programa também encerra corretamente quando o usuário utiliza o comando "sair".

Como melhoria futura, a base de conhecimento pode receber mais conteúdos e o sistema pode ser integrado a modelos de IA generativa para produzir respostas mais completas.

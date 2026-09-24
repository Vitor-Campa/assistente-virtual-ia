# Assistente de Estudos

# Base de conhecimento do assistente
base_conhecimento = {
    "python": "Python é uma linguagem de programação conhecida por possuir uma sintaxe simples.",
    "scrum": "Scrum é um framework utilizado para organizar o desenvolvimento de projetos.",
    "kanban": "Kanban é uma forma visual de organizar tarefas em colunas como A Fazer, Em Desenvolvimento e Concluído.",
    "engenharia de software": "Engenharia de Software é a área responsável por aplicar métodos e técnicas para desenvolver e manter sistemas de software.",
    "banco de dados": "Banco de dados é utilizado para armazenar e organizar informações.",
    "metodologias ageis": "Metodologias ágeis são formas de organizar o desenvolvimento buscando entregas frequentes e adaptação às mudanças."
}

print("====================================")
print("       ASSISTENTE DE ESTUDOS        ")
print("====================================")
print("Digite sua pergunta.")
print("Digite 'sair' para encerrar.\n")

while True:

    pergunta = input("Você: ").lower()

    if pergunta == "sair":
        print("\nAssistente: Até mais! Bons estudos!")
        break

    encontrou = False

    for assunto in base_conhecimento:

        if assunto in pergunta:
            print("\nAssistente:", base_conhecimento[assunto])
            encontrou = True
            break

    if encontrou == False:
        print("\nAssistente: Não encontrei esse assunto na minha base de conhecimento.")
        print("Tente perguntar sobre Python, Scrum, Kanban, Engenharia de Software ou Banco de Dados.")

    print()

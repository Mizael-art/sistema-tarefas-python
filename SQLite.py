import sqlite3

# ======================================
# CONEXÃO COM BANCO
# ======================================

conexao = sqlite3.connect("tarefas.db")

cursor = conexao.cursor()

# ======================================
# CRIAR TABELA
# ======================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    concluida INTEGER DEFAULT 0
)
""")

conexao.commit()

# ======================================
# FUNÇÕES
# ======================================

def adicionar():
    nome = input("Digite a tarefa: ")

    cursor.execute("""
    INSERT INTO tarefas (nome)
    VALUES (?)
    """, (nome,))

    conexao.commit()

    print("Tarefa adicionada!")

# ======================================

def listar():

    cursor.execute("SELECT * FROM tarefas")

    tarefas = cursor.fetchall()

    print("\n===== TAREFAS =====")

    for tarefa in tarefas:

        status = "✅" if tarefa[2] == 1 else "❌"

        print(f"""
ID: {tarefa[0]}
Tarefa: {tarefa[1]}
Concluída: {status}
""")

# ======================================

def concluir():

    id_tarefa = input("Digite ID da tarefa: ")

    cursor.execute("""
    UPDATE tarefas
    SET concluida = 1
    WHERE id = ?
    """, (id_tarefa,))

    conexao.commit()

    print("Tarefa concluída!")

# ======================================

def editar():

    id_tarefa = input("Digite ID da tarefa: ")

    novo_nome = input("Novo nome: ")

    cursor.execute("""
    UPDATE tarefas
    SET nome = ?
    WHERE id = ?
    """, (novo_nome, id_tarefa))

    conexao.commit()

    print("Tarefa editada!")

# ======================================

def apagar():

    id_tarefa = input("Digite ID da tarefa: ")

    cursor.execute("""
    DELETE FROM tarefas
    WHERE id = ?
    """, (id_tarefa,))

    conexao.commit()

    print("Tarefa apagada!")

# ======================================
# MENU
# ======================================

while True:

    print("""
1 - Adicionar
2 - Listar
3 - Concluir
4 - Editar
5 - Apagar
6 - Sair
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar()

    elif opcao == "2":
        listar()

    elif opcao == "3":
        concluir()

    elif opcao == "4":
        editar()

    elif opcao == "5":
        apagar()

    elif opcao == "6":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")

# ======================================
# FECHAR CONEXÃO
# ======================================

conexao.close()
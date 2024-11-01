
import sqlite3 as lite
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import main

def janela_relatorio() -> None:


    def mostrar_relatorio() ->None:
        try:
            
            conexao = lite.connect("pesagem.db")
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM produto")
            dados = cursor.fetchall() 

            # Inserir os dados no Treeview
            for linha in dados:
                tree.insert("", tk.END, values=linha)

            conexao.close()

        except lite.Error as err:
            messagebox.showerror("Erro", f"Erro ao conectar com o banco de dados: {err}")


    def exportar_para_txt() -> None:
        try:
            
            conexao = lite.connect("pesagem.db")
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM produto")
            dados = cursor.fetchall() 

            # Criar arquivo .txt e escrever os dados nele
            with open("relatorio_produto.txt", "w") as arquivo:
                arquivo.write("Relatório de Produtos\n\n")
                for linha in dados:
                    arquivo.write(f"Codigo: {linha[0]}, Nome: {linha[1]}, Peso_liquido: {linha[2]}\n")

            
            conexao.close()

            
            exibir_relatorio_txt()
        except lite.Error as err:
            messagebox.showerror("Erro", f"Erro ao conectar com o banco de dados: {err}")


    def exibir_relatorio_txt() ->None:

        try:
            # Nova janela para exibir o conteúdo do .txt
            janela_txt = tk.Toplevel(janela_relatorio)
            janela_txt.title("Relatório para Impressão")
            janela_txt.geometry("400x300")

            # Textbox com barra de rolagem para exibir o conteúdo do .txt
            texto = scrolledtext.ScrolledText(janela_txt, wrap=tk.WORD)
            texto.pack(fill="both", expand=True)

            # Ler o conteúdo do arquivo .txt e exibi-lo na textbox
            with open("relatorio_produto.txt", "r") as arquivo:
                conteudo = arquivo.read()
                texto.insert(tk.END, conteudo)
            
            # Desabilitar edição no Textbox
            texto.configure(state='disabled')
        except Exception as err:
            messagebox.showerror("Erro", f"Erro ao abrir o relatório: {err}")

# Criação da janela principal
    janela_relatorio = tk.Tk()
    janela_relatorio.title("Relatório de Produtos")
    janela_relatorio.iconbitmap(default="img.ico")
    janela_relatorio.geometry("400x300")

    # Configuração do Treeview
    colunas = ("Codigo","Nome", "Peso_liquido")
    tree = ttk.Treeview(janela_relatorio, columns=colunas, show="headings")

    # Definindo os cabeçalhos das colunas
    for coluna in colunas:
        tree.heading(coluna, text=coluna)
        tree.column(coluna, width=150)  # Largura da coluna

    tree.pack(fill="both", expand=True)

    # Botões para atualizar o relatório e exportar para .txt
    botao_atualizar = tk.Button(janela_relatorio, text="Atualizar Relatório", command=mostrar_relatorio)
    botao_atualizar.pack(pady=5)

    botao_exportar = tk.Button(janela_relatorio, text="Imprimir", command=exportar_para_txt)
    botao_exportar.pack(pady=5)

    # Exibir a janela principal
    janela_relatorio.mainloop()


if __name__ == '__main__':
    janela_relatorio()
import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import time
import webbrowser  # Importando o módulo para abrir o navegador

# Define o caminho para o arquivo hosts (ajusta de acordo com seu sistema)
if os.name == "posix":
    hosts_path = "/etc/hosts"
else:
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect_ip = "127.0.0.1"

# Senha padrão
senha_padrao = "0000"

# Função para verificar a senha
def verificar_senha():
    global tentativas
    senha = entrada_senha.get()
    
    # Verifica se a senha está correta
    if senha == senha_padrao:
        janela_login.destroy()  # Fecha a janela de login
        criar_interface()  # Chama a função para criar a interface principal
    else:
        tentativas += 1
        if tentativas >= 3:
            messagebox.showerror("Erro", "Número máximo de tentativas alcançado. Acesso bloqueado por 30 segundos.")
            janela_login.after(30000, resetar_tentativas)  # Espera 30 segundos antes de liberar o acesso
        else:
            messagebox.showerror("Erro", f"Senha incorreta. Tentativas restantes: {3 - tentativas}")

# Função para resetar as tentativas de login após 30 segundos
def resetar_tentativas():
    global tentativas
    tentativas = 0
    messagebox.showinfo("Informação", "Você pode tentar novamente.")

# Função para limpar o cache de DNS
def limpar_cache_dns():
    if os.name == "nt":
        subprocess.run("ipconfig /flushdns", shell=True)
    else:
        subprocess.run(["sudo", "systemctl", "restart", "systemd-resolved"])

# Função para criar a interface principal após o login
def criar_interface():
    # Função para bloquear o site
    def bloquear_site():
        site = entrada_site.get()  # Pega o texto digitado pelo usuário
        if site:
            try:
                # Verifica se o site já está bloqueado
                with open(hosts_path, "r") as file:
                    linhas = file.readlines()
                    if any(site in linha for linha in linhas):
                        messagebox.showinfo("Aviso", "O site já está bloqueado.")
                        return
                
                # Abre o arquivo hosts e adiciona o site para redirecionar para localhost
                with open(hosts_path, "a") as file:
                    file.write(f"{redirect_ip} {site}\n")
                
                limpar_cache_dns()  # Limpa o cache de DNS após modificar o arquivo
                messagebox.showinfo("Sucesso", f"O site '{site}' foi bloqueado.")
                entrada_site.delete(0, tk.END)  # Limpa o campo de entrada
            except PermissionError:
                messagebox.showerror("Erro", "Permissão negada! Execute o programa como administrador.")
        else:
            messagebox.showwarning("Aviso", "Por favor, insira um site.")

    # Função para desbloquear o site
    def desbloquear_site():
        site = entrada_site.get()  # Pega o texto digitado pelo usuário
        if site:
            try:
                # Lê o conteúdo do arquivo hosts
                with open(hosts_path, "r") as file:
                    linhas = file.readlines()
                
                # Remove a linha que bloqueia o site
                with open(hosts_path, "w") as file:
                    for linha in linhas:
                        if site not in linha:
                            file.write(linha)
                
                limpar_cache_dns()  # Limpa o cache de DNS após modificar o arquivo
                messagebox.showinfo("Sucesso", f"O site '{site}' foi desbloqueado.")
                entrada_site.delete(0, tk.END)  # Limpa o campo de entrada
            except PermissionError:
                messagebox.showerror("Erro", "Permissão negada! Execute o programa como administrador.")
        else:
            messagebox.showwarning("Aviso", "Por favor, insira um site.")

    # Função para atualizar a senha
    def atualizar_senha():
        nova_senha = entrada_nova_senha.get()
        confirmacao_senha = entrada_confirmacao_senha.get()
        
        if nova_senha == confirmacao_senha:
            global senha_padrao
            senha_padrao = nova_senha
            # Atualiza a senha em um arquivo ou configura como desejado
            messagebox.showinfo("Sucesso", "Senha atualizada com sucesso!")
        else:
            messagebox.showerror("Erro", "As senhas não coincidem. Tente novamente.")

    # Função para abrir o LinkedIn
    def abrir_linkedin(event=None):
        webbrowser.open("https://www.linkedin.com/in/gsouzade")  # Abre o perfil do LinkedIn no navegador

    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Bloqueador de Sites")
    janela.config(bg="#f0f0f0")  # Cor de fundo

    # Cria o frame principal
    frame = tk.Frame(janela, bg="#f0f0f0", padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    # Texto e campo para o usuário digitar o site
    tk.Label(frame, text="Site para bloquear/desbloquear:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    entrada_site = tk.Entry(frame, width=40, font=("Arial", 12))
    entrada_site.pack(pady=5)

    # Botão para bloquear o site
    btn_bloquear = tk.Button(frame, text="Bloquear Site", command=bloquear_site, width=20, height=2, bg="#4CAF50", fg="white", font=("Arial", 12))
    btn_bloquear.pack(pady=5)

    # Botão para desbloquear o site
    btn_desbloquear = tk.Button(frame, text="Desbloquear Site", command=desbloquear_site, width=20, height=2, bg="#f44336", fg="white", font=("Arial", 12))
    btn_desbloquear.pack(pady=5)

    # Área para atualizar a senha
    tk.Label(frame, text="Atualizar Senha:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
    entrada_nova_senha = tk.Entry(frame, show="*", width=40, font=("Arial", 12))
    entrada_nova_senha.pack(pady=5)

    tk.Label(frame, text="Confirme a nova senha:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    entrada_confirmacao_senha = tk.Entry(frame, show="*", width=40, font=("Arial", 12))
    entrada_confirmacao_senha.pack(pady=5)

    btn_atualizar_senha = tk.Button(frame, text="Atualizar Senha", command=atualizar_senha, width=20, height=2, bg="#008CBA", fg="white", font=("Arial", 12))
    btn_atualizar_senha.pack(pady=10)

    # Assinatura com o LinkedIn (clicável)
    assinatura = tk.Label(janela, text="Desenvolvido em fase de estudos para melhorar a vida de sua família! www.linkedin.com/in/gsouzadev", font=("Arial", 10), fg="blue", bg="#f0f0f0", cursor="hand2", anchor="e")
    assinatura.pack(side="bottom", padx=20, pady=10)
    assinatura.bind("<Button-1>", abrir_linkedin)  # Associa o evento de clique ao link

    # Executa a interface principal
    janela.mainloop()

# Criação da tela de login
janela_login = tk.Tk()
janela_login.title("Login")
janela_login.config(bg="#f0f0f0")

# Cria o frame do login
frame_login = tk.Frame(janela_login, bg="#f0f0f0", padx=20, pady=20)
frame_login.pack(padx=10, pady=10)

# Label e entrada para senha
tk.Label(frame_login, text="Digite a senha para acessar o programa:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
entrada_senha = tk.Entry(frame_login, show="*", width=30, font=("Arial", 12))
entrada_senha.pack(pady=5)

# Botão de login
btn_login = tk.Button(frame_login, text="Entrar", command=verificar_senha, width=20, height=2, bg="#4CAF50", fg="white", font=("Arial", 12))
btn_login.pack(pady=10)

# Variável global para o controle de tentativas
tentativas = 0

# Executa a tela de login
janela_login.mainloop()

# Bloqueador-de-Pornografia
Ferramenta para bloquear e desbloquear sites com controle de senha. Permite gerenciar o acesso à internet de forma simples, com funcionalidades para modificar o arquivo hosts, bloquear e desbloquear sites, além de atualizar a senha de acesso. Suporta Windows e Linux.


Bloqueador e Desbloqueador de Sites com Controle de Senha
Este projeto fornece uma ferramenta prática e eficiente para controlar o acesso a sites indesejados, com a possibilidade de bloquear e desbloquear sites de maneira simples e segura. Ele é projetado para ser usado por qualquer pessoa que queira melhorar a gestão do uso da internet, seja em um ambiente doméstico, escolar ou até mesmo corporativo.

Funcionalidades principais:
Login Seguro:

O acesso ao sistema é protegido por uma senha.
O usuário pode tentar inserir a senha até três vezes. Caso as tentativas falhem, o sistema impede novas tentativas por 30 segundos.
Bloqueio de Sites:

Permite bloquear qualquer site especificado pelo usuário.
O sistema redireciona o site bloqueado para o IP 127.0.0.1 (localhost), tornando-o inacessível através do navegador.
A ferramenta verifica se o site já está bloqueado antes de adicionar uma nova entrada no arquivo hosts, evitando duplicações.
Desbloqueio de Sites:

O usuário pode desbloquear qualquer site previamente bloqueado.
O sistema remove a entrada correspondente ao site no arquivo hosts, restaurando o acesso normal ao site.
Após a modificação, o cache de DNS é limpo para garantir que as mudanças tenham efeito imediato.
Atualização de Senha:

O sistema permite que o usuário altere a senha de acesso a qualquer momento, fornecendo uma camada extra de segurança.
O novo valor da senha é verificado, e o sistema garante que ambas as senhas (nova e de confirmação) coincidam antes de atualizar a senha.
Interface Simples e Intuitiva:

A interface gráfica é construída usando a biblioteca Tkinter, proporcionando uma experiência de usuário amigável e de fácil navegação.
Campos de entrada claros e botões bem definidos para realizar as ações de bloqueio, desbloqueio e atualização de senha.
Mensagens de feedback, como "Sucesso" e "Erro", para informar o status das ações.
Suporte ao Sistema Operacional:

O projeto foi desenvolvido para funcionar em sistemas operacionais Windows e Linux (com ajustes de caminho de arquivo hosts para cada sistema).
No Windows, o caminho padrão para o arquivo hosts é configurado automaticamente, enquanto no Linux, é feito o mesmo ajuste para garantir a compatibilidade.
Segurança e Privacidade:

O sistema requer privilégios administrativos (ou "root") para modificar o arquivo hosts, garantindo que somente usuários autorizados possam bloquear ou desbloquear sites.
Todas as ações são executadas de forma segura, sem comprometer a privacidade do usuário ou permitir alterações não autorizadas.
Objetivos do Projeto:
Este projeto tem como objetivo fornecer uma ferramenta fácil de usar para o controle de sites, promovendo uma navegação mais saudável e segura. Ideal para ambientes onde o acesso a determinados sites precisa ser restrito, seja para evitar distrações, melhorar a produtividade ou garantir a segurança de crianças e adolescentes. A ferramenta também oferece flexibilidade para que o usuário personalize suas configurações de bloqueio e desbloqueio de sites de acordo com suas necessidades.

Esse projeto é ideal para quem procura uma solução simples e acessível para controlar o acesso à internet, com uma interface gráfica intuitiva e funcionalidades robustas, que incluem segurança por senha, controle de sites e fácil atualização das configurações.

Meu perfil: www.linkedin.com/in/gsouzadev


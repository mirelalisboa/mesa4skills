---
name: construir-site-interativo-python
description: Especificar e construir um MVP de site interativo em Python com navegação, formulários, autenticação, dados e APIs sob premissas explícitas de hospedagem.
---

# Construir site interativo em Python com escopo seguro

**Problema e usuário:** empreendedores e equipes precisam transformar uma necessidade de negócio em um MVP web pequeno, hospedável e evolutivo, sem iniciar com complexidade desnecessária.

## Objetivo
Produzir uma especificação implementável e, quando autorizado, um MVP com validação de entradas, persistência e tratamento de erros.

## Quando usar
Use para site com páginas, formulário, login, painel, banco, API ou atualização dinâmica. Para alterar dados ou publicar em produção, confirme a intenção antes da execução.

## Entradas
- Problema, público, fluxos e critérios de sucesso.
- Páginas, campos, papéis, dados e integrações.
- Requisitos de hospedagem, escala, orçamento e privacidade/LGPD.
- Credenciais, domínio e banco: nunca inclua segredos no código.

## Saídas
`site-spec.md` com arquitetura, rotas, modelo de dados, segurança, dependências, ambiente, testes e plano de deploy. Código só é produzido após autorização explícita.

## Passos
1. Reduza o pedido a um fluxo principal e registre premissas, fora de escopo e critérios de aceite.
2. Escolha **Flask** para MVP pequeno e páginas simples; **Django** quando houver autenticação, admin e modelo relacional robustos; **FastAPI** quando API-first, tipagem e concorrência forem centrais.
3. Modele rotas, estados, validações, permissões e erros antes da UI.
4. Defina persistência: SQLite para protótipo local; PostgreSQL para produção multiusuário. Nunca trate SQLite como escolha automática para alta concorrência.
5. Planeje `.env`, migrações, logs sem dados sensíveis, CSRF, sessões seguras, hashing de senha e rate limiting.
6. Especifique testes de fluxo feliz, validação, autorização, falha de integração e acessibilidade.
7. Descreva hospedagem: serviço compatível com WSGI/ASGI, HTTPS, variáveis de ambiente, backup e rollback. Alternativas de baixo custo devem ser comparadas, não presumidas.
8. Só depois da confirmação implemente, rode testes e prepare deploy; não publique automaticamente.

## Regras e exceções
- Não armazenar senha em texto puro, segredos no repositório ou dados pessoais além do necessário.
- Consentimento, finalidade, retenção e exclusão devem ser definidos para analytics e formulários.
- Uploads, webhooks e APIs externas exigem validação, limites e tratamento de timeout.
- Requisitos conflitantes de produto devem ser apresentados como opções.

## Critérios de aceite
- Fluxos, rotas, esquema de dados e permissões estão rastreáveis ao requisito.
- Dependências e premissas de hospedagem estão documentadas.
- Há plano de testes para segurança, erro e acessibilidade.
- Nenhuma ação irreversível ou publicação ocorre sem confirmação do usuário.

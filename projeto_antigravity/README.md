# Mesa 4 Skills

Plataforma web do Mesa 4 para transformar ideias em roteiros, textos, planos de ação e materiais de conteúdo. O projeto combina skills reutilizáveis com uma interface interativa em Flask, mantendo o foco em prática, clareza e revisão humana.

> **Status:** MVP funcional, sem banco de dados e sem publicação automática de conteúdo.

## O que você encontra

### Pontos de partida

- **Roteiros e textos prontos:** roteiros de 30 segundos, hooks e posts de vendas em AIDA.
- **Planos de ação e listas:** checklists de edição, erros de copywriting e calendários de postagem.
- **Feedback e revisão:** prompts para melhorar textos e avaliar ideias de vídeo.

### Ferramentas interativas

- Gerador de rascunho para roteiro, copy, ativo visual e site Python.
- Plano de estudos personalizado de quatro semanas.
- Gerador de prompts para workflows com IA.
- Biblioteca de conteúdo sobre execução, marca, monetização e ferramentas.
- Tema claro/escuro com preferência salva no navegador.
- Imagem e link do canal [Somos Mesa 4 no YouTube](https://www.youtube.com/@SomosMesa4).

## Tecnologias

- Python 3.10+
- Flask 3
- Jinja2
- HTML e CSS responsivos
- JavaScript vanilla para interações locais

## Como executar localmente

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abra [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Rotas principais

| Rota | Função |
|---|---|
| `/` | Página inicial e pontos de partida |
| `/usar/video` | Roteiro de vídeo curto |
| `/usar/copy` | Copy persuasiva |
| `/usar/visual` | Brief visual para Figma |
| `/usar/site` | Especificação de site Python |
| `/explorar` | Biblioteca de conteúdos |
| `/planejamento` | Plano de estudos interativo |
| `/prompts` | Gerador de prompts com IA |
| `/ponto/roteiros-textos` | Roteiros e textos prontos |
| `/ponto/planos-listas` | Planos de ação e listas |
| `/ponto/feedback-revisao` | Feedback e revisão |

## Estrutura do projeto

```text
.
├── app.py                         # Rotas e geradores Flask
├── requirements.txt               # Dependências
├── templates/                     # Páginas Jinja2
├── static/style.css               # Temas e responsividade
├── static/images/                 # Imagens do projeto
└── .agents/skills/                # Skills documentadas
```

## Skills documentadas

- [Roteirizar vídeo curto](.agents/skills/roteirizar-video-curto/SKILL.md)
- [Escrever copy persuasiva](.agents/skills/escrever-copy-persuasiva/SKILL.md)
- [Projetar ativo visual](.agents/skills/projetar-ativo-visual/SKILL.md)
- [Construir site interativo em Python](.agents/skills/construir-site-interativo-python/SKILL.md)
- `business-narrative-builder`, `summarize-signal` e `image-analyzer` como skills de apoio.

## Privacidade e limites

As respostas dos formulários não são persistidas em banco. Não envie senhas, dados confidenciais ou informações pessoais desnecessárias. Valide fatos, direitos autorais, provas e alegações antes de publicar qualquer resultado.

## Licença

Defina a licença do repositório antes de distribuir o projeto publicamente.

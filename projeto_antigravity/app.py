from flask import Flask, render_template, request

app = Flask(__name__)

SKILLS = {
    "video": {
        "name": "Roteirizar vídeo curto",
        "eyebrow": "Conteúdo vertical",
        "description": "Transforme uma ideia em um roteiro gravável para Reels, TikTok ou Shorts.",
        "fields": [
            ("tema", "Tema e promessa central", "O que o vídeo precisa ensinar ou provocar?", True),
            ("publico", "Público", "Quem deve se identificar com o vídeo?", True),
            ("plataforma", "Plataforma e duração", "Ex.: Instagram Reel, 45 segundos", False),
            ("tom", "Tom de voz", "Ex.: direto, didático e energético", False),
            ("cta", "CTA", "Ex.: salve este vídeo e compartilhe", False),
        ],
    },
    "copy": {
        "name": "Escrever copy persuasiva",
        "eyebrow": "Mensagem que move",
        "description": "Crie headlines, legendas, e-mails e CTAs sem inventar provas.",
        "fields": [
            ("oferta", "Oferta ou produto", "O que está sendo oferecido?", True),
            ("publico", "Público e problema", "Para quem é e qual dor resolve?", True),
            ("canal", "Canal e objetivo", "Ex.: landing page para gerar leads", False),
            ("tom", "Tom de voz", "Ex.: humano, confiante e simples", False),
            ("provas", "Provas disponíveis", "Resultados, dados ou depoimentos já validados", False),
        ],
    },
    "visual": {
        "name": "Projetar ativo visual",
        "eyebrow": "Design com intenção",
        "description": "Saia da ideia para um brief visual reproduzível no Figma.",
        "fields": [
            ("mensagem", "Mensagem principal", "O que a pessoa precisa entender primeiro?", True),
            ("canal", "Canal e formato", "Ex.: carrossel Instagram, 1080×1350", True),
            ("publico", "Público", "Quem verá o ativo?", False),
            ("marca", "Cores, fontes e referências", "Informe identidade visual ou escreva 'a definir'", False),
            ("cta", "CTA", "Qual ação o ativo deve orientar?", False),
        ],
    },
    "site": {
        "name": "Construir site interativo em Python",
        "eyebrow": "MVP web",
        "description": "Organize um site pequeno, seguro e pronto para evoluir.",
        "fields": [
            ("problema", "Problema a resolver", "Que necessidade o site atende?", True),
            ("publico", "Público e fluxo principal", "Quem usa e qual ação realiza?", True),
            ("recursos", "Páginas e recursos", "Ex.: home, formulário, painel e login", True),
            ("hospedagem", "Hospedagem e orçamento", "Ex.: protótipo local, baixo custo", False),
            ("dados", "Dados e privacidade", "Que dados serão coletados? Há requisito LGPD?", False),
        ],
    },
}

STARTING_POINTS = {
    "roteiros-textos": {
        "title": "Roteiros e textos prontos",
        "eyebrow": "Produza agora",
        "description": "Roteiros curtos, hooks e posts de vendas para transformar uma ideia em conteúdo.",
        "prompts": [
            "Escreva 3 opções de roteiro de 30 segundos para Reels/TikTok sobre [seu tema].",
            "Crie 5 ganchos (frases iniciais) chamativos para reter a atenção em um vídeo.",
            "Escreva um post de vendas usando a estrutura AIDA (Atenção, Interesse, Desejo, Ação).",
        ],
        "links": [("Roteirizar vídeo curto", "/usar/video"), ("Escrever copy persuasiva", "/usar/copy")],
    },
    "planos-listas": {
        "title": "Planos de ação e listas",
        "eyebrow": "Organize a execução",
        "description": "Checklists, erros para evitar e calendários de conteúdo para sair da intenção e executar.",
        "prompts": [
            "Me dê um checklist de edição para deixar um vídeo curto mais dinâmico.",
            "Liste os 5 erros mais comuns em Copywriting que eu devo evitar hoje.",
            "Crie um calendário de postagens para 7 dias com o tema [seu assunto].",
        ],
        "links": [("Montar plano de estudos", "/planejamento"), ("Explorar biblioteca", "/explorar")],
    },
    "feedback-revisao": {
        "title": "Feedback e revisão",
        "eyebrow": "Melhore o que já existe",
        "description": "Use perguntas objetivas para revisar textos e transformar ideias de vídeo em propostas mais atraentes.",
        "prompts": [
            "Analise este texto que escrevi e reescreva de forma mais persuasiva: [seu texto].",
            "Avalie esta ideia de vídeo e me diga como torná-la mais atraente: [sua ideia].",
        ],
        "links": [("Criar prompts de revisão", "/prompts"), ("Projetar ativo visual", "/usar/visual")],
    },
}


def value(form, key, fallback="não informado"):
    return form.get(key, "").strip() or fallback


def generate(skill_id, form):
    data = {key: value(form, key) for key, *_ in SKILLS[skill_id]["fields"]}
    skill = SKILLS[skill_id]["name"]
    if skill_id == "video":
        body = f"""# Roteiro de vídeo curto\n\n## Premissas\n- Tema: {data['tema']}\n- Público: {data['publico']}\n- Plataforma/duração: {data['plataforma']}\n- Tom: {data['tom']}\n\n## Estrutura sugerida\n1. **Hook (0–3 s):** apresente uma pergunta ou tensão diretamente ligada a “{data['tema']}”.\n2. **Contexto (3–10 s):** mostre por que isso importa para {data['publico']}.\n3. **Valor (10–35 s):** entregue de 1 a 3 pontos práticos, com cortes e texto na tela.\n4. **Exemplo (35–45 s):** demonstre a aplicação sem inventar resultados.\n5. **CTA:** {data['cta']}.\n\n## Checklist\n- Legendas legíveis mesmo sem áudio.\n- Formato vertical 9:16 e área segura.\n- Música e imagens com licença compatível.\n- Revisar duração antes de publicar."""
    elif skill_id == "copy":
        body = f"""# Copy persuasiva\n\n## Brief\n- Oferta: {data['oferta']}\n- Público/problema: {data['publico']}\n- Canal/objetivo: {data['canal']}\n- Tom: {data['tom']}\n- Provas disponíveis: {data['provas']}\n\n## Rascunho\n**Headline:** Para {data['publico']}, uma forma mais clara de avançar com {data['oferta']}.\n\n**Benefício:** Explique o mecanismo e o próximo passo em linguagem simples, sem prometer resultado garantido.\n\n**Prova:** [PROVA NECESSÁRIA — validar antes de usar]\n\n**CTA:** Conheça a solução e escolha o próximo passo.\n\n## Revisão\n- Confirmar cada alegação com uma fonte ou evidência.\n- Manter uma única ação principal.\n- Ajustar o texto ao canal antes do teste A/B."""
    elif skill_id == "visual":
        body = f"""# Brief visual para Figma\n\n## Direção\n- Mensagem: {data['mensagem']}\n- Canal/formato: {data['canal']}\n- Público: {data['publico']}\n- Identidade: {data['marca']}\n- CTA: {data['cta']}\n\n## Wireframe\n1. **Frame:** definir dimensão e área segura do canal.\n2. **Topo:** headline com a mensagem principal.\n3. **Centro:** imagem, exemplo ou diagrama que apoie a leitura.\n4. **Base:** prova/detalhe e CTA com alto contraste.\n\n## Entrega\nUsar grid, espaçamento consistente, hierarquia tipográfica e componentes reutilizáveis. Exportar no formato pedido e verificar leitura em tamanho real. Registrar origem e licença de imagens, fontes e ícones."""
    else:
        body = f"""# Especificação de site interativo\n\n## Escopo\n- Problema: {data['problema']}\n- Público/fluxo: {data['publico']}\n- Recursos: {data['recursos']}\n- Hospedagem/orçamento: {data['hospedagem']}\n- Dados/privacidade: {data['dados']}\n\n## Arquitetura recomendada\n- **Framework:** Flask para este MVP de páginas e formulários; Django se autenticação/admin crescerem; FastAPI se a API for o produto principal.\n- **Persistência:** SQLite no protótipo local; PostgreSQL para produção multiusuário.\n- **Configuração:** variáveis de ambiente, sem segredos no código.\n\n## Segurança e aceite\nValidar entradas, proteger CSRF e sessões, aplicar hashing de senhas, limitar requisições e não coletar dados além do necessário. Testar fluxo feliz, autorização, erros, acessibilidade e falha de integração. Publicação e alterações em produção exigem confirmação explícita."""
    return skill, body


@app.get("/")
def home():
    return render_template("index.html", skills=SKILLS, starting_points=STARTING_POINTS)


@app.route("/usar/<skill_id>", methods=["GET", "POST"])
def use_skill(skill_id):
    if skill_id not in SKILLS:
        return render_template("404.html"), 404
    skill = SKILLS[skill_id]
    result = None
    if request.method == "POST":
        required = [key for key, _, _, is_required in skill["fields"] if is_required]
        missing = [key for key in required if not request.form.get(key, "").strip()]
        if missing:
            result = {"error": "Preencha os campos obrigatórios para gerar o rascunho."}
        else:
            name, body = generate(skill_id, request.form)
            result = {"name": name, "body": body}
    return render_template("skill.html", skill=skill, skill_id=skill_id, result=result)


@app.get("/ponto/<point_key>")
def starting_point(point_key):
    if point_key not in STARTING_POINTS:
        return render_template("404.html"), 404
    return render_template("starting-point.html", point=STARTING_POINTS[point_key])


EXPLORE = {
    "planos": {
        "title": "Planos de estudo & roteiros práticos",
        "intro": "Aprenda fazendo: trilhas curtas, projetos para portfólio e ferramentas para acelerar a prática.",
        "items": [
            ("Plano de 4 semanas", "copywriting", "Monte uma rotina progressiva do zero ao primeiro projeto."),
            ("Projetos de portfólio", "portfólio", "Treine edição de vídeo com três briefs fictícios e publicáveis."),
            ("Trilha de ferramentas", "ferramentas", "Compare opções gratuitas e pagas para vídeo, copy e design."),
        ],
    },
    "execucao": {
        "title": "Estratégia, roteiros & execução",
        "intro": "Transforme conceitos em conteúdo: hooks, roteiros de 60 segundos, exercícios e storytelling.",
        "items": [
            ("Roteiro de 60 segundos", "retenção", "Hook nos primeiros 3 segundos, desenvolvimento e CTA."),
            ("Exercícios de copy", "hooks", "Cinco variações para exercitar clareza e atenção."),
            ("Storytelling aplicado", "AIDA e Jornada do Herói", "Escolha a estrutura narrativa certa para sua marca."),
        ],
    },
    "marca": {
        "title": "Posicionamento de marca & monetização",
        "intro": "Construa uma presença coerente, encontre seu público e transforme skill em serviço.",
        "items": [
            ("Calendário editorial", "conteúdo", "Equilibre educação, engajamento e vendas na semana."),
            ("Persona e nicho", "posicionamento", "Organize dores, desejos e contexto do cliente ideal."),
            ("Primeiros clientes", "freelancer", "Empacote sua oferta, prospecte e monte prova de trabalho."),
        ],
    },
    "ia": {
        "title": "Integração com inteligência artificial",
        "intro": "Use IA para acelerar pesquisa, ideação e rascunhos sem perder autoria, contexto ou revisão humana.",
        "items": [
            ("Workflows com IA", "processo", "Da pauta ao roteiro, com pontos claros de revisão humana."),
            ("Gerador de prompts", "prompts", "Crie comandos reutilizáveis para posts e textos persuasivos."),
            ("Originalidade e ética", "revisão", "Use referências sem copiar e valide fatos antes de publicar."),
        ],
    },
}

TOOLS = {
    "Edição de vídeo": "CapCut (gratuito), DaVinci Resolve (gratuito), Adobe Premiere (pago), Audacity (gratuito).",
    "Copywriting": "Google Docs (gratuito), Notion (gratuito), LanguageTool (gratuito/pago), ChatGPT (gratuito/pago).",
    "Design e UI/UX": "Figma (gratuito/pago), Canva (gratuito/pago), Penpot (gratuito e open source), Coolors (gratuito).",
}


@app.get("/explorar")
def explore():
    return render_template("explore.html", explore=EXPLORE, tools=TOOLS)


@app.get("/explorar/<section_key>")
def explore_section(section_key):
    if section_key not in EXPLORE:
        return render_template("404.html"), 404
    return render_template("section.html", section=EXPLORE[section_key], section_key=section_key)


@app.route("/planejamento", methods=["GET", "POST"])
def study_plan():
    plan = None
    if request.method == "POST":
        topic = value(request.form, "topic", "Copywriting")
        goal = value(request.form, "goal", "criar meu primeiro projeto")
        hours = value(request.form, "hours", "5 horas")
        plan = {
            "title": f"Plano de 4 semanas: {topic}",
            "goal": goal,
            "hours": hours,
            "weeks": [
                ("Semana 1 — Fundamentos", "Estude os conceitos essenciais de " + topic + ". Crie um mapa de referências e reescreva 5 exemplos existentes, identificando o que funciona."),
                ("Semana 2 — Técnica", "Pratique uma técnica por dia. Produza 3 variações, compare clareza e peça feedback de uma pessoa do público."),
                ("Semana 3 — Projeto", "Escolha um briefing real ou fictício. Crie, revise e documente as decisões, limitações e evidências usadas."),
                ("Semana 4 — Portfólio", "Finalize o projeto, escreva o estudo de caso, publique apenas após revisar direitos autorais e peça uma avaliação externa."),
            ],
        }
    return render_template("planner.html", plan=plan)


@app.route("/prompts", methods=["GET", "POST"])
def prompts():
    generated = None
    if request.method == "POST":
        area = value(request.form, "area", "criação de conteúdo")
        objective = value(request.form, "objective", "gerar ideias")
        audience = value(request.form, "audience", "meu público")
        tone = value(request.form, "tone", "claro e humano")
        generated = [
            f"Atue como estrategista de {area}. Gere 10 ideias para {objective} voltadas a {audience}. Para cada uma, informe a promessa, o formato e a pergunta que valida a relevância. Não invente dados.",
            f"Crie um rascunho de {area} sobre [TEMA] para {audience}, com tom {tone}. Estruture em hook, contexto, 3 pontos práticos e CTA. Marque [PROVA NECESSÁRIA] em toda alegação sem fonte.",
            f"Revise o texto abaixo como editor de {area}: preserve a voz do autor, aponte trechos genéricos, sugira cortes e liste o que precisa ser validado antes da publicação. Texto: [COLE AQUI]",
        ]
    return render_template("prompts.html", generated=generated)


if __name__ == "__main__":
    app.run(debug=False)

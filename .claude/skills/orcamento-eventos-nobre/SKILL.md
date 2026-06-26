---
name: orcamento-eventos-nobre
description: Gera orçamento e proposta profissional de eventos para o Nobre Bistrô (catering, buffet, finger food). Use SEMPRE que o Breno pedir orçamento, proposta, precificação, cardápio com preço, "quanto cobrar" ou "quanto sai" para qualquer evento — coquetel, almoço, jantar, buffet, batizado, aniversário, 15 anos, casamento, Natal, Páscoa, etc. — mesmo que ele não diga a palavra "orçamento". O fluxo faz pesquisa de mercado de preços com fontes citadas, monta uma planilha de custo em Excel (dimensionamento + custo-plus + 3 cenários) e uma proposta em PDF com a identidade do Nobre Bistrô, e sempre inclui análise crítica de itens de baixa margem e alto desperdício. Acione esta skill antes de responder a qualquer pedido de precificação de evento.
---

# Orçamento de Eventos — Nobre Bistrô

Fluxo padrão do Breno (chef e dono do Nobre Bistrô, Osasco-SP) para precificar e propor eventos. O objetivo é sempre o mesmo: um orçamento **realista, lucrativo e competitivo**, com uma proposta de cliente bonita e uma planilha de custo editável.

## Princípios inegociáveis
- **Português do Brasil**, tom direto, técnico e objetivo. Sem clichê.
- **Receitas e quantidades sempre em métrico** (g, ml, °C).
- **Análise crítica acima de agradar.** Sempre apontar riscos, gargalos, itens de baixa margem ou alto desperdício, e oferecer alternativas mais rentáveis sem perder elegância. Nunca validar por validar.
- **Verificabilidade.** Pesquisar preços atuais e **citar a fonte**. Sinalizar claramente o que é estimativa ("validar com fornecedor"). Nunca inventar preço.
- **O TEMPO DO BRENO É CUSTO.** Sempre precificar a mão de obra dele (horas de produção × R$/h + horas no local). É o erro mais comum e costuma ser o MAIOR custo do evento. Nunca subestimar.
- **Conferir o PDF visualmente** (rasterizar e olhar a imagem) antes de entregar.

## Workflow
1. **Levantar os dados do evento.** Data; nº de convidados (separar adultos de crianças/bebês — bebês não consomem o menu, então o custo real é pelos adultos); duração; formato (coquetel / finger individual / buffet / empratado); local; bebidas (inclusas ou não); restrições; ocasião. Ler conversa, print de WhatsApp ou briefing se houver.
2. **Fechar o cardápio.** Equilibrar: cortar repetição de ingredientes entre pratos, contrastar texturas e riqueza, usar salada ácida pra cortar gordura, sobremesa leve pra fechar. Quando o Breno deixar escolha em aberto (proteína, salada, sabor), recomendar uma opção forte com justificativa.
3. **Pesquisar preços** dos insumos que mais pesam e que são incertos (carnes nobres, queijos importados/búfala, frutos do mar/bacalhau, pistache, frutas vermelhas). Citar fontes. Sinalizar **sazonalidade** (framboesa: safra dez–fev; morango: safra no inverno/primavera) e **prêmio de datas** (Natal/Páscoa encarecem bacalhau, filé, pernil) e **adicional de feriado na mão de obra**.
4. **Montar a planilha** (Excel, 3 abas: Dimensionamento, Custos, Precificação). Usar `scripts/build_orcamento_xlsx.py`. Detalhes de ratios, linhas de custo e fórmulas em `references/metodologia.md`.
5. **Montar a proposta em PDF** com a marca Nobre Bistrô. Usar `assets/proposta_template.html` + `scripts/build_proposta_pdf.py`.
6. **Apresentar no chat:** custo total, custo/convidado, CMV% e os 3 cenários. Fazer a análise crítica (itens de baixa margem/alto desperdício + alternativas). Deixar o Breno escolher o valor.
7. **Padrão "gordura".** Ele costuma escolher um cenário e pedir pra somar uma folga ("coloca uns R$X de gordura"). Some o valor e arredonde para um **valor por convidado redondo (múltiplo de 5)**, informando a folga real adicionada e a margem líquida resultante.

## Precificação (resumo — detalhe em references/metodologia.md)
- **Custo total** = insumos + descartáveis/embalagens + gás + energia + perdas (10% s/ insumos) + transporte + **equipe (incluindo o Breno)** + estrutura/locação.
- **Preço = Custo / (1 − imposto% − margem_líquida_alvo%).**
- **3 cenários:** Econômico 12% · **Profissional 22% (recomendado)** · Premium 32%.
- **Imposto:** confirmar Anexo do Simples (~6%–15,5%); usar ~10% como placeholder e sinalizar.
- **CMV** (insumos ÷ preço) como métrica de leitura.
- **Competitividade:** comparar com o segmento certo — buffet servido a domicílio fica em ~R$150–400/pessoa, com carnes nobres/frutos do mar no topo. "Ceia pronta"/delivery industrializado (R$40–140) **não** é concorrente de menu artesanal servido. Não baixar preço por comparar com produto diferente.

## Marca e PDF
- Paleta: bordô **#7B2D2D**, creme **#FBF7F1**, dourado **#B08D57**, texto **#3A3338**. Serifada (Georgia/Liberation Serif) no corpo; labels em sans com letter-spacing.
- Logo Nobre Bistrô em `assets/logo_nobre.png` (fundo transparente). Rodapé: "Gastronomia & Eventos · Osasco — São Paulo".
- Sempre: data do evento; validade 15 dias; "valores sujeitos a ajuste conforme cardápio final"; deixar claro o que **não** está incluso (bebidas, louça, etc.).
- Copy de cliente: natural, como o Breno escreve, sem clichê de IA e sem erros.
- Renderizar com `wkhtmltopdf` (A4, margens 0). **Conferir visualmente** antes de entregar.

## Entregáveis
1. Planilha **.xlsx** — modelo editável com fórmulas (o Breno troca os preços de referência pelos do fornecedor dele e tudo recalcula).
2. Proposta **.pdf** — cliente, na identidade Nobre Bistrô.
3. No chat — resumo executivo + cenários + análise crítica.

# Nobre Bistro — Painel Admin

Painel de gestão do Nobre Bistro (bistrô dentro de salão de beleza). App single-file
em React (via CDN) + Supabase como backend. Funciona abrindo o `index.html` em qualquer
navegador ou publicado em hospedagem estática (Vercel, Netlify, GitHub Pages).

## Como usar

1. Abra `index.html` no navegador (ou acesse a URL publicada).
2. Faça login com uma das senhas abaixo.

### Senhas de acesso

| Perfil     | Senha       | O que vê                                  |
|------------|-------------|-------------------------------------------|
| Gerente    | `nobre2025` | Todas as abas (caixa, financeiro, ERP...) |
| Atendente  | `balcao`    | Balcão, Pedidos, Cozinha                  |
| Cozinha    | `cozinha`   | Apenas Cozinha                            |

> Recomendado trocar essas senhas antes de uso real (estão no `index.html`, na função `App`).

## Navegação (organizada em grupos)

As telas ficam agrupadas em **7 grupos grandes com ícone** (mais fácil para quem
tem pouca familiaridade com sistemas). Ao tocar num grupo, aparecem as sub-abas dele:

| Grupo          | Ícone | O que tem dentro                                   |
|----------------|-------|----------------------------------------------------|
| Operação       | 🍽️   | Balcão · Pedidos · Cozinha                          |
| Dinheiro       | 💰    | Caixa do dia · Relatórios · Consultor IA           |
| Fiado          | 📒    | Em aberto · Fechar quinzena · Histórico            |
| Cardápio       | 📖    | Cardápio · Receitas/CMV                            |
| Clientes       | ⭐    | Clientes (fidelidade) · Centro IA                  |
| Equipe         | 👥    | Pessoas · Horários                                 |
| Estoque        | 📦    | Produtos · Insumos · Fornecedores · Compras (ERP)  |

O **Atendente** só vê o grupo **Operação**; a **Cozinha** só vê **Cozinha**.

## Login por PIN, comissão, margem e despesas

- **PIN individual por funcionário** — cada pessoa cadastrada na aba **Pessoas**
  pode ter um PIN próprio e um papel (Gerente / Atendente / Cozinha). Ao entrar
  com o PIN, o sistema sabe **quem** está operando, e toda venda do balcão guarda
  o nome do operador. As senhas-mestras (`nobre2025`, `balcao`, `cozinha`)
  continuam funcionando como atalho do dono.
- **Comissão de venda** — cada funcionário tem um **% de comissão** (aba Pessoas).
  A aba **Comissões** (dentro do grupo Equipe) mostra, por período (hoje / quinzena
  / mês), quanto cada um vendeu e quanto recebe de comissão, com botão de enviar no
  WhatsApp.
- **Margem de lucro** — cada produto do **Cardápio** agora tem um campo de **custo**.
  Os **Relatórios** mostram lucro bruto, margem % e **lucro líquido do mês**
  (vendas − custo dos produtos − despesas).
- **Despesas** — aba nova (grupo Dinheiro) para lançar contas/gastos por categoria;
  entram no cálculo do lucro líquido.

## Segurança / Anti-roubo

- **Cancelar pedido exige a senha do gerente** — um atendente sozinho não consegue
  cancelar uma venda. Todo cancelamento grava data, hora, motivo e quem autorizou
  (tabelas `audit_logs` e `system_events`).
- **Telas de dinheiro são exclusivas do gerente** — Caixa, Relatórios, Fiado,
  Quinzena, Equipe e todo o ERP ficam invisíveis para atendente e cozinha.
- **A tela de login não mostra mais as senhas** (antes elas apareciam escritas).
- Recomendado **trocar as senhas** padrão antes do uso real (estão no `index.html`,
  função `App`, e o gatilho do cancelamento usa `nobre2025`).

## Funcionalidades

- **Balcão** — lançar pedidos, formas de pagamento, fiado para profissionais
- **Pedidos / Cozinha** — fila de produção, tempo de preparo, conclusão
- **Caixa / Financeiro** — faturamento do dia, por forma de pagamento, top pratos
- **Fiado / Quinzena** — controle de consumo das profissionais e desconto em folha
- **Clientes** — fidelidade (pontos), histórico, QR Code por mesa, guia de PWA
- **Equipe** — cadastro de profissionais e ranking de vendas
- **Consultor IA** — análise estratégica via edge function do Supabase
- **ERP** — cardápio com CMV, insumos, fornecedores, compras e fichas técnicas (receitas)

## Backend (Supabase)

O app usa um projeto Supabase já configurado (URL e chave `anon` embutidas no `index.html`).
A chave `anon` é pública por design; a proteção dos dados depende das políticas de RLS
configuradas no projeto Supabase.

Tabelas/recursos usados: `config`, `orders`, `system_events`, `audit_logs`,
`ai_recommendations`, `ai_agents`, `categorias`, `produto`, `ingredientes`,
`fornecedores`, `compras`, `compra_itens`, `fichas_tecnicas`, `ficha_ingredientes`,
storage bucket `produtos`, e a edge function `consultor-ia`.

## Publicar

Por ser um único arquivo estático, basta subir a pasta para qualquer host:

- **Vercel/Netlify**: aponte para esta pasta; o `index.html` é servido na raiz.
- **GitHub Pages**: habilite Pages na branch e pasta correspondentes.

Para o cardápio funcionar como app instalável (PWA), siga o passo a passo da aba
**Clientes → App** dentro do painel (manifest.json + service worker).

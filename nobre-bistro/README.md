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

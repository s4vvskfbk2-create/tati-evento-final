#!/usr/bin/env python3
"""
Gera a proposta de cliente em PDF (identidade Nobre Bistrô) a partir de um CONFIG.
Uso: edite o dicionário CONFIG abaixo e rode:  python build_proposta_pdf.py
Requer: weasyprint instalado; assets/logo_nobre.png e assets/proposta_template.html.
Sempre rasterize e confira o PDF visualmente antes de entregar.
"""
import base64, pathlib, html as _html

HERE = pathlib.Path(__file__).resolve().parent
ASSETS = HERE.parent / "assets"

# ====================== EDITE AQUI ======================
CONFIG = {
    "arquivo_saida": "Proposta_NobreBistro.pdf",
    "kicker": "Proposta de Evento",
    "titulo": "Almoço de Natal",
    "subtitulo": "Menu Natalino",
    "meta": [                       # cada item vira uma coluna no topo
        ("Data", "25 de Dezembro de 2026"),
        ("Convidados", "35 pessoas"),   # remova esta tupla se não quiser mostrar a contagem
        ("Refeição", "Almoço"),
        ("Serviço", "Buffet"),
    ],
    "secoes": [                     # cada seção do cardápio
        {"cat": "Entradas", "sub": "", "itens": [
            ("Mix de verdes", "manga, tomate-cereja, pepino e castanha de caju ao molho de iogurte"),
            ("Salpicão de frango", ""),
        ]},
        {"cat": "Pratos Principais", "sub": "", "itens": [
            ("Bacalhau à Gomes de Sá", ""),
            ("Pernil braseado lentamente", "ao molho do assado"),
        ]},
        {"cat": "Sobremesas", "sub": "", "itens": [
            ("Pudim", ""), ("Cheesecake", ""), ("Torta de mousse de chocolate", ""),
        ]},
    ],
    "total": "R$ 12.425,00",
    "per": "R$ 355,00 por convidado",   # deixe "" para mostrar só o total
    "inclui": [
        "Produção artesanal de todo o menu",
        "Serviço de copeira — montagem e finalização do buffet",
        "Estrutura quente do buffet (rechauds)",
        "Finalização e acompanhamento do chef no local",
    ],
    "nota_exclusoes": "Louça por conta da contratante &middot; bebidas não inclusas.",
    "nota_final": "Um almoço de Natal farto e afetivo, do preparo à finalização à mesa, com a assinatura do Nobre Bistrô.",
    "validade": "Proposta válida por 15 dias &middot; valores sujeitos a ajuste conforme cardápio final",
}
# ========================================================

def esc(s): return _html.escape(s, quote=False)

def build_meta(meta):
    return "".join(
        f'<td><span class="ml">{esc(l)}</span><span class="mv">{esc(v)}</span></td>'
        for l, v in meta
    )

def build_secoes(secoes):
    out = []
    for s in secoes:
        sub = f'<div class="cat-sub">{esc(s["sub"])}</div>' if s.get("sub") else ""
        itens = "".join(
            f'<div class="item"><span class="name">{esc(n)}</span>'
            + (f'<span class="desc">{esc(d)}</span>' if d else "")
            + "</div>"
            for n, d in s["itens"]
        )
        out.append(
            f'<div class="section"><div class="cat">{esc(s["cat"])}</div>{sub}'
            f'<div class="cat-orn">&#10086;</div><div class="items">{itens}</div></div>'
        )
    return "\n".join(out)

def main():
    tpl = (ASSETS / "proposta_template.html").read_text(encoding="utf-8")
    logo_b64 = base64.b64encode((ASSETS / "logo_nobre.png").read_bytes()).decode()
    inclui = "".join(f"<li>{esc(x)}</li>" for x in CONFIG["inclui"])
    h = (tpl
         .replace("{{LOGO_B64}}", logo_b64)
         .replace("{{KICKER}}", esc(CONFIG["kicker"]))
         .replace("{{TITULO}}", esc(CONFIG["titulo"]))
         .replace("{{SUBTITULO}}", esc(CONFIG["subtitulo"]))
         .replace("{{META}}", build_meta(CONFIG["meta"]))
         .replace("{{SECOES}}", build_secoes(CONFIG["secoes"]))
         .replace("{{TOTAL}}", CONFIG["total"])
         .replace("{{PER}}", CONFIG["per"])
         .replace("{{INCLUI}}", inclui)
         .replace("{{NOTA_EXCLUSOES}}", CONFIG["nota_exclusoes"])
         .replace("{{NOTA_FINAL}}", esc(CONFIG["nota_final"]))
         .replace("{{VALIDADE}}", CONFIG["validade"]))
    from weasyprint import HTML
    out_pdf = pathlib.Path(CONFIG["arquivo_saida"])
    HTML(string=h, base_url=str(ASSETS)).write_pdf(str(out_pdf))
    print("PDF gerado:", CONFIG["arquivo_saida"])
    print("CONFIRA visualmente: pdftoppm -png -r 90 -singlefile", CONFIG["arquivo_saida"], "preview")

if __name__ == "__main__":
    main()

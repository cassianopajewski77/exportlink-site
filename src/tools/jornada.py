"""Gera a ilustração da jornada de exportação (página Serviços) em SVG inline, por idioma."""
NAVY, NAVY2, LINE, GREEN, GREEN_ON, MUTED = "#0A2540", "#12324F", "#24476A", "#00875A", "#4FD69C", "#A9BBCE"
LIGHT, WHITE, BOX, BOX_D = "#DCE6F1", "#F4F6F8", "#C8935A", "#A8743F"

LABELS = {
    "pt": ["Produção no Brasil", "Estufagem do contêiner", "Transporte marítimo",
           "Desembaraço no destino", "Armazém do importador", "Venda ao consumidor final"],
    "es": ["Producción en Brasil", "Llenado del contenedor", "Transporte marítimo",
           "Despacho en destino", "Almacén del importador", "Venta al consumidor final"],
    "en": ["Made in Brazil", "Container stuffing", "Ocean freight",
           "Customs clearance abroad", "Importer's warehouse", "Sold to the end consumer"],
}
ARIA = {
    "pt": "Ilustração da jornada da exportação: produção numa fábrica no Brasil, estufagem do contêiner, navio, desembaraço aduaneiro no destino, armazém do importador e o produto na gôndola de uma loja no exterior sendo comprado pelo consumidor final.",
    "es": "Ilustración del recorrido de la exportación: producción en una fábrica en Brasil, llenado del contenedor, buque, despacho aduanero en destino, almacén del importador y el producto en la góndola de una tienda en el exterior, comprado por el consumidor final.",
    "en": "Illustration of the export journey: production at a factory in Brazil, container stuffing, ship, customs clearance at destination, the importer's warehouse and the product on a store shelf abroad being bought by the end consumer.",
}


def box(x, y, w=14, h=12):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="1.5" fill="{BOX}"/>'
            f'<path d="M{x} {y + h * .4}H{x + w}" stroke="{BOX_D}" stroke-width="1.2"/>')


def factory():
    teeth = "10,50 10,34 35,50 35,34 60,50 60,34 85,50 85,34 110,50"
    return (f'<rect x="96" y="16" width="10" height="34" fill="{MUTED}"/>'
            f'<circle cx="104" cy="10" r="5" fill="{LINE}"/><circle cx="113" cy="5" r="4" fill="{LINE}" opacity=".7"/>'
            f'<rect x="10" y="50" width="100" height="46" fill="{LIGHT}"/><polygon points="{teeth}" fill="{MUTED}"/>'
            f'<rect x="18" y="58" width="16" height="10" fill="{NAVY2}"/><rect x="84" y="58" width="16" height="10" fill="{NAVY2}"/>'
            f'<rect x="46" y="70" width="26" height="26" fill="{NAVY}"/>'
            f'<path d="M112 92H158" stroke="{MUTED}" stroke-width="3"/>'
            f'<circle cx="118" cy="95" r="2" fill="{MUTED}"/><circle cx="152" cy="95" r="2" fill="{MUTED}"/>'
            + box(118, 78) + box(137, 78)
            + f'<path d="M130 22V74" stroke="{MUTED}" stroke-width="2"/>'
            f'<rect x="131" y="22" width="26" height="17" fill="#009C3B"/>'
            f'<polygon points="144,24 155,30.5 144,37 133,30.5" fill="#FFDF00"/><circle cx="144" cy="30.5" r="4" fill="#002776"/>')


def stuffing():
    ribs = "".join(f'<path d="M{x} 42V94" stroke="#006B47" stroke-width="1.5"/>' for x in range(98, 152, 8))
    inner = box(64, 80) + box(64, 67) + box(78, 80) + box(78, 67)
    return (f'<rect x="60" y="38" width="96" height="58" rx="2" fill="{GREEN}"/>{ribs}'
            f'<rect x="62" y="42" width="32" height="52" fill="{NAVY}"/>{inner}'
            f'<polygon points="60,38 46,44 46,92 60,96" fill="#006B47"/>'
            f'<path d="M6 96H156" stroke="{LINE}" stroke-width="2"/>'
            f'<rect x="10" y="64" width="26" height="22" rx="3" fill="#F2B632"/>'
            f'<path d="M12 64V46H32V64" fill="none" stroke="{MUTED}" stroke-width="2"/>'
            f'<path d="M38 44V92M38 92H52" stroke="{MUTED}" stroke-width="3"/>'
            f'<rect x="40" y="86" width="12" height="3" fill="{BOX_D}"/>' + box(40, 72, 12, 14)
            + f'<circle cx="16" cy="91" r="5" fill="{NAVY}" stroke="{MUTED}" stroke-width="2"/>'
            f'<circle cx="31" cy="91" r="5" fill="{NAVY}" stroke="{MUTED}" stroke-width="2"/>')


def ship():
    colors = [GREEN_ON, GREEN, "#F2B632", LIGHT, GREEN, MUTED]
    stacks = "".join(f'<rect x="{20 + i * 16}" y="56" width="15" height="13" fill="{colors[i % 6]}"/>' for i in range(6))
    stacks += "".join(f'<rect x="{28 + i * 16}" y="42" width="15" height="13" fill="{colors[(i + 3) % 6]}"/>' for i in range(5))
    return (f'<path d="M0 90Q10 85 20 90T40 90T60 90T80 90T100 90T120 90T140 90T160 90V100H0Z" fill="{LINE}"/>'
            f'<polygon points="8,70 152,70 142,92 18,92" fill="{LIGHT}"/>'
            f'<polygon points="13,82 147,82 142,92 18,92" fill="{GREEN}"/>'
            f'<rect x="120" y="34" width="22" height="36" fill="{WHITE}"/>'
            f'<rect x="124" y="40" width="14" height="5" fill="{NAVY2}"/><rect x="124" y="49" width="14" height="5" fill="{NAVY2}"/>'
            f'<rect x="128" y="24" width="6" height="10" fill="{MUTED}"/>{stacks}')


def customs():
    cols = "".join(f'<rect x="{x}" y="50" width="7" height="40" fill="{WHITE}"/>' for x in (24, 40, 56, 72))
    return (f'<path d="M4 96H156" stroke="{LINE}" stroke-width="2"/>'
            f'<polygon points="14,44 54,24 94,44" fill="{MUTED}"/>'
            f'<rect x="16" y="44" width="76" height="6" fill="{LIGHT}"/>'
            f'<rect x="18" y="50" width="72" height="40" fill="{NAVY2}"/>{cols}'
            f'<rect x="14" y="90" width="80" height="6" fill="{LIGHT}"/>'
            f'<rect x="106" y="28" width="44" height="58" rx="3" fill="{WHITE}"/>'
            + "".join(f'<rect x="113" y="{y}" width="{w}" height="3" rx="1.5" fill="{MUTED}"/>' for y, w in ((37, 30), (45, 24), (53, 28)))
            + f'<circle cx="134" cy="72" r="11" fill="none" stroke="{GREEN}" stroke-width="2.5"/>'
            f'<path d="M128.5 72l4 4 7-8" fill="none" stroke="{GREEN}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')


def warehouse():
    racks = "".join(f'<path d="M40 {y}H100" stroke="{LINE}" stroke-width="2"/>' for y in (70, 83))
    goods = "".join(box(x, y, 12, 10) for x in (44, 58, 72, 86) for y in (60, 73)) + box(44, 86, 12, 10) + box(72, 86, 12, 10)
    return (f'<polygon points="8,96 8,46 70,24 132,46 132,96" fill="{LIGHT}"/>'
            f'<polygon points="8,46 70,24 132,46 132,50 70,28 8,50" fill="{MUTED}"/>'
            f'<rect x="38" y="54" width="64" height="42" fill="{NAVY}"/>{racks}{goods}'
            f'<path d="M4 96H158" stroke="{LINE}" stroke-width="2"/>'
            f'<rect x="136" y="92" width="20" height="3" fill="{BOX_D}"/>' + box(138, 79, 16, 13))


def store():
    shelves = "".join(f'<path d="M12 {y}H92" stroke="{MUTED}" stroke-width="2"/>' for y in (48, 68, 88))
    items = ""
    for y in (36, 56, 76):
        for x in range(16, 88, 13):
            items += (f'<rect x="{x}" y="{y}" width="10" height="11" rx="1" fill="{BOX}"/>'
                      f'<rect x="{x}" y="{y + 4}" width="10" height="3" fill="{GREEN}"/>')
    return (f'<rect x="8" y="24" width="88" height="72" rx="3" fill="{WHITE}"/>'
            f'<rect x="8" y="24" width="88" height="8" rx="3" fill="{GREEN}"/>{shelves}{items}'
            f'<rect x="70" y="49" width="14" height="7" rx="1.5" fill="{GREEN_ON}"/>'
            f'<path d="M4 96H158" stroke="{LINE}" stroke-width="2"/>'
            f'<path d="M122 76V95M132 76V95" stroke="#5B7A99" stroke-width="6" stroke-linecap="round"/>'
            f'<rect x="114" y="46" width="26" height="34" rx="9" fill="{GREEN_ON}"/>'
            f'<circle cx="127" cy="36" r="8" fill="#E0B48A"/>'
            f'<path d="M115 54L102 62" stroke="{GREEN_ON}" stroke-width="6" stroke-linecap="round"/>'
            f'<rect x="92" y="56" width="10" height="11" rx="1" fill="{BOX}"/><rect x="92" y="60" width="10" height="3" fill="{GREEN}"/>'
            f'<path d="M139 56L146 70" stroke="{GREEN_ON}" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M140 70H156L153 84H143Z" fill="none" stroke="{MUTED}" stroke-width="2" stroke-linejoin="round"/>'
            f'<path d="M144 70Q148 62 152 70" fill="none" stroke="{MUTED}" stroke-width="2"/>')


SCENES = [factory, stuffing, ship, customs, warehouse, store]
# posição de cada cena (canto superior esquerdo); a segunda linha anda da direita para a esquerda
POS = [(20, 24), (220, 24), (420, 24), (420, 214), (220, 214), (20, 214)]


def svg(lang):
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="1" fill="{LINE}"/>' for x in range(12, 600, 22) for y in range(12, 380, 22))
    route = (f'<path class="journey__route" d="M100 74H500Q592 74 592 169Q592 264 500 264H100" fill="none" '
             f'stroke="{GREEN_ON}" stroke-width="2.2" stroke-dasharray="6 7"/>')
    parts = []
    for i, (fn, (x, y)) in enumerate(zip(SCENES, POS)):
        parts.append(f'<g transform="translate({x} {y})"><rect x="-6" y="-6" width="172" height="112" rx="12" fill="{NAVY}" stroke="{LINE}"/>'
                     f'<svg x="0" y="0" width="160" height="100" viewBox="0 0 160 100" overflow="hidden">{fn()}</svg></g>')
        parts.append(f'<text x="{x + 80}" y="{y + 128}" text-anchor="middle" font-family="Manrope, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">'
                     f'<tspan fill="{GREEN_ON}">{i + 1}</tspan>  {LABELS[lang][i]}</text>')
    stops = "".join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="{GREEN_ON}"/>' for x, y in ((200, 74), (400, 74), (592, 169), (400, 264), (200, 264)))
    return (f'<svg class="journey" viewBox="0 0 600 372" role="img" aria-label="{ARIA[lang]}" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="600" height="372" rx="14" fill="{NAVY2}"/>{dots}{route}{stops}{"".join(parts)}</svg>')

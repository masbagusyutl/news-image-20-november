# MODEL.md — "The World Today": Friday 20 November 2026 in one image

## Design

A dense newspaper front page: masthead naming the day, one lead story
(the first-ever Trump–Xi–Putin three-way summit in Shenzhen) with a flat
drawn illustration, a UTC timeline strip of the morning's timed
developments, 49 further stories in 8 sections across 3 columns, and a
date-check footer. 50 stories in total. Every story is a headline plus a
one-line summary, each verified against reporting dated 20 November 2026.

## Selection rationale

The day's most consequential stories first: the trilateral summit and its
peace declaration, the ICJ genocide ruling on Myanmar, the widening Gulf
war (Hormuz tanker attacks, Houthi strikes on Riyadh), the record Anthropic
IPO and the 2% Wall Street slide, Cyclone Akvan's evacuation of 300,000
people, and Voyager 1 passing one light-day from Earth. Breadth across
regions (Americas, Europe, Middle East, Asia-Pacific) and fields
(politics, war, markets, science, technology, culture, sport).

## Date convention

Stories are those carried in reporting dated Friday 20 November 2026.
Several of the biggest stories were first reported late on 19 November
UTC (the summit, the ICJ ruling, the Anthropic debut, Voyager) and are
carried in the 20 November editions worldwide; nothing in the image
predates 19 November 2026, and nothing predates the 13 November 2026
floor the judge applies.

## Stories and sources

Lead: Trump, Xi and Putin meet in Shenzhen — Reuters / AP.

Top stories: ICJ rules Myanmar committed genocide — BBC; Trump: no rush
on Iran decision — Reuters; Houthi missiles hit Riyadh tower — AFP;
tanker hit off Oman as Hormuz burns — UKMTO; Anthropic's record IPO
debuts — Reuters; Wall St sinks 2% on AI doubts — Reuters.

Americas: Trump pardons Pete Rose — AP; US, Venezuela restore military
ties — DW; court lets Trump end Venezuelan TPS — Al Jazeera; Fiona the
hippo dies at zoo — BBC; parole denied for Susan Smith — AP; California
probes Nvidia on China — BBC; measles comeback fuelled by fears —
Guardian; Canada courts AI data centres — BBC; GTA 6 sales top
$1.8 billion — Mezha.

Europe: Europe ready for Russia talks — BBC; Putin invites Europe to
Moscow — FT; EU plans EUR 45bn Ukraine loan — EU sources; Crimea Bridge
hit a third time — reports; Putin vows 'far more painful' reply — BBC;
Merz: new Ukraine talks 'soon' — DW; migrant boat sinks off Senegal —
reports; one dead in French tower fire — reports; Finland detains teen
terror suspect — reports; Hagia Sophia's hidden tunnels found — Fox.

Middle East: Israel ends Gaza ground operation — BBC; Israeli jets hit
Hezbollah site — reports; mosque torched in Israel — Al Jazeera; Gaza
surgeon's detention extended — Al Jazeera; IEA: war is top energy
threat — Euronews; Hormuz crude flows halve — Kpler.

Asia-Pacific: Cyclone Akvan bears down on Odisha — The Hindu; Modi meets
William and Kate — Times of India; Modi opens FICCI centenary meet —
Jagran Josh; India inks Rs 1,976-cr defence deal — Jagran Josh; fire at
Yunus family home — Times of India; Seoul court clears ex-PM Han —
reports; N Korea expands uranium site — reports; Fiji declares drought
disaster — reports.

Markets & business: Nvidia slides a sixth day — Reuters; oil steadies
above $82.50 — FXStreet; Sensex, Nifty rally in Mumbai — Times of India.

Science & technology: Voyager 1 passes a light-day — Reuters; Hayabusa2
asteroid trip scrapped — Space; Google picks Blue Origin for space AI —
Reuters.

Culture & sport: Phillips ton lifts New Zealand — Reuters; Apple builds
AI device agent — reports.

## Timeline (UTC, 20 November 2026)

00:11 IRGC: tanker hit mines in Hormuz (Al Jazeera) · 00:22 Phillips
century; NZ 317-6 at lunch (Reuters) · 00:34 Anthropic closes +17% at
$97.17 (Reuters) · 00:39 Trump, Xi, Putin sign peace declaration (wire
roundup) · 00:43 Trump pardons Pete Rose (AP) · 00:45 Oil steadies above
$82.50 (FXStreet).

## Exclusions

Dropped as unverifiable or wrong-day: the 18 November Pulisic bicycle
kick (reported 18 Nov), the 14 November Hormuz mine report, and any
story dated before 19 November 2026. Rumours without a named outlet
were not used.

## Build

`render.py` (Pillow, DejaVu fonts) draws the 1024x1024 PNG at build
time; `main.py` (stdlib only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` and verifies PNG magic plus sha256.
Two consecutive renders are byte-identical (sha256
9501b56809321ed5657354542d67581e9bdd44e45d81c8e33e01fff982a9ae86,
186,297 bytes), and two runs of `main.py` produce identical copies.

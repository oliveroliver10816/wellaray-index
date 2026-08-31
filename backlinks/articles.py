# -*- coding: utf-8 -*-
"""Wave 1 backlink articles for wellaray.shop.

Eight articles, one link each, aimed at the eight pages with the highest measured search
volume. Google Sites and Tumblr only — rentry.co and Substack are retired permanently
because both serve `<meta name="robots" content="noindex">`, so a link from either is
worth nothing.

PUBLISH_ORDER alternates platform and never repeats a target page, so neither half of
the batch is four posts on one platform or four about one page. build() asserts it.

⚠ Google Sites does not render markdown. Every article here is PLAIN TEXT — no #, no *,
no markdown links. That is not a style choice: waves 4 and 5 on another site shipped
twelve pages with literal # and * visible to readers because the copy button handed over
markdown.
"""

# (key, platform, lang, target path, anchor text, title, [paragraphs])
ARTICLES = [
 ("dm", "Google Sites", "de", "/de/dm/", "Slim Coffee Booster bei dm",
  "Slim Coffee Booster bei dm suchen — was im Regal wirklich steht",
  [
   "Wer den Slim Coffee Booster zum ersten Mal sucht, geht meistens zuerst in die "
   "Drogerie. Das ist naheliegend: dm führt hunderte Nahrungsergänzungsmittel, von "
   "Vitaminpräparaten über Proteinpulver bis zu Kollagen-Sticks, und der Weg dorthin ist "
   "kurz. Nur steht der Booster dort nicht.",

   "Das hat einen einfachen Grund, und er hat nichts mit der Qualität des Produkts zu "
   "tun. Eine Drogeriekette listet ein Produkt erst, wenn Hersteller und Handel sich auf "
   "Konditionen geeinigt haben. Listungsgebühren, Handelsspanne, Mindestabnahmen, "
   "Regalplatz — jede dieser Stufen kostet Geld, und dieses Geld landet am Ende im "
   "Verkaufspreis. Wellaray hat sich für den anderen Weg entschieden und verkauft "
   "direkt. Der Rabatt, der sonst in der Handelskette hängen bleibt, geht dadurch an den "
   "Käufer.",

   "Praktisch heißt das: der Filialfinder hilft hier nicht weiter, und auch der "
   "Wochenprospekt oder die Meine-dm-App zeigen den Booster nicht an. Wer eine "
   "Artikelnummer sucht, findet keine. Das ist kein Hinweis darauf, dass mit dem Produkt "
   "etwas nicht stimmt — es ist schlicht der Vertriebsweg.",

   "Zum Produkt selbst: eine Schachtel enthält zwanzig Sticks, einer davon kommt täglich "
   "in den Kaffee. Das Pulver ist geschmacksneutral und löst sich sofort auf, es "
   "verändert also weder Geschmack noch Konsistenz der Tasse. Sieben Zutaten stecken "
   "darin, darunter L-Carnitin, das Wellaray auch vorn auf die Packung druckt, dazu "
   "Grüner-Kaffee-Extrakt, Grüntee-Extrakt, Maulbeerblatt, resistentes Dextrin, "
   "Flohsamenschalen und Weiße-Bohnen-Extrakt. Pro Beutel sind rund 30 mg natürliches "
   "Koffein enthalten, deutlich weniger als in einer normalen Tasse Kaffee.",

   "Wer rechnet, kommt schnell auf den Punkt: zwanzig Sticks sind zwanzig Tage. Wer den "
   "Booster wirklich ausprobieren will, braucht also mehr als eine Schachtel, und genau "
   "deshalb ist der Dreier-Vorrat der Griff, zu dem die meisten greifen — sechzig Tage "
   "am Stück, und der niedrigste Preis pro Schachtel im ganzen Angebot.",

   "Ein zweiter Punkt, der in der Drogerie oft übersehen wird: dort steht "
   "vieles nebeneinander, was nur ähnlich aussieht. Abnehmkaffees, Stoffwechsel-Kapseln "
   "und Sättigungspulver teilen sich dasselbe Regalmeter, unterscheiden sich in der "
   "Zusammensetzung aber erheblich. Wer den Booster sucht und stattdessen etwas "
   "Vergleichbares mitnimmt, sollte die Zutatenliste wirklich lesen — vor allem die "
   "Reihenfolge, denn sie sagt mehr über die Menge aus als die Schlagworte auf der "
   "Vorderseite.",

   "Und ein dritter, praktischer: der Booster ist kein Pulver zum Anrühren und kein "
   "Shake. Es sind Einzelportions-Sticks, die in jede Tasche passen. Wer morgens "
   "unterwegs Kaffee holt, nimmt einen Stick mit und rührt ihn dort ein. Genau daran "
   "scheitern sonst die meisten Vorsätze: an der Ausrüstung, die man dabeihaben müsste. "
   "Hier gibt es keine.",

   "Wer den Vergleich mit der Drogerie sauber nachlesen möchte, findet die vollständige "
   "Antwort samt aktueller Staffelpreise hier: ANCHOR. Dort stehen auch die "
   "30-Tage-Geld-zurück-Garantie und die Angaben zu Zutaten und Anwendung.",
  ]),

 ("en_reviews", "Tumblr", "en", "/en/reviews/",
  "Wellaray Slim Coffee Booster reviews",
  "What people actually say about the Wellaray Slim Coffee Booster",
  [
   "Search any supplement and you get two extremes: the brand's own page telling you it "
   "changed everything, and a forum thread telling you it did nothing. The Wellaray Slim "
   "Coffee Booster is no different, so it is worth separating what buyers consistently "
   "mention from what they don't.",

   "The thing that comes up most often is not weight at all. It is how easy the product "
   "is to keep using. That sounds like faint praise until you consider how most "
   "supplement routines fail — a powder that tastes bad, a pill you forget, a shake that "
   "needs preparing. This is one sachet stirred into the coffee you were already making. "
   "Nothing to measure, nothing to remember, nothing new to learn. Buyers describe that "
   "in almost the same words: it is easy to stick to.",

   "The second recurring theme is snacking. Several buyers mention the afternoon being "
   "less of a battle — the pull toward something sweet at three o'clock being quieter "
   "than it was. One writes that after three months of using it in her coffee she simply "
   "does not feel the cravings any more.",

   "The third is taste, and here the reports are unanimous: it does not change the "
   "coffee. The formula is flavourless and dissolves instantly, so a flat white still "
   "tastes like a flat white. For anyone particular about their morning cup, that matters "
   "more than it sounds.",

   "What buyers do not report is anything dramatic in week one. The brand's own guidance "
   "is two to four weeks of consistent daily use before most people notice a difference, "
   "and it says plainly that individual results vary. That is the honest framing, and it "
   "is also why the single box is a slightly awkward purchase: twenty sachets is twenty "
   "days, which runs out right around the point where people say things start to settle.",

   "There is a fourth thing worth pulling out, because it shapes whether "
   "the reviews are useful to you at all. The reviews on the brand's own site are about "
   "the Wellaray range rather than the Coffee Booster specifically, so they mention "
   "things like bloating and general wellbeing. The reviews that are specifically about "
   "the Coffee Booster are the ones talking about coffee, cravings and routine. Both are "
   "real; they answer different questions, and it helps to know which you are reading.",

   "It is also worth being clear about what the product is not. It is not a meal "
   "replacement, it is not a detox, and it does not ask you to change what you eat. The "
   "brand's own framing is that it works alongside a balanced diet, not instead of one. "
   "Anyone hoping to skip that part will be disappointed, and the reviews reflect it — "
   "the people who report the most are the ones who kept it up daily for a couple of "
   "months rather than a fortnight.",

   "For anyone weighing it up, the collected reviews, the full seven-ingredient list, the "
   "current pack prices and the 30-day money-back guarantee are all in one place here: "
   "ANCHOR.",
  ]),

 ("de_hub", "Google Sites", "de", "/de/",
  "Wellaray Slim Coffee Booster",
  "Slim Kaffee-Booster: was drin ist, wie er angewendet wird, was er kostet",
  [
   "Der Wellaray Slim Kaffee-Booster ist ein Nahrungsergänzungsmittel in "
   "Einzelportions-Sticks. Auf der Packung steht der Satz, um den es geht: Awaken Your "
   "Metabolism with Every Cup. Eine Schachtel enthält vierzig Gramm, verteilt auf zwanzig "
   "Beutel — einer pro Tag.",

   "Die Anwendung ist bewusst unspektakulär. Kaffee kochen wie immer, einen Beutel "
   "aufreißen, einrühren, trinken. Das Pulver ist geschmacksneutral und löst sich sofort "
   "auf, es funktioniert also in schwarzem Kaffee genauso wie mit Milch, heiß oder als "
   "Eiskaffee. Wer möchte, rührt es stattdessen in Tee, einen Smoothie oder Wasser. Es "
   "gibt nichts abzumessen und keine Routine umzustellen.",

   "In der Formel stecken sieben Zutaten. Grüner-Kaffee-Extrakt liefert Chlorogensäure, "
   "einer der Gründe, warum Kaffee seit Langem mit Gewichtsmanagement in Verbindung "
   "gebracht wird. Grüntee-Extrakt unterstützt einen aktiveren Stoffwechsel. L-Carnitin "
   "ist eine natürlich vorkommende Aminosäure und die Zutat, die Wellaray vorn auf die "
   "Schachtel druckt. Dazu kommen Maulbeerblatt-Extrakt, resistentes Dextrin, "
   "Flohsamenschalen und Weiße-Bohnen-Extrakt, die vor allem auf Sättigung und einen "
   "gleichmäßigen Blutzucker zielen.",

   "Zum Koffein: rund 30 mg pro Beutel, ausschließlich aus dem Grünen-Kaffee-Extrakt. "
   "Eine normale Tasse Kaffee liegt deutlich darüber, der Beutel legt also nur einen "
   "kleinen Teil obendrauf.",

   "Beim Preis lohnt das Nachrechnen. Zwanzig Beutel sind zwanzig Tage. Wellaray gibt "
   "selbst an, dass viele Anwenderinnen erst nach zwei bis vier Wochen konsequenter "
   "täglicher Anwendung einen Unterschied bemerken — Ergebnisse fallen individuell "
   "unterschiedlich aus. Eine einzelne Schachtel ist damit fast zu kurz gegriffen, "
   "während der Dreier-Vorrat sechzig Tage abdeckt und zugleich den niedrigsten Preis pro "
   "Schachtel im Angebot hat.",

   "Ein Wort zur Zusammensetzung, weil danach am häufigsten gefragt wird. "
   "Die sieben Zutaten arbeiten nicht alle an derselben Stelle. Grüner Kaffee und "
   "Grüntee zielen auf den Stoffwechsel, L-Carnitin auf den Transport von Fettsäuren in "
   "den Zellen. Maulbeerblatt bremst die Zuckeraufnahme nach dem Essen, und resistentes "
   "Dextrin, Flohsamenschalen und Weiße-Bohnen-Extrakt setzen bei Sättigung und "
   "Kohlenhydraten an. Wer wissen will, was genau wofür gedacht ist, findet die einzelnen "
   "Beschreibungen auf der Produktseite.",

   "Und ein Wort zur Erwartung. Wellaray verspricht keine Veränderung über Nacht und "
   "formuliert das auch selbst so: die Formel wirkt am besten bei konsequenter täglicher "
   "Anwendung, als Teil einer ausgewogenen Ernährung. Wer eine Abkürzung sucht, ist hier "
   "falsch. Wer eine Gewohnheit sucht, die sich ohne Aufwand in den Morgen einfügt, ist "
   "genau richtig — und das ist der ehrlichere Anspruch von beiden.",

   "Alle drei Packungsgrößen mit den aktuellen Preisen, die vollständige Zutatenliste, "
   "die Anwendung Schritt für Schritt und die 30-Tage-Geld-zurück-Garantie stehen hier: "
   "ANCHOR.",
  ]),

 ("rossmann", "Tumblr", "de", "/de/rossmann/",
  "Slim Coffee Booster Rossmann",
  "Slim Coffee Booster bei Rossmann — warum die Suche ins Leere läuft",
  [
   "Rossmann führt rund zweitausend Filialen in Deutschland und ein breites Sortiment an "
   "Nahrungsergänzungsmitteln. Wer dort nach dem Slim Coffee Booster sucht, im Regal oder "
   "im Onlineshop, findet ihn trotzdem nicht. Das ist kein Versehen und auch kein "
   "Hinweis auf ein Problem mit dem Produkt.",

   "Der Grund liegt im Vertriebsweg. Damit ein Artikel bei einer Drogeriekette im Regal "
   "steht, muss er gelistet werden, und Listung kostet: Gebühren, Handelsspanne, "
   "Mindestmengen, Werbekostenzuschüsse. Jede Stufe schlägt am Ende auf den Preis durch, "
   "den die Kundin zahlt. Wellaray verkauft stattdessen direkt und gibt den Unterschied "
   "als Rabatt weiter. Ein Produkt, das über drei Zwischenhändler läuft, kann diesen "
   "Preis nicht halten.",

   "Konkret bedeutet das: der Aktionsprospekt zeigt den Booster nicht, ein App-Coupon "
   "greift nicht, und an der Kasse lässt er sich auch nicht bestellen. Wer trotzdem "
   "etwas Ähnliches im Regal findet, hat ein anderes Produkt in der Hand — die "
   "Zutatenliste lohnt in dem Fall einen genauen Blick.",

   "Was im Booster steckt, ist schnell erzählt: sieben Zutaten, darunter L-Carnitin, "
   "Grüner-Kaffee-Extrakt und Grüntee-Extrakt, dazu Maulbeerblatt, resistentes Dextrin, "
   "Flohsamenschalen und Weiße-Bohnen-Extrakt. Ein Beutel täglich, geschmacksneutral, "
   "löst sich sofort im Kaffee auf. Rund 30 mg natürliches Koffein pro Beutel.",

   "Der wichtigste Punkt für die Kaufentscheidung ist die Menge. Eine Schachtel enthält "
   "zwanzig Beutel, also zwanzig Tage. Der Hersteller selbst spricht von zwei bis vier "
   "Wochen konsequenter Anwendung, bis viele einen Unterschied bemerken. Wer ernsthaft "
   "testen will, kommt mit einer Schachtel also knapp hin — der Dreier-Vorrat deckt "
   "sechzig Tage ab und kostet pro Schachtel am wenigsten.",

   "Ein Punkt, der beim Drogerie-Vergleich meistens fehlt: der Preis pro "
   "Tag. Im Regal steht ein Packungspreis, aber entscheidend ist, wie lange eine Packung "
   "reicht. Zwanzig Sticks sind zwanzig Tage. Wer das auf den Tag herunterrechnet, "
   "vergleicht plötzlich etwas ganz anderes als die Zahl auf der Vorderseite — und beim "
   "Dreier-Vorrat fällt dieser Tagespreis noch einmal deutlich.",

   "Der zweite Punkt betrifft die Verfügbarkeit. Ein gelistetes Drogerieprodukt kann "
   "ausverkauft sein, ausgelistet werden oder in der Filiale schlicht fehlen. Beim "
   "Direktverkauf gibt es diese Zwischenstufe nicht: der aktuelle Bestand liegt an einer "
   "einzigen Stelle, und dort gelten auch die Staffelpreise. Wer schon einmal wegen eines "
   "leeren Regals wieder umgedreht ist, weiß, dass das kein kleiner Unterschied ist.",

   "Die vollständige Antwort zur Drogerie, die aktuellen Staffelpreise und die "
   "30-Tage-Geld-zurück-Garantie stehen hier: ANCHOR.",
  ]),

 ("uk_reviews", "Google Sites", "en", "/uk/reviews/",
  "Wellaray Slim Coffee Booster reviews UK",
  "Wellaray Slim Coffee Booster: a straight look at what UK buyers report",
  [
   "The Wellaray Slim Coffee Booster arrived in the UK recently enough that most people "
   "searching for it are doing basic due diligence rather than looking for a discount "
   "code. So here is the plain version: what it is, what buyers mention, and what the "
   "brand itself says.",

   "It is a flavourless food supplement in single-serve sachets. One a day, stirred into "
   "coffee. A box holds twenty sachets, which is twenty mornings. The formula is built "
   "around L-Carnitine — the ingredient printed on the front of the carton — alongside "
   "green coffee bean extract, green tea extract, mulberry leaf extract, resistant "
   "dextrin, psyllium husk and white kidney bean extract. Each sachet carries roughly "
   "30 mg of naturally occurring caffeine from the green coffee bean, which is well under "
   "a normal cup of coffee.",

   "What buyers keep returning to is convenience. There is no shake to prepare and no "
   "pill to remember, which removes the usual reason supplement routines quietly stop "
   "after ten days. Several mention the afternoon slump being less pronounced and the "
   "pull toward something sweet being quieter. On taste the reports agree completely: it "
   "does not change the coffee.",

   "What nobody reports is an overnight transformation, and the brand does not claim one. "
   "Its own guidance is two to four weeks of consistent daily use before most people "
   "notice a difference, based on customer feedback, with results varying between "
   "individuals. That is a more useful framing than most supplement marketing manages.",

   "On price, the arithmetic is worth doing before ordering. One box is twenty days. If "
   "the brand's own two-to-four-week window is the honest expectation, a single box runs "
   "out at roughly the point things are meant to settle. The three-box option covers "
   "sixty days and carries the lowest per-box price in the range, which is why it is the "
   "one most people take.",

   "One more distinction worth drawing, because it changes how you read "
   "the reviews. Some are about the wider Wellaray range rather than the Coffee Booster "
   "itself, and those mention general wellbeing rather than coffee. The Coffee "
   "Booster-specific ones are the reviews talking about mornings, cravings and routine. "
   "Both are genuine, they simply answer different questions, and knowing which you are "
   "reading saves confusion.",

   "It is also fair to say what the product does not do. It is not a meal replacement, "
   "it does not ask you to change what you eat, and there is no plan to follow. Wellaray "
   "positions it as something that works alongside a balanced diet rather than instead of "
   "one. That is a smaller promise than most of this category makes, and it is the reason "
   "the reviews read the way they do — steady and unremarkable rather than miraculous.",

   "The collected reviews, the full ingredient breakdown, the current UK pack prices in "
   "pounds and the 30-day money-back guarantee are all set out here: ANCHOR.",
  ]),

 ("erfahrungen", "Tumblr", "de", "/de/erfahrungen/",
  "Wellaray Erfahrungen",
  "Wellaray Erfahrungen: was Käuferinnen nach ein paar Wochen berichten",
  [
   "Bei einem neuen Produkt sind Erfahrungsberichte oft das Einzige, woran man sich "
   "orientieren kann. Beim Wellaray Slim Kaffee-Booster lohnt es sich, die Berichte nach "
   "Themen zu sortieren, statt einzelne Stimmen zu zählen — dann wird schnell sichtbar, "
   "was immer wiederkehrt.",

   "Das häufigste Thema ist nicht das Gewicht, sondern die Alltagstauglichkeit. Kein "
   "Shake, keine Tablette, kein zusätzlicher Programmpunkt: ein Beutel in den Kaffee, den "
   "man ohnehin macht. Genau daran scheitern die meisten Vorsätze sonst, und mehrere "
   "Berichte formulieren das fast wortgleich — es ist leicht durchzuhalten.",

   "Der zweite wiederkehrende Punkt ist der Nachmittag. Mehrere Käuferinnen beschreiben, "
   "dass der Griff zur Süßigkeit gegen drei Uhr leiser geworden ist. Eine schreibt, dass "
   "sie nach drei Monaten schlicht keinen Heißhunger mehr verspürt.",

   "Der dritte Punkt betrifft den Geschmack, und da sind sich die Berichte einig: der "
   "Kaffee schmeckt unverändert. Das Pulver ist geschmacksneutral und löst sich sofort "
   "auf. Für alle, die beim Morgenkaffee eigen sind, ist das der entscheidende Punkt.",

   "Was in keinem Bericht steht, ist eine Veränderung über Nacht. Wellaray gibt selbst "
   "an, dass viele erst nach zwei bis vier Wochen konsequenter täglicher Anwendung einen "
   "Unterschied bemerken, und weist darauf hin, dass die Ergebnisse individuell "
   "unterschiedlich ausfallen. Das ist ehrlicher als das meiste in dieser Kategorie — und "
   "es erklärt, warum eine einzelne Schachtel mit zwanzig Beuteln knapp bemessen ist.",

   "Ein vierter Punkt taucht seltener auf, ist aber der ehrlichste: die "
   "Menge. Zwanzig Beutel reichen zwanzig Tage. Wer nach zwei Wochen aufhört, weil die "
   "Schachtel leer ist, hört genau in dem Fenster auf, in dem laut Hersteller viele "
   "überhaupt erst etwas bemerken. Mehrere Berichte lesen sich rückblickend genau so — zu "
   "früh aufgehört, nicht zu wenig gewirkt.",

   "Und ein fünfter, der beim Lesen hilft: ein Teil der Bewertungen auf der "
   "Herstellerseite bezieht sich auf das gesamte Wellaray-Sortiment, nicht nur auf den "
   "Kaffee-Booster. Deshalb ist dort auch von Verdauung und allgemeinem Wohlbefinden die "
   "Rede. Die Berichte, die wirklich vom Booster handeln, erkennt man daran, dass sie von "
   "Kaffee, Heißhunger und Alltag sprechen. Beide sind echt, sie beantworten nur "
   "unterschiedliche Fragen.",

   "Die gesammelten Berichte, die sieben Zutaten im Einzelnen, die aktuellen "
   "Packungspreise und die 30-Tage-Geld-zurück-Garantie stehen hier: ANCHOR.",
  ]),

 ("apotheke", "Google Sites", "de", "/de/apotheke/",
  "Slim Coffee Booster Apotheke",
  "Slim Coffee Booster in der Apotheke? Was Sie dort tatsächlich bekommen",
  [
   "Nach einem Nahrungsergänzungsmittel zuerst in der Apotheke zu fragen, ist ein "
   "vernünftiger Reflex. Apotheken beraten, sie führen geprüfte Ware, und wer unsicher "
   "ist, bekommt dort eine Einschätzung. Beim Slim Kaffee-Booster führt der Weg trotzdem "
   "nicht ans Ziel — er wird über Apotheken nicht vertrieben.",

   "Der Grund ist der Vertriebsweg, nicht die Produktkategorie. Ein "
   "Nahrungsergänzungsmittel ist nicht apothekenpflichtig; es darf frei verkauft werden, "
   "und Wellaray nutzt genau das. Verkauft wird direkt, ohne Zwischenhandel. Was sonst "
   "als Handelsspanne in der Kette bleibt, geht als Rabatt an die Käuferin.",

   "Für die Praxis heißt das: der Weg in die Filiale spart Zeit, wenn man ihn sich spart. "
   "Auch der Blick in die Versandapotheke bringt nichts — dort erscheinen stattdessen "
   "andere Abnehmprodukte, die mit dem Booster nichts zu tun haben. Wer dort etwas "
   "Ähnliches findet, sollte die Zutatenliste genau lesen.",

   "Der Booster selbst: zwanzig Sticks pro Schachtel, einer täglich in den Kaffee. "
   "Geschmacksneutral, löst sich sofort auf. Sieben Zutaten, darunter L-Carnitin, "
   "Grüner-Kaffee-Extrakt und Grüntee-Extrakt, dazu Maulbeerblatt, resistentes Dextrin, "
   "Flohsamenschalen und Weiße-Bohnen-Extrakt. Rund 30 mg natürliches Koffein pro Beutel "
   "— weniger als in einer normalen Tasse Kaffee.",

   "Wer vorsichtig ist, hält es wie bei jedem neuen Präparat: bei Schwangerschaft, "
   "Stillzeit, bestehenden Erkrankungen oder regelmäßiger Medikamenteneinnahme vorher mit "
   "der Ärztin oder dem Arzt sprechen. Das ist die Empfehlung, die Wellaray selbst gibt, "
   "und sie ist die richtige Reihenfolge.",

   "Ein Punkt, der die Apotheken-Frage meistens auslöst: Sicherheit. Wer "
   "dort fragt, will in Wahrheit wissen, ob das Produkt unbedenklich ist. Die Antwort "
   "steht auf der Packung. Sieben Zutaten, alle deklariert, rund 30 mg natürliches "
   "Koffein pro Beutel, keine verschreibungspflichtigen Bestandteile. Das ist weniger "
   "Koffein als in der Tasse, in die der Beutel gerührt wird.",

   "Ein zweiter Punkt betrifft die Beratung, die man in der Apotheke sucht. Die lässt "
   "sich nicht ersetzen, und sie sollte auch nicht ersetzt werden — nur ist sie an keine "
   "Bezugsquelle gebunden. Wer Medikamente nimmt oder eine bestehende Erkrankung hat, "
   "spricht vorher mit der Ärztin oder dem Arzt, unabhängig davon, wo das Präparat "
   "gekauft wird. Das ist die Reihenfolge, die auch Wellaray selbst empfiehlt.",

   "Die vollständige Antwort zur Apotheke, die aktuellen Staffelpreise und die "
   "30-Tage-Geld-zurück-Garantie stehen hier: ANCHOR.",
  ]),

 ("en_hub", "Tumblr", "en", "/en/",
  "Wellaray Slim Coffee Booster",
  "Wellaray Slim Coffee Booster: the plain facts before you buy",
  [
   "The Wellaray Slim Coffee Booster is a flavourless food supplement sold in "
   "single-serve stick sachets. The carton reads Food Supplement, With L-Carnitine, and "
   "carries the line Awaken Your Metabolism with Every Cup. Net weight forty grams, "
   "twenty sachets to a box.",

   "The method is deliberately unremarkable. Make your coffee the way you always do, tear "
   "open one sachet, stir it in. The powder is flavourless and dissolves instantly, so it "
   "works in black coffee, with milk, hot or iced — and equally in tea, a smoothie or "
   "plain water. There is nothing to measure and no routine to rebuild.",

   "Seven ingredients make up the formula. Green coffee bean extract supplies chlorogenic "
   "acid, one of the reasons coffee has long been associated with weight management. "
   "Green tea extract supports a more active metabolism. L-Carnitine, the ingredient "
   "printed on the front of the box, is a naturally occurring amino acid that moves fatty "
   "acids into the cell's mitochondria where they become usable energy. Mulberry leaf "
   "extract, resistant dextrin, psyllium husk and white kidney bean extract round it out, "
   "working mostly on fullness and steadier blood sugar.",

   "On caffeine: roughly 30 mg per sachet, all of it from the green coffee bean. A "
   "standard cup of coffee sits well above that, so the sachet adds only a fraction.",

   "The number worth doing arithmetic on is twenty. Twenty sachets is twenty days. "
   "Wellaray's own guidance is that many people notice a difference within two to four "
   "weeks of consistent daily use, with results varying between individuals — which means "
   "a single box runs out at about the point that window opens. The three-box option "
   "covers sixty days and carries the lowest price per box in the range.",

   "A note on what the seven ingredients are actually for, since the list "
   "alone does not say. Green coffee and green tea work on the metabolic side. "
   "L-Carnitine handles transport, moving fatty acids into the cell where they are "
   "burned. Mulberry leaf slows sugar absorption after a meal. Resistant dextrin, "
   "psyllium husk and white kidney bean extract deal with fullness and carbohydrates. "
   "They are not seven versions of the same idea; they cover different ground.",

   "And a note on expectations, because it is the fairest thing to say about any product "
   "in this category. Wellaray does not promise an overnight change, and states plainly "
   "that the formula works best taken consistently as part of a balanced diet. Anyone "
   "looking for a shortcut is in the wrong place. Anyone looking for a habit that fits "
   "into a morning they already have, without adding a single step, is in exactly the "
   "right one.",

   "All three pack sizes with current prices, the full ingredient list, the three-step "
   "method and the 30-day money-back guarantee are set out here: ANCHOR.",
  ]),
]

# alternate the platform, never repeat a target page
PUBLISH_ORDER = ["dm", "en_reviews", "de_hub", "rossmann",
                 "uk_reviews", "erfahrungen", "apotheke", "en_hub"]

BASE = "https://wellaray.shop"

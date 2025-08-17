import os
import argparse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Frame, Table, TableStyle, HRFlowable
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus.doctemplate import NextPageTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from markdown import markdown
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import datetime
import re

# Nuova classe per la gestione del PDF
class MyDocTemplate(SimpleDocTemplate):
    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        SimpleDocTemplate.__init__(self, filename, **kw)
        #template = PageTemplate('normal', [Frame(2.5*cm, 2.5*cm, 15*cm, 25*cm, id='F1')])
        #self.addPageTemplates(template)

    def afterFlowable(self, flowable):
        "Registers TOC entries."
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()
            style = flowable.style.name
            if style == 'Header1':
                self.notify('TOCEntry', (0, text, self.page))
            if style == 'Header2':
                self.notify('TOCEntry', (1, text, self.page))
            if style == 'Header3':
                self.notify('TOCEntry', (2, text, self.page))
            if style == 'Header4':
                self.notify('TOCEntry', (3, text, self.page))

def convert_markdown_to_pdf( lang = 'it' ):
    try:
        # File di output
        output_file = '../Path to senior developer-' +lang +'.pdf'
        print(f'Inizio la creazione di: {output_file}')

        # Registra i font personalizzati
        pdfmetrics.registerFont(TTFont('Quicksand'      , '../book/fonts/Quicksand-Regular.ttf'))
        pdfmetrics.registerFont(TTFont('Quicksand-Bold' , '../book/fonts/Quicksand-Bold.ttf'))
        pdfmetrics.registerFont(TTFont('Roboto'         , '../book/fonts/Roboto-Regular.ttf'))
        pdfmetrics.registerFont(TTFont('Roboto-Bold'    , '../book/fonts/Roboto-Bold.ttf'))
        pdfmetrics.registerFont(TTFont('Roboto-Italic'  , '../book/fonts/Roboto-Italic.ttf'))
        pdfmetrics.registerFont(TTFont('SourceCodePro'  , '../book/fonts/SourceCodePro-Regular.ttf'))
        print(pdfmetrics.getRegisteredFontNames())

        # Stili personalizzati per i paragrafi
        custom_styles = {
            'header1'   : ParagraphStyle(
                name='Header1',
                fontName='Roboto-Bold',
                fontSize=16,
                spaceAfter=16,
                leading=24,
                alignment=TA_CENTER        # Allineamento centrato
            ),
            'header2'   : ParagraphStyle(name='Header2'     , fontName='Roboto-Bold'    , fontSize=14,                  spaceAfter=8    , leading=16                    ),
            'header3'   : ParagraphStyle(name='Header3'     , fontName='Roboto-Bold'    , fontSize=12,                  spaceAfter=8    , leading=14                    ),
            'header4'   : ParagraphStyle(name='Header4'     , fontName='Roboto-Bold'    , fontSize=12,                  spaceAfter=8    , leading=12                    ),
            'paragraph': ParagraphStyle(
                name='Paragraph',
                fontName='Quicksand',  # Font normale
                fontSize=12,
                spaceBefore=10,
                spaceAfter=10,
                leading=18,
                alignment=TA_JUSTIFY,
                # Aggiungi questa linea per supportare il grassetto
                allowWidows=1,  # Evita che una riga venga lasciata sola in una pagina
                allowOrphans=1,  # Evita che una riga venga lasciata sola in una pagina
            ),
            'link': ParagraphStyle(
                name='Link',
                fontName='Helvetica',
                fontSize=12,
                textColor=colors.blue,
                underline=True,
            ),
            'toc_entry' : ParagraphStyle(name='TOCEntry'    , fontName='Roboto'         , fontSize=14, spaceBefore=6,   spaceAfter=6    , leading=14                    ),
            'code'      : ParagraphStyle(
                name='Code'        ,
                fontName='SourceCodePro'  ,
                fontSize=12,
                spaceBefore=10,
                spaceAfter=10   ,
                leading=14    ,
                # leftIndent=12,
                textColor=colors.black,
                backColor=colors.Color(0.93, 0.93, 0.93),  # Grigio estremamente tenue
                borderColor=colors.Color(0.8, 0.8, 0.8),   # Bordo quasi invisibile
                borderWidth=0.3,
                borderPadding=5,
                borderRadius=2,  # Angoli arrotondati )
            ),
            'caption': ParagraphStyle(
                name='Caption',
                fontName='Quicksand-Bold',  # Usa il font Quicksand-Bold
                fontSize=12,                # Dimensione del font
                textColor=colors.black,     # Colore del testo
                alignment=TA_CENTER,        # Allineamento centrato
                spaceBefore=5,              # Spazio prima della didascalia
                spaceAfter=10,              # Spazio dopo la didascalia
            )
        }

        # Stile con sfondo e bordo
        boxed_style = ParagraphStyle(
            'BoxedStyle',
            fontName='Helvetica',
            fontSize=10,
            textColor=colors.black,
            backColor=colors.lightgrey,  # Sfondo grigio chiaro
            borderColor=colors.darkgrey,  # Colore bordo
            borderWidth=1,  # Spessore bordo
            borderPadding=5,  # Padding interno
            borderRadius=3,  # Angoli arrotondati
        )


        # Lista dei capitoli con i rispettivi file markdown
        capitoli = [
            ('paragrafi/00-prefazione-' +lang +'.md', ''),
            ('paragrafi/00-ringraziamenti-' +lang +'.md', ''),
            ('paragrafi/00-introduzione-' +lang +'.md', ''),

            # Fondamenta della Professionalità
#            ('paragrafi/01-fondamenta-della-professionalità-' +lang +'.md', ''),
            ('capitolo00/14-DiventareProgrammatoriOggi-articolo-' +lang +'.md', 'capitolo00/14-DiventareProgrammatoriOggi-articolo-1-leonardo-ai.png'),
            ('capitolo01/01-ProgrammatoriA40Anni-articolo-' +lang +'.md', 'capitolo01/01-ProgrammatoriA40Anni-articolo-1-leonardo-ia.jpg'),
            ('capitolo02/02-FinireIPropriTask-articolo-' +lang +'.md', 'capitolo02/02-FinireIPropriTask-articolo-1-leonardo-ai.jpg'),
            ('capitolo03/12-AmmettereDiNonSapere-articolo-' +lang +'.md', 'capitolo03/12-AmmettereDiNonSapere-articolo-3-leonardo-ai.jpg'),
#            ('capitolo04/57-Comunicazione Efficace in Team Tecnici.md', 'capitolo04/.jpg'),

            # Eccellenza Tecnica
            ('paragrafi/02-eccellenzatecnica-' +lang +'.md', ''),
            ('capitolo05/04-CondizioneNelCodice-articolo-' +lang +'.md', 'capitolo05/04-CondizioneNelCodice-articolo-3-leonardo-ai.jpg'),
            ('capitolo06/06-EsplorareNuoviFramework-articolo-' +lang +'.md', 'capitolo06/06-EsplorareNuoviFramework-articolo-4-leonardo-ai.jpg'),
            ('capitolo07/03-IlMitodelFullStackDeveloper-articolo-' +lang +'.md', 'capitolo07/03-DALL·E 2024-04-15 15.23.18 - A wide aspect image of a mythical version of a fullstack developer as Medusa. This scene blends ancient and modern elements_ Medusa, with a crown of v.webp'),
            ('capitolo08/11-CodeReview-articolo-' +lang +'.md', 'capitolo08/11-CodeReview-articolo-1-leonardo-ai.jpg'),

            # Dimensione Professionale
#            ('' +lang +'/03-dimensione professionale.md', ''),
            ('capitolo09/05-CelodurismoDeiProgrammatori-articolo-' +lang +'.md', 'capitolo09/05-CelodurismoDeiProgrammatori-articolo-1-leonardo-ai.jpg'),
            ('capitolo10/07-ProgrammatoriMercenari-articolo-' +lang +'.md', 'capitolo10/07-ProgrammatoriMercenari-articolo-2-leonardo-ai.jpg'),
            ('capitolo11/09-LaRALMotivaAlCambiamento-articolo-' +lang +'.md', 'capitolo11/09-LaRALMotivaAlCambiamento-articolo-2-leonardo-ai.jpg'),
            ('capitolo12/10-ChiPerdeUnProgrammatorePerdeUnTesoro-articolo-' +lang +'.md', 'capitolo12/10-ChiPerdeUnProgrammatorePerdeUnTesoro-articolo-2-dall-e.png'),

            # Dimensioni Personali e Sistemiche
#            ('' +lang +'/04-dimensioni personali e sistemiche.md', ''),
            ('capitolo13/13-ProgrammatoreAnelloDebole-' +lang +'.md', 'capitolo13/13-ProgrammatoreAnelloDebole-2-chatgpt.png'),
#            ('capitolo13/12-Gestione-del-Burnout-e-Salute-Mentale.md', 'capitolo13/.jpg'),
#            ('capitolo14/58-Etica e Responsabilità nella Programmazione.md', 'capitolo14/.jpg'),
            ('capitolo15/15-IlCimiteroDeiGeni-articolo-' +lang +'.md', 'capitolo15/15-IlCimiteroDeiGeni-articolo-1-leonardo-ai.jpg'),

            ('paragrafi/00-biografia-' +lang +'.md', '')
        ]

        h1 = ParagraphStyle(name = 'h1', fontSize = 14, leading = 16)
        h2 = ParagraphStyle(name = 'h2', fontSize = 12, leading = 14, leftIndent = 10)
        h3 = ParagraphStyle(name = 'h3', fontSize = 12, leading = 14, leftIndent = 10)
        h4 = ParagraphStyle(name = 'h4', fontSize = 10, leading = 14, leftIndent = 18)

        # Creazione del PDF
        doc = MyDocTemplate(output_file,
                            pagesize=letter,
                            bottomMargin=100) # Lascia spazio per il footer

        page_width, page_height = letter
        frame_no_margins = Frame(0, 0, page_width, page_height, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        frame_with_margins = Frame(inch, inch, page_width - 2*inch, page_height - 2*inch, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

        first_page_template = PageTemplate(id="FirstPage", frames=[frame_no_margins])
        following_pages_template = PageTemplate(id="FollowingPages", frames=[frame_with_margins])
        doc.addPageTemplates([first_page_template, following_pages_template])

        elements = []

        # Crea l'oggetto TOC
        toc = TableOfContents()
        toc.levelStyles = [h1, h2, h3, h4]

        # Copertina
        cover_image = Image(os.path.join('cover/Path to senior developer - alternative 3.png'), width=9*inch, height=11*inch)
        elements.append(cover_image)
        add_page(elements)

        # Elaborazione capitoli
        for chapter_info in capitoli:
            # Gestisci la possibilità di avere 2 o 3 elementi nella tupla
            if len(chapter_info) == 2:
                filename, image_path = chapter_info
            else:
                filename= chapter_info
                image_path = None

            # Leggi il contenuto del file markdown
            print(f'Leggo MD {filename}')
            with open(filename, 'r', encoding='utf-8') as f:
                markdown_content = f.read()

                # Estrai la prima riga e il resto del contenuto
                lines = markdown_content.splitlines()  # Divide il contenuto in righe

                # La prima riga è il titolo
                title = lines[0].strip()  # Usa strip() per rimuovere spazi bianchi e newline
                title = title.replace('#', '').strip()

                # Il resto del contenuto (dalla seconda riga in poi)
                markdown_content = "\n".join(lines[1:]).strip()  # Unisci le righe e trimmale

                # Se image_path è None, usa l'immagine di default
                if image_path:
                    process_markdown_title(elements, custom_styles, title, image_path)
                else:
                    markdown_content = f"# {title}\n\n{markdown_content}"

                # Salva la directory corrente
                original_dir = os.getcwd()

                # Ottieni la directory del file Markdown
                file_dir = os.path.dirname(filename)

                # Cambia directory alla cartella del file Markdown
                os.chdir(file_dir)

                chapter_elements = process_markdown_content(markdown_content, custom_styles)

                # Torna alla directory originale
                os.chdir(original_dir)

                elements.extend(chapter_elements)

                add_page(elements)

        # Inserisci la TOC prima della biografia
        elements.append(Paragraph('Indice', custom_styles['header1']))
        elements.append(toc)
        add_page(elements)

        # Dati aziendali personalizzati
        now = datetime.now()
        custom_data = {
            'oggi': now.strftime("%d/%m/%Y %H:%M")
        }

        # Genera PDF
        doc.multiBuild(elements,
            onLaterPages=lambda canvas, doc: (
                add_footer(canvas, doc, custom_data)
            ))

        # Stampa a video il percorso del file creato
        print(f'PDF creato: {output_file}')

    except Exception as e:
        print(f"Errore durante la generazione del PDF: {e}", exc_info=True)
        exit(1)  # Termina lo script con un codice di errore

# Resto del codice rimane invariato
def main():
    convert_markdown_to_pdf( 'it' )
    convert_markdown_to_pdf( 'en' )
    convert_markdown_to_pdf( 'es' )

def process_markdown_title(elements, custom_styles, title, image_path):
    # Aggiungi l'intestazione del capitolo
    if title:
        elements.append(Paragraph(title, custom_styles['header1']))

        # Aggiungi l'immagine se presente
        if image_path and os.path.exists(image_path):
            try:
                print(f'Leggo immagine {image_path}')
                img = Image(image_path, width=400*1.2, height=300*1.2)  # Regola dimensioni secondo necessità
                img.hAlign = 'CENTER'
                elements.append(img)
            except Exception as e:
                print(f"Errore nel caricamento dell'immagine {image_path}: {e}")
        else:
            raise Exception(f"Immagine non trovata: {image_path}")

        add_page(elements)

def apply_bold(text):
    # Cerca il testo tra ** e lo sostituisce con il formato grassetto
    bold_pattern = re.compile(r'\*\*(.*?)\*\*')
    return bold_pattern.sub(lambda match: f'<font name="Quicksand-Bold">{match.group(1)}</font>', text)

def apply_italic(text):
    """
    Trasforma il testo in corsivo da Markdown a ReportLab.
    Riconosce il testo tra * o _ e lo sostituisce con <i>.
    """
    # Cerca il testo tra * o _ e lo sostituisce con <i>
    italic_pattern = re.compile(r'(\*)(.*?)\1')
    return italic_pattern.sub(lambda match: f'<font name="Roboto-Italic">{match.group(2)}</font>', text)

def process_images(line, custom_styles):
    """
    Gestisce le immagini Markdown, aggiunge un bordo, centra la didascalia e aggiunge uno sfondo tenue.
    """
    # Cerca il pattern ![didascalia](path_immagine)
    image_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
    match = image_pattern.search(line)

    if match:
        caption = match.group(1)  # Didascalia
        image_path = os.path.join(os.getcwd(), match.group(2))  # Percorso dell'immagine

        # Verifica se il file esiste
        if not os.path.exists(image_path):
            raise Exception(f"Immagine non trovata: {image_path}")

        try:
            # Aggiungi l'immagine
            img = Image(image_path, width=400, height=300)  # Regola le dimensioni secondo necessità

            # Crea una tabella per il bordo, la didascalia e lo sfondo
            table_data = [
                [img],  # Immagine
                [Paragraph(caption, custom_styles['caption'])]  # Didascalia con stile personalizzato
            ]

            # Crea la tabella
            table = Table(table_data, colWidths=400)  # Larghezza della tabella uguale a quella dell'immagine

            # Aggiungi uno stile alla tabella per il bordo, il centramento e lo sfondo
            table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centra tutto il contenuto
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Allinea verticalmente al centro
                ('BOX', (0, 0), (-1, -1), 1, colors.black),  # Aggiungi un bordo nero
                ('BACKGROUND', (0, 0), (-1, -1), colors.Color(0.95, 0.95, 0.95)),  # Sfondo grigio chiaro
                ('PADDING', (0, 0), (-1, -1), 10),  # Aggiungi un po' di padding
            ]))

            return [table]  # Restituisci la tabella con l'immagine e la didascalia
        except Exception as e:
            raise Exception(f"Errore nel caricamento dell'immagine {image_path}: {e}")

    # Se non c'è un'immagine, restituisci None
    return None

def process_links(line, custom_styles):
    # Cerca il pattern [testo](URL)
    link_pattern = re.compile(r'\[(.*?)\]\((.*?)\)')
    match = link_pattern.search(line)

    if match:
        link_text = match.group(1)  # Testo del link
        link_url = match.group(2)   # URL del link
        link_html = f'<a href="{link_url}" color="blue">{link_text}</a>'
        link_paragraph = Paragraph(link_html, custom_styles['link'])
        return link_paragraph
    return None

def process_lists(line, custom_styles):
    # Gestisce le liste non ordinate
    if line.strip().startswith("- "):
        return Paragraph(f"• {line[2:]}", custom_styles['paragraph'])
    # Gestisce le liste ordinate
    elif re.match(r'^\d+\. ', line.strip()):
        return Paragraph(line, custom_styles['paragraph'])
    return None

def process_markdown_content(content, custom_styles):
    blocks = []
    in_code_block = False
    code_lines = []

    for line in content.splitlines():
        if line.strip().startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_lines = []
            else:
                in_code_block = False
                code_text = "<br/>".join(code_lines)
                blocks.append(Paragraph(code_text, custom_styles['code']))
                code_lines = []
        elif in_code_block:
            code_lines.append(line)
        else:
            # Applica il grassetto al testo tra **
            line = apply_bold(line)

            # Applica il corsivo al testo tra *
            line = apply_italic(line)

            # Gestisci le immagini
            image_elements = process_images(line, custom_styles)
            if image_elements:
                blocks.extend(image_elements)
                continue  # Passa alla prossima riga dopo aver gestito l'immagine

            # Gestisci i link
            link_paragraph = process_links(line, custom_styles)
            if link_paragraph:
                blocks.append(link_paragraph)
                continue  # Passa alla prossima riga dopo aver gestito il link

            # Gestisci le liste
            list_paragraph = process_lists(line, custom_styles)
            if list_paragraph:
                blocks.append(list_paragraph)
                continue  # Passa alla prossima riga dopo aver gestito la lista

            # Riconosce le intestazioni
            if line.startswith("# "):
                blocks.append(Paragraph(line[2:], custom_styles['header1']))
            elif line.startswith("## "):
                # Aggiungi un PageBreak prima delle conclusioni
                if line.startswith("## Conclusioni"):
                    blocks.append(PageBreak())

                blocks.append(Paragraph(line[3:], custom_styles['header2']))
            elif line.startswith("### "):
                blocks.append(Paragraph(line[3:], custom_styles['header3']))
            elif line.startswith("#### "):
                blocks.append(Paragraph(line[4:], custom_styles['header4']))
            else:
                # Linea normale trattata come paragrafo
                blocks.append(Paragraph(line, custom_styles['paragraph']))

    if code_lines:
        code_text = "\n".join(code_lines)
        blocks.append(Paragraph(code_text, custom_styles['code']))

    return blocks

def add_footer(canvas, doc, custom_data):
    print(f'Fine pagina {doc.page}')

    # Aggiungi il testo "DRAFT" come sfondo
    add_draft_watermark(canvas, doc)

    canvas.saveState()

    # Disegna una riga orizzontale
    canvas.setStrokeColor(colors.grey)
    canvas.setLineWidth(0.5)  # Spessore della riga
    canvas.line(
        doc.leftMargin,  # Punto x iniziale
        doc.bottomMargin - 65,  # Punto y (leggermente sopra il testo del footer)
        doc.width + doc.leftMargin,  # Punto x finale (larghezza totale)
        doc.bottomMargin - 65  # Punto y finale (stesso y iniziale)
    )

    footer_styleR = ParagraphStyle(
        'footer',
        fontSize=12,
        textColor=colors.grey,
        alignment=TA_RIGHT,  # Allineamento a destra per il numero di pagina
        #borderColor=colors.darkgrey,  # Colore bordo
        #borderWidth=1,  # Spessore bordo
    )

    footer_styleC = ParagraphStyle(
        'footer',
        fontSize=12,
        textColor=colors.grey,
        alignment=TA_CENTER,  # Allineamento a destra per il numero di pagina
        #borderColor=colors.darkgrey,  # Colore bordo
        #borderWidth=3,  # Spessore bordo
    )

    footer_styleL = ParagraphStyle(
        'footer',
        fontSize=12,
        textColor=colors.grey,
        alignment=TA_LEFT,  # Allineamento a destra per il numero di pagina
        #borderColor=colors.darkgrey,  # Colore bordo
        #borderWidth=5,  # Spessore bordo
    )

    # Footer sinistro
    left_footer = Paragraph("Matteo Baccan", footer_styleL)
    w, h = left_footer.wrap(doc.width, doc.bottomMargin)
    left_footer.drawOn(canvas, doc.leftMargin, h)

    # Footer centrale
    center_footer = Paragraph( custom_data['oggi'], footer_styleC)
    w, h = center_footer.wrap(doc.width, doc.bottomMargin)
    center_footer.drawOn(canvas, doc.leftMargin, h)

    # Footer destro (numero pagina)
    right_footer = Paragraph(f"Pagina {doc.page}", footer_styleR)
    w, h = right_footer.wrap(doc.width, doc.bottomMargin)
    right_footer.drawOn(canvas, doc.leftMargin, h)

    canvas.restoreState()

def add_draft_watermark(canvas, doc):
    canvas.saveState()

    # Imposta il colore del testo in grigio chiaro (trasparente)
    canvas.setFillColor(colors.Color(0.9, 0.9, 0.9, alpha=0.3))  # Grigio chiaro con trasparenza

    # Imposta il font e la dimensione del testo
    canvas.setFont("Helvetica-Bold", 60)

    # Ruota il testo di 45 gradi
    canvas.rotate(45)

    # Posizioni multiple per il testo "DRAFT"
    positions = [
        (doc.width / 2 + 100, doc.height / 2 - 200),  # Posizione centrale
        (doc.width / 2 - 200, doc.height / 2 + 100),  # Spostato in alto a sinistra
        (doc.width / 2 + 400, doc.height / 2 - 500),  # Spostato in basso a destra
        (doc.width / 2 - 500, doc.height / 2 + 400),  # Spostato in alto a destra
        (doc.width / 2 + 300, doc.height / 2 + 300),  # Altra posizione
    ]

    # Disegna il testo "DRAFT" in tutte le posizioni
    for x, y in positions:
        canvas.drawCentredString(x, y, "DRAFT DRAFT DRAFT")

    canvas.restoreState()

def add_page(elements):
    elements.append(PageBreak())

if __name__ == "__main__":
    main()

"""Generate professional CV PDFs (PT and EN) for Alessandro Canon."""

from pathlib import Path
from fpdf import FPDF

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "wwwroot" / "img" / "canon-profile.jpg"
OUT = ROOT / "wwwroot" / "files"
FONT = Path("C:/Windows/Fonts/arial.ttf")
FONT_BOLD = Path("C:/Windows/Fonts/arialbd.ttf")

MARGIN = 18
CONTENT_W = 210 - (MARGIN * 2)
LINKEDIN = "linkedin.com/in/alessandro-oliveira-sebastiao-a9099a66"


class CV(FPDF):
    def __init__(self, lang="pt"):
        super().__init__()
        self.lang = lang
        self.set_margins(MARGIN, MARGIN, MARGIN)
        self.set_auto_page_break(auto=True, margin=MARGIN)
        self.add_font("Arial", "", str(FONT))
        self.add_font("Arial", "B", str(FONT_BOLD))

    def _t(self, pt, en):
        return pt if self.lang == "pt" else en

    def _contact_line(self, text_x, width, text, line_h=4.8):
        self.set_x(text_x)
        self.set_font("Arial", "", 8.5)
        self.set_text_color(71, 85, 105)
        self.multi_cell(width, line_h, text)

    def header_block(self):
        y_start = MARGIN
        text_x = MARGIN + 38
        text_w = CONTENT_W - 38

        if IMG.exists():
            self.image(str(IMG), x=MARGIN, y=y_start, w=32, h=32)

        self.set_xy(text_x, y_start)
        self.set_font("Arial", "B", 16)
        self.set_text_color(15, 23, 42)
        self.multi_cell(text_w, 7, "Alessandro de Oliveira Sebastião")

        self.set_x(text_x)
        self.set_font("Arial", "B", 10)
        self.set_text_color(37, 99, 235)
        title = self._t(
            "Analista de Tecnologia da Informação | Engenheiro da Computação",
            "IT Analyst | Computer Engineer",
        )
        self.multi_cell(text_w, 5, title)
        self.ln(1)

        location = self._t("Botucatu, SP, Brasil", "Botucatu, SP, Brazil")
        self._contact_line(text_x, text_w, location)
        self._contact_line(text_x, text_w, "(14) 99715-8964")
        self._contact_line(
            text_x,
            text_w,
            "developercanon@gmail.com  |  developercanon@outlook.com",
        )
        self._contact_line(
            text_x,
            text_w,
            f"{LINKEDIN}  |  github.com/CanonEngineer",
        )

        line_y = self.get_y() + 3
        self.set_draw_color(37, 99, 235)
        self.set_line_width(0.6)
        self.line(MARGIN, line_y, 210 - MARGIN, line_y)
        self.set_y(line_y + 6)

    def section_title(self, title):
        if self.get_y() > 265:
            self.add_page()
        self.ln(3)
        self.set_font("Arial", "B", 10)
        self.set_text_color(37, 99, 235)
        self.cell(CONTENT_W, 6, title.upper())
        self.ln(6)

    def body_text(self, text):
        self.set_font("Arial", "", 9)
        self.set_text_color(51, 65, 85)
        self.multi_cell(CONTENT_W, 4.5, text)
        self.ln(2)

    def experience_entry(self, period, role, company, bullets):
        if self.get_y() > 250:
            self.add_page()

        y = self.get_y()
        self.set_font("Arial", "B", 9.5)
        self.set_text_color(15, 23, 42)
        self.cell(CONTENT_W - 42, 5, role)
        self.set_font("Arial", "", 8.5)
        self.set_text_color(100, 116, 139)
        self.cell(42, 5, period, align="R")
        self.ln(5)

        self.set_font("Arial", "", 9)
        self.set_text_color(71, 85, 105)
        self.cell(CONTENT_W, 4.5, company)
        self.ln(5)

        self.set_font("Arial", "", 8.5)
        self.set_text_color(51, 65, 85)
        for bullet in bullets:
            self.set_x(MARGIN + 2)
            self.multi_cell(CONTENT_W - 2, 4.2, f"\u2022  {bullet}")
        self.ln(2)

    def education_entry(self, period, degree, institution):
        if self.get_y() > 265:
            self.add_page()

        self.set_font("Arial", "B", 9)
        self.set_text_color(15, 23, 42)
        self.cell(CONTENT_W - 42, 5, degree)
        self.set_font("Arial", "", 8.5)
        self.set_text_color(100, 116, 139)
        self.cell(42, 5, period, align="R")
        self.ln(5)

        self.set_font("Arial", "", 8.5)
        self.set_text_color(71, 85, 105)
        self.cell(CONTENT_W, 4.5, institution)
        self.ln(5)

    def skill_block(self, label, items):
        self.set_font("Arial", "B", 8.5)
        self.set_text_color(15, 23, 42)
        self.cell(32, 5, f"{label}:")
        self.set_font("Arial", "", 8.5)
        self.set_text_color(51, 65, 85)
        self.multi_cell(CONTENT_W - 32, 4.5, items)
        self.ln(1)

    def build_pt(self):
        self.add_page()
        self.header_block()

        self.section_title("Resumo Profissional")
        self.body_text(
            "Profissional de TI com experiência em infraestrutura, redes, desenvolvimento de "
            "software e segurança da informação. Atuação em ambientes corporativos com foco em "
            "automação, modernização tecnológica e melhoria contínua. Formação em Engenharia da "
            "Computação com certificações em redes, segurança e DevOps."
        )

        self.section_title("Experiência Profissional")
        self.experience_entry(
            "Abr/2026 - Atual",
            "Analista de Tecnologia da Informação",
            "Hospital das Clínicas da Faculdade de Medicina de Botucatu (HCFMB)",
            [
                "Administração de infraestrutura de TI e redes corporativas.",
                "Suporte a sistemas institucionais e segurança da informação.",
                "Automação de processos e projetos de transformação digital.",
            ],
        )
        self.experience_entry(
            "Fev/2024 - Ago/2024",
            "Estágio em Engenharia da Computação",
            "Fixomolde Metalúrgica Tecnologia em Setup Ltda",
            [
                "Modernização da infraestrutura tecnológica da organização.",
                "Aplicação de metodologias ágeis (Scrum) em projetos de TI.",
                "Soluções para produtividade e segurança da informação.",
            ],
        )
        self.experience_entry(
            "Jul/2009 - Dez/2009",
            "Estágio em Análise e Desenvolvimento de Sistemas",
            "Faculdade de Tecnologia de Botucatu (FATEC)",
            [
                "Desenvolvimento backend com Python, Django e PostgreSQL.",
                "Manutenção de sistemas e arquitetura de software.",
            ],
        )

        self.section_title("Formação Acadêmica")
        self.education_entry("2020 - 2024", "Engenharia da Computação", "UNIVESP")
        self.education_entry("2011 - 2012", "Pós-Graduação em Gestão de Negócios", "FATEC Botucatu")
        self.education_entry(
            "2006 - 2009",
            "Tecnólogo em Análise e Desenvolvimento de Sistemas",
            "FATEC Botucatu",
        )

        self.section_title("Competências Técnicas")
        self.skill_block("Linguagens", "Python, JavaScript, HTML5, CSS3, SQL")
        self.skill_block("Frameworks", "Django, Node.js, Bootstrap, jQuery")
        self.skill_block("Infraestrutura", "Linux, Docker, Apache, Nginx, Git, DevOps, Redes")
        self.skill_block("Bancos de Dados", "PostgreSQL, MySQL, SQLite")

        self.section_title("Certificações")
        self.body_text(
            "CCNA (1-3) | CyberOps Associate | CSFPC | DevOps Essentials (DEPC) | "
            "PCAP Python | JavaScript Essentials (JSE) | Cisco IT Essentials"
        )

        self.section_title("Idiomas")
        self.body_text("Português (nativo) | Inglês (intermediário)")

    def build_en(self):
        self.add_page()
        self.header_block()

        self.section_title("Professional Summary")
        self.body_text(
            "IT professional with experience in infrastructure, networking, software development, "
            "and information security. Proven track record in corporate environments focused on "
            "automation, technology modernization, and continuous improvement. Computer Engineering "
            "degree with certifications in networking, cybersecurity, and DevOps."
        )

        self.section_title("Professional Experience")
        self.experience_entry(
            "Apr/2026 - Present",
            "IT Analyst",
            "Hospital das Clinicas da Faculdade de Medicina de Botucatu (HCFMB)",
            [
                "Managed IT infrastructure and corporate networks.",
                "Supported institutional systems and information security.",
                "Led process automation and digital transformation projects.",
            ],
        )
        self.experience_entry(
            "Feb/2024 - Aug/2024",
            "Computer Engineering Intern",
            "Fixomolde Metalurgica Tecnologia em Setup Ltda",
            [
                "Contributed to technology infrastructure modernization initiatives.",
                "Applied agile methodologies (Scrum) in IT projects.",
                "Delivered solutions for productivity and information security.",
            ],
        )
        self.experience_entry(
            "Jul/2009 - Dec/2009",
            "Systems Analysis & Development Intern",
            "Faculdade de Tecnologia de Botucatu (FATEC)",
            [
                "Backend development with Python, Django, and PostgreSQL.",
                "System maintenance and software architecture support.",
            ],
        )

        self.section_title("Education")
        self.education_entry("2020 - 2024", "B.S. in Computer Engineering", "UNIVESP")
        self.education_entry("2011 - 2012", "MBA in Business Management", "FATEC Botucatu")
        self.education_entry(
            "2006 - 2009",
            "A.S. in Systems Analysis & Development",
            "FATEC Botucatu",
        )

        self.section_title("Technical Skills")
        self.skill_block("Languages", "Python, JavaScript, HTML5, CSS3, SQL")
        self.skill_block("Frameworks", "Django, Node.js, Bootstrap, jQuery")
        self.skill_block("Infrastructure", "Linux, Docker, Apache, Nginx, Git, DevOps, Networking")
        self.skill_block("Databases", "PostgreSQL, MySQL, SQLite")

        self.section_title("Certifications")
        self.body_text(
            "CCNA (1-3) | CyberOps Associate | CSFPC | DevOps Essentials (DEPC) | "
            "PCAP Python | JavaScript Essentials (JSE) | Cisco IT Essentials"
        )

        self.section_title("Languages")
        self.body_text("Portuguese (native) | English (intermediate)")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    cv_pt = CV("pt")
    cv_pt.build_pt()
    cv_pt.output(str(OUT / "Alessandro_Canon_CV_PT.pdf"))

    cv_en = CV("en")
    cv_en.build_en()
    cv_en.output(str(OUT / "Alessandro_Canon_CV_EN.pdf"))

    print("CVs generated successfully.")


if __name__ == "__main__":
    main()

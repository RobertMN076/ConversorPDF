# Conversor de Arquivos Local 📄🔄

Um aplicativo desktop minimalista e de alto contraste desenvolvido em Python para converter documentos e imagens para PDF localmente, sem depender de ferramentas online.

## 🚀 Funcionalidades

* **Conversão de TXT para PDF:** Processamento linha a linha com fonte monoespaçada (Courier) para garantir que alinhamentos e quebras manuais do bloco de notas sejam preservados.
* **Conversão de DOCX para PDF (Alta Fidelidade):** Utiliza o motor de renderização nativo do sistema para espelhar perfeitamente o layout, fontes e tabelas do documento original.
* **Conversão de Imagens (PNG, JPG, JPEG) para PDF:** Preserva a densidade de pixels original e realiza o tratamento automático de canais de transparência (RGBA para RGB) para compatibilidade com PDF.
* **Interface Gráfica UI/UX:** Design clean de alto contraste (Branco e Azul) focado em usabilidade, construído com CustomTkinter.
* **Stand-alone:** Suporte para empacotamento em um único executável (`.exe`) via PyInstaller, permitindo uso prático direto na área de trabalho.

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/):** Linguagem base.
* **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter):** Para a interface gráfica moderna e estilizada.
* **[fpdf2](https://pyfpdf.github.io/fpdf2/):** Para a geração de PDFs a partir de textos puros.
* **[Pillow (PIL)](https://python-pillow.org/):** Para manipulação e conversão de matrizes de imagens.
* **[docx2pdf](https://github.com/AlJohri/docx2pdf):** Para a comunicação com o motor do sistema operacional (requer MS Word instalado para conversão de DOCX).
* **[PyInstaller](https://pyinstaller.org/):** Para compilação do projeto em executável.

## ⚙️ Como rodar o projeto em ambiente de desenvolvimento

1. Clone este repositório:
   ```bash
   git clone https://github.com/RobertMN076/ConversorPDF.git
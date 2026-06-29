import customtkinter as ctk
from tkinter import filedialog, messagebox
from fpdf import FPDF
from PIL import Image
import os

try:
    from docx2pdf import convert as converter_docx
except ImportError:
    converter_docx = None

# Força o modo claro para manter a paleta branca
ctk.set_appearance_mode("Light")  

class ConversorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configurações da janela principal com fundo branco
        self.title("Conversor de Arquivos")
        self.geometry("450x400")
        self.resizable(False, False) 
        self.configure(fg_color="#FFFFFF") # Fundo totalmente branco
        
        self.arquivo_selecionado = None
        self.tipo_arquivo = None 

        # Paleta de Cores
        COR_AZUL_PRINCIPAL = "#0056D2"
        COR_AZUL_HOVER = "#00419E"
        COR_TEXTO_ESCURO = "#0A192F"
        COR_TEXTO_SECUNDARIO = "#4A5568"

        # Título com azul escuro para alto contraste
        self.label_titulo = ctk.CTkLabel(
            self, 
            text="Conversor Local", 
            font=("Arial", 24, "bold"),
            text_color=COR_TEXTO_ESCURO
        )
        self.label_titulo.pack(pady=(30, 20))

        # Container para agrupar os botões de seleção
        self.frame_botoes = ctk.CTkFrame(self, fg_color="#F8FAFC", corner_radius=10)
        self.frame_botoes.pack(pady=10, padx=40, fill="x")

        # Botão 1: Documentos
        self.btn_doc = ctk.CTkButton(
            self.frame_botoes, 
            text="Selecionar TXT / DOCX", 
            command=lambda: self.selecionar_arquivo("doc"),
            fg_color="#FFFFFF",
            hover_color="#E2E8F0",
            text_color=COR_AZUL_PRINCIPAL,
            border_width=2,
            border_color=COR_AZUL_PRINCIPAL,
            font=("Arial", 13, "bold")
        )
        self.btn_doc.pack(pady=(15, 10), padx=20, fill="x")

        # Botão 2: Imagens
        self.btn_img = ctk.CTkButton(
            self.frame_botoes, 
            text="Selecionar Imagem PNG / JPG", 
            command=lambda: self.selecionar_arquivo("img"),
            fg_color="#FFFFFF",
            hover_color="#E2E8F0",
            text_color=COR_AZUL_PRINCIPAL,
            border_width=2,
            border_color=COR_AZUL_PRINCIPAL,
            font=("Arial", 13, "bold")
        )
        self.btn_img.pack(pady=(0, 15), padx=20, fill="x")

        # Label para mostrar o nome do arquivo escolhido
        self.label_arquivo = ctk.CTkLabel(
            self, 
            text="Nenhum arquivo selecionado", 
            text_color=COR_TEXTO_SECUNDARIO,
            font=("Arial", 12)
        )
        self.label_arquivo.pack(pady=5)

        # Botão Principal de Conversão (Azul Sólido)
        self.btn_converter = ctk.CTkButton(
            self, 
            text="Converter para PDF", 
            command=self.processar_conversao, 
            state="disabled", 
            height=45, 
            font=("Arial", 15, "bold"),
            fg_color=COR_AZUL_PRINCIPAL,
            hover_color=COR_AZUL_HOVER,
            text_color="#FFFFFF"
        )
        self.btn_converter.pack(pady=20, padx=40, fill="x")

    def selecionar_arquivo(self, tipo):
        if tipo == "doc":
            tipos = [("Documentos", "*.txt *.docx")]
        else:
            tipos = [("Imagens", "*.png *.jpg *.jpeg")]

        caminho = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=tipos)
        
        if caminho:
            self.arquivo_selecionado = caminho
            self.tipo_arquivo = tipo
            # Destaca o nome do arquivo selecionado em azul escuro
            self.label_arquivo.configure(text=os.path.basename(caminho), text_color="#0A192F", font=("Arial", 12, "bold"))
            self.btn_converter.configure(state="normal")

    def converter_imagem_pdf(self, entrada, saida):
        img = Image.open(entrada)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(saida, "PDF", resolution=100.0)

    def converter_txt_preciso(self, entrada, saida):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=10)
        with open(entrada, "r", encoding="utf-8", errors="ignore") as f:
            for linha in f:
                linha_limpa = linha.rstrip('\n')
                pdf.cell(0, 6, text=linha_limpa.encode('latin-1', 'replace').decode('latin-1'), ln=1)
        pdf.output(saida)

    def processar_conversao(self):
        if not self.arquivo_selecionado: return

        saida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
        if not saida: return

        try:
            ext = os.path.splitext(self.arquivo_selecionado.lower())[1]

            if ext in [".png", ".jpg", ".jpeg"]:
                self.converter_imagem_pdf(self.arquivo_selecionado, saida)
            elif ext == ".txt":
                self.converter_txt_preciso(self.arquivo_selecionado, saida)
            elif ext == ".docx":
                if converter_docx:
                    converter_docx(self.arquivo_selecionado, saida)
                else:
                    raise Exception("A biblioteca docx2pdf não está instalada.")

            messagebox.showinfo("Sucesso", "Conversão concluída com sucesso!")
            
            # Resetando a interface após o sucesso
            self.arquivo_selecionado = None
            self.label_arquivo.configure(text="Nenhum arquivo selecionado", text_color="#4A5568", font=("Arial", 12))
            self.btn_converter.configure(state="disabled")

        except Exception as e:
            messagebox.showerror("Erro", f"Falha na conversão:\n{e}")

if __name__ == "__main__":
    app = ConversorApp()
    app.mainloop()
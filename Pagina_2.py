from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import glob


class Pagina_2:
    def __init__(self, master):
        self.master = master
        self.list_mes = StringVar()
        self.list_empresa = StringVar()
        self.list_romaneio = ['Romaneio 450', 'dois', 'tres', 'quatro',
                              'cinco', 'seis', 'sets', 'oito', 'nove', 'Romaneio 460']
        self.test = []

        # Frames principais
        self.lf_top = LabelFrame(master)
        self.lf_top.place(relwidth=1, relheight=1/5)
        self.lf_mid = LabelFrame(master)
        self.lf_mid.place(relwidth=1, relheight=3/5, rely=1/5)
        self.lf_bot = LabelFrame(master)
        self.lf_bot.place(relwidth=1, relheight=1/5, rely=4/5)

    def top_frames(self):
        # Frames e Labels esquerdos / de texto
        lf_mes = LabelFrame(self.lf_top)
        lf_mes.place(relwidth=0.3, relheight=1/2, relx=0.1)

        lf_empresa = LabelFrame(self.lf_top)
        lf_empresa.place(relwidth=0.3, relheight=1/2, relx=0.1, rely=1/2)

        l_mes = Label(lf_mes, text='Mês', font=(
            'Segoe UI Semibold', 12), justify='center')
        l_mes.pack(fill='both', expand=1)

        lf_empresa = Label(lf_empresa, text='Empresa', font=(
            'Segoe UI Semibold', 12), justify='center')
        lf_empresa.pack(fill='both', expand=1)
        # Frames direitos / comboboxes
        lf_combo_mes = LabelFrame(self.lf_top, text='Mês do Fechamento')
        lf_combo_mes.place(relwidth=0.5, relheight=1/2, relx=0.45, rely=-0.1/2)

        lf_combo_empresa = LabelFrame(
            self.lf_top, text='Empresa de Fechamento')
        lf_combo_empresa.place(
            relwidth=0.5, relheight=1/2, relx=0.45, rely=0.9/2)

        combo_mes = ttk.Combobox(lf_combo_mes, textvariable=self.list_mes, font=(
            'Segoe UI Semibold', 12), justify='center')
        combo_mes.pack(fill='both', expand=1)
        combo_mes['value'] = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                              'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

        combo_empresa = ttk.Combobox(
            lf_combo_empresa, textvariable=self.list_empresa, font=(
                'Segoe UI Semibold', 12), justify='center')
        combo_empresa.pack(fill='both', expand=1)
        combo_empresa['value'] = ('Composê', 'Quebra-Cabeça')

    def mid_frames(self):
        # Iniciando os frames de posição
        lf_romaneio = LabelFrame(self.lf_mid, text='Romaneios')
        lf_romaneio.place(relwidth=3/10, relheight=1)

        lf_qntd = LabelFrame(self.lf_mid, text='Qntd')
        lf_qntd.place(relwidth=2/10, relheight=1, relx=3/10)

        lf_preço = LabelFrame(self.lf_mid, text='  R$')
        lf_preço.place(relwidth=1.5/10, relheight=1, relx=5/10)

        lf_entrada = LabelFrame(self.lf_mid, text='Entrada')
        lf_entrada.place(relwidth=2/10, relheight=1, relx=6.5/10)

        lf_saida = LabelFrame(self.lf_mid, text='saída')
        lf_saida.place(relwidth=1.5/10, relheight=1, relx=8.5/10)

        for i in range(len(self.list_romaneio)):
            romaneio = LabelFrame(lf_romaneio)
            romaneio.place(relwidth=1, relheight=1/10, rely=i/10)
            lb_romaneio = Label(romaneio, text=f'{self.list_romaneio[i]}')
            lb_romaneio.pack(fill='both', expand=1)

    def bot_frames(self):
        lb = LabelFrame(self.lf_bot, text='Obs:')
        lb.place(relwidth=0.5, relheight=1)
        st = scrolledtext.ScrolledText(lb, wrap=WORD)
        st.place(relwidth=1, relheight=1)

        Button(self.lf_bot, text='teste', command=repeat).pack(side='right')
        self.test.append(st)


def repeat():
    text = []
    st = pag_2.test[0].get('1.0', END)
    text.append(st)
    print(text)


if __name__ == '__main__':
    app = Tk()
    app.geometry('300x500')
    pag_2 = Pagina_2(app)
    pag_2.top_frames()
    pag_2.mid_frames()
    pag_2.bot_frames()
    repeat()
    app.mainloop()

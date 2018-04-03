import tkinter as tk
import pywallet_api

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    # UI Widgets Setup
    def create_widgets(self):
        self.main_label = tk.Label(self)
        self.main_label["text"] = "Click Go! to Create/Open"
        self.main_label["bg"] = "black"
        self.main_label["fg"] = "green"
        self.main_label["width"] = 50
        self.main_label["height"] = 20
        self.main_label["wraplength"] = 200
        self.main_label.pack(side="top")

        self.show_wallet_btn = tk.Button(self)
        self.show_wallet_btn["text"] = "Go!"
        self.show_wallet_btn["command"] = self.access_wallet
        self.show_wallet_btn.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.quit)
        self.quit.pack(side="bottom")

    #  Create New or Open Existing Wallet
    def access_wallet(self):
        # hide button
        self.show_wallet_btn.pack_forget()

        self.wallet_manager = pywallet_api.WalletManagerFactory.getWalletManager()
        has_wallet = self.wallet_manager.walletExists('wallet/mywallet');
        if has_wallet != True:
            self.w = self.wallet_manager.createWallet('wallet/mywallet', '', 'English', 1)
        else :
            self.w = self.wallet_manager.openWallet('wallet/mywallet', '', 1);

        self.main_label["text"] = '\n Main address : ' + self.w.mainAddress() + '\n\n seed : ' + self.w.seed()

root = tk.Tk()

# launch to foreground
root.lift()
root.attributes('-topmost',True)

app = Application(master=root)
app.mainloop()

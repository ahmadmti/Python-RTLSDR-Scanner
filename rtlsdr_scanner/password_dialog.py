import wx
import sys
import os

PASS_CANCEL = wx.NewId()
PASS_OK = wx.NewId()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2",os.path.abspath("."))

    return os.path.join(base_path, relative_path)
class PasswordDialog(wx.Dialog):
    def __init__(self, parent, title, caption):
        style = wx.DEFAULT_DIALOG_STYLE
        super(PasswordDialog, self).__init__(parent, -1, title, style=style)
        text = wx.StaticText(self, -1, caption)
        input = wx.TextCtrl(self, -1, style=wx.PASSWORD)
        button_cancel = wx.Button(self, PASS_OK, label='Ok')
        button_cancel.Bind(wx.EVT_BUTTON, self.on_ok)

        button_ok = wx.Button(self, PASS_CANCEL, label='Cancel')
        button_ok.Bind(wx.EVT_BUTTON, self.on_cancel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        row_sizer=wx.BoxSizer(wx.HORIZONTAL)
        row_sizer.Add(button_ok,0,wx.EXPAND|wx.ALL, 5)
        row_sizer.Add(button_cancel, 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(text, 0, wx.ALL, 5)
        sizer.Add(input, 0, wx.EXPAND, 1)
        sizer.Add(row_sizer,0,wx.EXPAND,5)
        self.SetSizerAndFit(sizer)
        self.input = input
    def SetValue(self, value):
        self.input.SetValue(value)

    def on_ok(self,event):
        with open(resource_path("res/pass.txt")) as file:
            password = file.read().strip()
            if self.input.GetValue() == password:
                self.EndModal(PASS_OK)
            else:
                self.input.SetBackgroundColour ( "Pink" )

    def on_cancel(self,event):
        self.EndModal(event.EventObject.Id)


class NewPasswordDialog(wx.Dialog):
    def __init__(self, parent):
        style = wx.DEFAULT_DIALOG_STYLE
        super(NewPasswordDialog, self).__init__(parent, -1, "Change Password", style=style)
        password_label = wx.StaticText(self, -1, "New Password")
        password = wx.TextCtrl(self, -1, style=wx.PASSWORD)
        button_cancel = wx.Button(self, PASS_CANCEL, label='Cancel')
        button_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)

        button_ok = wx.Button(self,PASS_OK , label='Ok')
        button_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        sizer = wx.BoxSizer(wx.VERTICAL)
        row_sizer=wx.BoxSizer(wx.HORIZONTAL)
        row_sizer.Add(button_cancel, 0, wx.EXPAND|wx.ALL, 5)
        row_sizer.Add(button_ok, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(password_label, 0, wx.ALL, 5)
        sizer.Add(password, 0, wx.EXPAND, 1)
        sizer.Add(row_sizer,0,wx.EXPAND,5)
        self.SetSizerAndFit(sizer)
        self.password = password
    def SetValue(self, value):
        self.password.SetValue(value)

    def on_ok(self,event):
        if len(self.password.GetValue())>=8:
            with open(resource_path("res/pass.txt"),"w") as file:
                file.write(self.password.GetValue())
                self.EndModal(PASS_OK)
        else:
            self.password.SetBackgroundColour(wx.RED)

    def on_cancel(self,event):
        self.EndModal(event.EventObject.Id)

class MasterPasswordDialog(wx.Dialog):
    def __init__(self, parent):
        style = wx.DEFAULT_DIALOG_STYLE
        super(MasterPasswordDialog, self).__init__(parent, -1, "Enter Master Password", style=style)
        text = wx.StaticText(self, -1, "Master Password")
        input = wx.TextCtrl(self, -1, style=wx.PASSWORD)
        button_cancel = wx.Button(self, PASS_OK, label='Ok')
        button_cancel.Bind(wx.EVT_BUTTON, self.on_ok)

        button_ok = wx.Button(self, PASS_CANCEL, label='Cancel')
        button_ok.Bind(wx.EVT_BUTTON, self.on_cancel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        row_sizer=wx.BoxSizer(wx.HORIZONTAL)
        row_sizer.Add(button_ok,0,wx.EXPAND|wx.ALL, 5)
        row_sizer.Add(button_cancel, 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(text, 0, wx.ALL, 5)
        sizer.Add(input, 0, wx.EXPAND, 1)
        sizer.Add(row_sizer,0,wx.EXPAND,5)
        self.SetSizerAndFit(sizer)
        self.input = input
    def SetValue(self, value):
        self.input.SetValue(value)

    def on_ok(self,event):
        if self.input.GetValue() == "thecrackofdawn":
            self.EndModal(PASS_OK)
        else:
            self.input.SetBackgroundColour ( "Pink" )

    def on_cancel(self,event):
        self.EndModal(event.EventObject.Id)


# if __name__ == '__main__':
#     app = wx.PySimpleApp()
#     dialog = PasswordDialog(None, 'Please Provide Password', 'Password')
#     dialog.Center()
#     dialog.SetValue('Value')
#     if dialog.ShowModal() == wx.ID_OK:
#         pass
#     dialog.Destroy()
#     app.MainLoop()
'''
Created on 2018/08/11
refer to URL
https://torina.top/detail/43/
https://wxpython.org/Phoenix/docs/html/wx.MouseEvent.html?highlight=dclick#wx.MouseEvent.Aux1DClick
http://wxwindowsjp.osdn.jp/docs/html/wx/wx411.htm
http://maku77.github.io/python/wxpython/textctrl.html
http://wxwindowsjp.osdn.jp/docs/html/wx/wx381.htm
https://wxpython.org/Phoenix/docs/html/wx.KeyEvent.html
https://www.blog.pythonlibrary.org/2009/08/29/wxpython-catching-key-and-char-events/
@author: atomic
'''

import wx
##############################################
#            global variable
##############################################
rec_side = 50       #四角の辺の大きさ
bd_width = 500     #フレームの横幅
bd_height = 500    #フレームの縦幅
center_x = bd_width/2
center_y = bd_height/2
clr = "black"       #背景の色
tclr = 'green'       #テキストの色
prime_cnt = 50
dict = {
    "mind":None,
    "net":None,
    "IT":None,
    "swk":None,
    "tom":None
    }

ret_text = "None"

class mind():

    #コンストラクタ
    def __init__(self,panel,text):
        self.x = center_x
        #self.y = center_y
        self.panel = panel
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.click_panel)
        print(dict)
        dict_list = list(dict.keys())
        dict_len = len(dict_list)
        for i in range(dict_len):
            self.y =center_y+i*25
            text_obj = wx.StaticText(self.panel, wx.ID_ANY, dict_list[i],pos = (self.x,self.y))
            text_obj.SetForegroundColour(tclr)
            text_obj.Bind(wx.EVT_LEFT_DOWN, self.click)
            text_obj.Bind(wx.EVT_LEFT_DCLICK, self.double_click)
        #layout.Add(text_obj, proportion=0, flag=wx.TOP,  border=10)


    def click_panel(self,event):
        self.textbox.Destroy()
        #self.panel.Bind(wx.EVT_CHAR_HOOK, self.key_event)
        #self.panel.Bind(wx.EVT_KEY_DOWN, self.key_event)
        self.panel.Bind(wx.EVT_CHAR, self.key_event)

    def key_event(self,event):
        #self.keycode = event.GetUnicodeKey()
        self.keycode = event.GetKeyCode()
        #print(keycode)
        # It's a special key, deal with all the known ones:
        #self.keycode.Destroy()
        #self.keycode.GetSkipped()
        #event.GetSkipped()
        #self.text_input()
        print("press key")
        print(self.keycode)
        event.GetSkipped()
        if self.keycode == wx.WXK_TAB:
            # give help ...
            #event.Skip()
            #self.keycode.GetSkipped()
            #event.GetSkipped()
            print("tab")
            self.texttabbox = wx.TextCtrl(self.panel, -1, pos = (self.x,self.y+25),style=wx.TE_PROCESS_ENTER )
            #self.texttabbox.Bind(wx.EVT_TEXT_ENTER, self.OnText)
            input_text =self.texttabbox.GetValue()
            self.texttabbox.Destroy()
            print(input_text)
            #text_obj = wx.StaticText(self.panel, wx.ID_ANY, input_text, pos = (self.x,self.y+25))
            #text_obj.SetForegroundColour(tclr)
            #text_obj.Bind(wx.EVT_LEFT_DOWN, self.click)
            #text_obj.Bind(wx.EVT_LEFT_DCLICK, self.double_click)
            #self.text_input()
            #self.keycode.Destroy()
            #event.Skip()
             
    #def text_input(self):
    #    print("TAB")
    #    self.texttabbox = wx.TextCtrl(self.panel, -1, pos = (self.x,self.y+25),style=wx.TE_PROCESS_ENTER )
    #    self.texttabbox.Bind(wx.EVT_TEXT_ENTER, self.OnText)

    def click(self, event):
        #self.textbox.Destroy()
        click = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        click_text = click.GetLabel()  # そのオブジェクトのラベルを取得
        #self.result_text.SetLabel(click_text)  # 結果表示欄にクリックされたテキストを貼り付け
        ret_text = click_text
        print(ret_text)

    def double_click(self, event):
        self.click = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        click_text = self.click.GetLabel()  # そのオブジェクトのラベルを取得
        ret_text = click_text
        print(ret_text)
        self.textbox = wx.TextCtrl(self.panel, -1, click_text, pos = self.click.GetPosition(),style=wx.TE_PROCESS_ENTER )
        #self.textbox.Bind(wx.EVT_TEXT, self.OnText)
        self.textbox.Bind(wx.EVT_TEXT_ENTER, self.OnText)
        #self.Fit()

    def OnText(self, event):
        #self.Fit()
        input_text =self.textbox.GetValue()
        self.textbox.Destroy()
        #self.textbox.Close(force=True)
        #self.textbox.Clear()
        print(input_text)
        self.click.SetLabel(input_text)

#class Main(wx.Frame):
class Main():
    #def __init__(self, parent, id, title):
    def __init__(self):
        """ レイアウトの作成 """
        #wx.Frame.__init__(self, parent, id, title)
        frame = wx.Frame(None,title="mindnet")#ウィンドウ作成クラス
        frame.SetClientSize(bd_width,bd_height)
        panel = wx.Panel(frame)
        panel.SetBackgroundColour(clr)#set color of background

        self.result_text = wx.StaticText(panel, wx.ID_ANY, "click text name ...")
        self.result_text.SetForegroundColour(tclr)
        self.result_text.Bind(wx.EVT_LEFT_DOWN, self.click)
        # 上に10pxあけてStaticTextを配置
        v_layout = wx.BoxSizer(wx.VERTICAL)

        # StaticTextを3つ作る
        mind(panel,"text1")
        #mind(panel,"text2")
        #v_layout.Add(self.result_text, proportion=0, flag=wx.TOP,  border=10)

        panel.SetSizer(v_layout)
        #self.Show(True)
        frame.Show(True)

    def click(self, event):
        click = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        click_text = click.GetLabel()  # そのオブジェクトのラベルを取得
        self.result_text.SetLabel(ret_text)  # 結果表示欄にクリックされたテキストを貼り付け
        #self.frame.Show(True)

def main():
    app = wx.App()
    Main()
    app.MainLoop()

if __name__ == "__main__":
    main()
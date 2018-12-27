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
TEXTBOX_CNT = 0
TEXTBOX_ENABLE = 1
TEXTBOX_DISABLE = 0

class mind():
    #コンストラクタ
    def __init__(self,panel,text):
        self.x = center_x
        self.y = center_y
        self.textobj_list = []
        self.textbox_list = []
        self.textbox_cnt = 0
        self.panel = panel
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.click_panel)
        print(dict)
        self.dict_list = list(dict.keys())
        dict_len = len(self.dict_list)
        for text_cnt in range(dict_len):
            self.y = center_y + text_cnt * 25
            self.textobj = wx.StaticText(self.panel, wx.ID_ANY, self.dict_list[text_cnt],pos = (self.x,self.y))
            self.textobj.SetForegroundColour(tclr)
            self.textobj.Bind(wx.EVT_LEFT_DOWN, self.click)
            self.textobj.Bind(wx.EVT_LEFT_DCLICK, self.double_click)
            self.textobj_list.append(self.textobj)
        print(" self.textbox_cnt = " + str(self.textbox_cnt))
        print(" len(self.textbox_list) = " + str(len(self.textbox_list)))

    def click_panel(self,event):
        print(len(self.textbox_list))
        if self.textbox_cnt > TEXTBOX_DISABLE :
            print(self.textbox_cnt)
            self.textbox_list[self.textbox_cnt-1].Destroy()
            del self.textbox_list[self.textbox_cnt-1]
            print("#textbox_delete")
            self.textbox_cnt -= 1
        #self.panel.Bind(wx.EVT_CHAR_HOOK, self.key_event)#MAC NG
        self.panel.Bind(wx.EVT_KEY_DOWN, self.key_event)#MAC OK
        #self.panel.Bind(wx.EVT_CHAR, self.key_event)
        print(" self.textbox_cnt = " + str(self.textbox_cnt))
        print(" len(self.textbox_list) = " + str(len(self.textbox_list)))

    def key_event(self,event):
        self.keycode = event.GetKeyCode()
        print("press key")
        print(self.keycode)
        #event.GetSkipped()
        if self.keycode == wx.WXK_TAB:
            print("tab")
            self.y += 25
            self.textbox = wx.TextCtrl(self.panel, -1, pos = (self.x,self.y),style=wx.TE_PROCESS_ENTER )
            self.textbox.Bind(wx.EVT_TEXT_ENTER, self.OnTabText)
            self.textbox_list.append(self.textbox)
            self.textbox_cnt += 1
        print(" self.textbox_cnt = " + str(self.textbox_cnt))
        print(" len(self.textbox_list) = " + str(len(self.textbox_list)))

    def OnTabText(self, event):
        self.box = event.GetEventObject()
        input_text = self.box.GetValue()
        self.box.Destroy()
        self.textbox_cnt -= 1
        print(input_text)
        #if int(dict.setdefault(input_text,None)) > len(self.dict_list)):
        textobj = wx.StaticText(self.panel, wx.ID_ANY, input_text,pos = (self.x,self.y))
        textobj.SetForegroundColour(tclr)
        textobj.Bind(wx.EVT_LEFT_DOWN, self.tabclick)
        textobj.Bind(wx.EVT_LEFT_DCLICK, self.tabdouble_click)
        print(dict)
        
    def tabclick(self, event):
        if self.textbox_cnt > TEXTBOX_DISABLE :
            print(self.textbox_cnt)
            self.textbox_list[self.textbox_cnt-1].Destroy()
            del self.textbox_list[self.textbox_cnt-1]
            print("#textbox_delete")
            self.textbox_cnt -= 1
        click = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        click_text = click.GetLabel()  # そのオブジェクトのラベルを取得
        ret_text = click_text
        print(ret_text)

    def tabdouble_click(self, event):
        self.click = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        click_text = self.click.GetLabel()  # そのオブジェクトのラベルを取得
        ret_text = click_text
        print(ret_text)
        self.textbox = wx.TextCtrl(self.panel, -1, click_text, pos = self.click.GetPosition(),style=wx.TE_PROCESS_ENTER )
        self.textbox.Bind(wx.EVT_TEXT_ENTER, self.OnText)
        self.textbox_list.append(self.textbox)
        self.textbox_cnt += 1
        print(" self.textbox_cnt = " + str(self.textbox_cnt))
        print(" len(self.textbox_list) = " + str(len(self.textbox_list)))
        
    def click(self, event):
        if self.textbox_cnt > TEXTBOX_DISABLE :
            print(self.textbox_cnt)
            self.textbox_list[self.textbox_cnt-1].Destroy()
            del self.textbox_list[self.textbox_cnt-1]
            print("#textbox_delete")
            self.textbox_cnt -= 1
        click = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        click_text = click.GetLabel()  # そのオブジェクトのラベルを取得
        ret_text = click_text
        print(ret_text)

    def double_click(self, event):
        self.click = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        click_text = self.click.GetLabel()  # そのオブジェクトのラベルを取得
        ret_text = click_text
        print(ret_text)
        self.textbox = wx.TextCtrl(self.panel, -1, click_text, pos = self.click.GetPosition(),style=wx.TE_PROCESS_ENTER )
        self.textbox.Bind(wx.EVT_TEXT_ENTER, self.OnText)
        self.textbox_list.append(self.textbox)
        self.textbox_cnt += 1
        print(" self.textbox_cnt = " + str(self.textbox_cnt))
        print(" len(self.textbox_list) = " + str(len(self.textbox_list)))

    def OnText(self, event):
        self.ontextobj = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        input_text =self.textbox.GetValue()
        if self.textbox_cnt > TEXTBOX_DISABLE:
            print(self.textbox_cnt)
            self.textbox_list[self.textbox_cnt-1].Destroy()
            del self.textbox_list[self.textbox_cnt-1]
            print("#textbox_delete")
            self.textbox_cnt -= 1
        print(input_text)
        self.click.SetLabel(input_text)

    def del_txtbox(self):
        print(" self.textbox_cnt = " + str(self.textbox_cnt))
        print(" len(self.textbox_list) = " + str(len(self.textbox_list)))

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
        #self.result_text.SetLabel(ret_text)  # 結果表示欄にクリックされたテキストを貼り付け
        #self.frame.Show(True)

def main():
    app = wx.App()
    Main()
    app.MainLoop()

if __name__ == "__main__":
    main()
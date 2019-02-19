# coding: UTF-8
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
text events
http://wxwindowsjp.osdn.jp/docs/html/wx/wx381.htm
https://maku77.github.io/python/wxpython/graphics.html
@author: atomic
'''
import math
import json
import wx
##############################################
#            global variable
##############################################
PI = math.pi
rec_side = 50       #四角の辺の大きさ
bd_width = 500     #フレームの横幅
bd_height = 500    #フレームの縦幅
center_x = bd_width/2
center_y = bd_height/2
clr = "black"       #背景の色
tclr = 'white'       #テキストの色
prime_cnt = 50
f = open('data.json', 'r', encoding='utf-8')
#f = open('data_w.json', 'w')
jsonData = json.load(f)
f.close
print (json.dumps(jsonData, sort_keys = True, indent = 4))
dict = jsonData
#"""
ret_text = "None"
TEXTBOX_CNT = 0
TEXTBOX_ENABLE = 1
TEXTBOX_DISABLE = 0
INCRS_PI = PI/11

class mind():
    #constractor
    th = -PI/4   #θ
    r = 100      #radius
    cur_x = center_x + r * math.cos(th)
    cur_y = center_y + r * math.sin(th)
    cur_len = 0
    tab_flag = False
    del_editbox = None#delete editbox
    callSkip = None
    dc = None
    child_flag = False

    #constractor
    def __init__(self,panel):
        self.textobj_list = []
        self.textbox_list = []
        self.textbox_cnt = 0
        self.x = mind.cur_x
        self.y = mind.cur_y
        self.dict_list = list(dict.keys())
        mind.panel = panel
        mind.cur_len = len(self.dict_list)
        for text_cnt in range(mind.cur_len):
            mind.cur_x =  center_x + mind.r * math.cos(mind.th)
            mind.cur_y =  center_y + mind.r * math.sin(mind.th)
            mind.th += INCRS_PI
            self.theta = mind.th
            self.textobj = wx.StaticText(mind.panel, wx.ID_ANY, self.dict_list[text_cnt],pos = (mind.cur_x,mind.cur_y))
            self.textobj.SetForegroundColour(tclr)
            self.textobj.Bind(wx.EVT_LEFT_UP, self.click)
            self.textobj.Bind(wx.EVT_LEFT_DCLICK, self.double_click)

            self.textobj_list.append(self.textobj)

    def click(self, event):
        #event.Skip()
        print("mind.click()")
        mind.child_flag = True
        if self.textbox_cnt > TEXTBOX_DISABLE :
            print(self.textbox_cnt)
            self.textbox_list[self.textbox_cnt-1].Destroy()
            del self.textbox_list[self.textbox_cnt-1]
            print("#textbox_delete")
            self.textbox_cnt -= 1
        click = event.GetEventObject()  #クリックされたのはどのオブジェクトか
        click.Bind(wx.EVT_CHAR_HOOK, self.key_tab)
        click_text = click.GetLabel()  #そのオブジェクトのラベルを取得
        ret_text = click_text
        print(ret_text)

    def key_tab(self,event):
        print("key_tab()")
        keycode = event.GetKeyCode()
        event.Skip()
        print("mind.key_tab()")
        print(keycode)
        #event.GetSkipped()
        if keycode == wx.WXK_TAB:
            print("tab")
            #self.y += 25
            self.textbox = wx.TextCtrl(mind.panel, -1, pos = (center_x,center_y),style = wx.TE_PROCESS_ENTER )
            #self.textbox.Bind(wx.EVT_TEXT_ENTER, self.OnTabText)
            #self.textbox_list.append(self.textbox)
            self.textbox_cnt += 1
        #print(" self.textbox_cnt = " + str(self.textbox_cnt))
        #print(" len(self.textbox_list) = " + str(len(self.textbox_list)))

    def double_click(self, event):
        print("double_click()")
        self.click = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        click_text = self.click.GetLabel()  # そのオブジェクトのラベルを取得
        ret_text = click_text
        print(ret_text)
        textbox = wx.TextCtrl(mind.panel, -1, click_text, pos = self.click.GetPosition(),style = wx.TE_PROCESS_ENTER )
        textbox.SelectAll()
        textbox.SetFocus()
        #print(textbox.GetSelection())
        textbox.Bind(wx.EVT_TEXT_ENTER, self.OnText)
        self.textbox_list.append(textbox)
        self.textbox_cnt += 1
        print(" self.textbox_cnt = " + str(self.textbox_cnt))
        print(" len(self.textbox_list) = " + str(len(self.textbox_list)))

    def OnText(self, event):
        print("OnText()")
        textbox = event.GetEventObject()
        #self.textbox.SelectAll()
        input_text = textbox.GetValue()
        #self.textbox.SetValue(input_text)
        if self.textbox_cnt > TEXTBOX_DISABLE:
            print(self.textbox_cnt)
            self.textbox_list[self.textbox_cnt-1].Destroy()
            del self.textbox_list[self.textbox_cnt-1]
            print("OnText() textbox_delete")
            self.textbox_cnt -= 1
        print(input_text)
        #self.click.SetLabel(input_text)

    def del_txtbox(self):
        print("entry_label")
        print(" self.textbox_cnt = " + str(self.textbox_cnt))
        print(" len(self.textbox_list) = " + str(len(self.textbox_list)))

    @classmethod
    def entry_label(cls):
        print("entry_label()")
        cls.th += INCRS_PI
        #cls.cur_y = center_y + cls.cur_len * 25
        cls.cur_x =  center_x + cls.r * math.cos(mind.th)
        cls.cur_y =  center_y + cls.r * math.sin(mind.th)
        cls.tab_flag = 0
        editbox = wx.TextCtrl(mind.panel, -1, pos = (cls.cur_x ,cls.cur_y),style = wx.TE_PROCESS_ENTER )
        editbox.SetFocus()
        cls.del_editbox = editbox
        cls.tab_flag = True#set tab pressed
        editbox.Bind(wx.EVT_TEXT_ENTER, cls.write_label )

    @classmethod
    def write_label(cls,event):
        print("write_label()")
        editbox = event.GetEventObject()
        input_text = editbox.GetValue()
        editbox.Destroy()
        write_flag = dict.setdefault(input_text,None)
        print(dict.setdefault(input_text,None))
        if write_flag == None:
            Static = wx.StaticText(cls.panel, -1, input_text, pos = (cls.cur_x,cls.cur_y))
            Static.SetForegroundColour(tclr)
            cls.tab_flag = False#set tab unpressed
            cls.cur_len += 1#inclease text objct
        else:
            print("dict is not available")
        print(dict)

    @classmethod
    def cls_leave(cls,event):
        print("cls_leave()")
        editbox = event.GetEventObject()
        editbox.Destroy()
        cls.tab_flag = False#set tab unpressed

    @classmethod
    def cls_delete(cls,event):
        print("cls_delete()")
        editbox = event.GetEventObject()
        editbox.Destroy()
        cls.tab_flag = False#set tab unpressed

#class Main(wx.Frame):
class Main():
    #def __init__(self, parent, id, title):
    panel = None
    def __init__(self):
        #wx.Frame.__init__(self, parent, id, title)
        frame = wx.Frame(None,title="mindnet")
        frame.SetClientSize(bd_width,bd_height)

        Main.panel = wx.Panel(frame)
        Main.panel.Bind(wx.EVT_LEFT_DOWN, self.click_ev)
        Main.panel.SetBackgroundColour(clr)
        mind(Main.panel)
        frame.Show(True)

    def click_ev(self,event):
        print("click_ev()")
        Main.panel.Bind(wx.EVT_CHAR_HOOK, self.key_event)#WIN OK
        #panel.Bind(wx.EVT_KEY_DOWN, self.key_event)#MAC OK
        if mind.tab_flag == True:
            print("delete editbox")
            mind.del_editbox.Destroy()
            mind.tab_flag  = False#set tab unpressed
        else:
            print("no editbox")

    def key_event(self,event):
        print("key_event()")
        keycode = event.GetKeyCode()
        # 後続のキーイベントをスキップする
        #mind.callSkip = True
        if mind.child_flag == False:
            if keycode == wx.WXK_TAB:
                print("press TAB")
                if mind.tab_flag == False:#tab dont pressed case
                    print("create editbox")
                    mind.entry_label()
                else:
                    print("cant create editbox")

            elif keycode == wx.WXK_ESCAPE:
                print("press ESC")
                if mind.tab_flag == True:
                    print("delete editbox")
                    mind.del_editbox.Destroy()
                    mind.tab_flag = False#set tab unpressed
                else:
                    print("no editbox")
            else:
                print("other key down")
                event.Skip()
        else:
            print("detect child flag")
            #event.Bind(wx.EVT_SET_FOCUS, self.onKeyKillFocus)
            event.Skip()

    def onKeyKillFocus(self, event):
        print ("key lost focus!")


def main():
    app = wx.App()
    Main()
    app.MainLoop()

if __name__ == "__main__":
    main()

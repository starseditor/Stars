# -*-encoding=utf-8-*-
import os
import Tkinter, tkFileDialog

class OperateTrack:
    def __init__(self):
        self.modelname = ""
        self.operateList = []
        self.trackLogDir = os.path.join(os.getcwd(),"operateTrackLog")  
        #os.getcwd()的作用是返回当前工作目录；后面的参数operateTrackLog用来拼接形成日志文件的存储路径
        if not os.path.exists(self.trackLogDir):
            os.path.exists(self.trackLogDir)
        #函数os.path.exists(path) 
        #路径存在则返回True,路径损坏返回False
        


    def addOperate(self, isadd, operatename, functionname):
        if isadd :
            self.operateList.append([operatename, functionname])
            # list.append(obj) obj表示添加到列表末尾的对象
            # append() 方法用于在列表末尾添加新的对象。

            print "Add operate "+ operatename
        else:
            pass
            #Python pass是空语句，是为了保持程序结构的完整性。
            #pass 不做任何事情，一般用做占位语句。

    def saveOperate(self):
        title = 'Save Operate Track As Model'
        initialdir = self.trackLogDir
        type = [('Operate Log','*.opr')]
        filename = tkFileDialog.asksaveasfilename(filetypes = type,title = title,initialdir=initialdir,defaultextension='.opr')
        if not filename:
            return
        self.filepath = filename
        fo = open(filename,"w")
        fo.write(str(len(self.operateList))+"\n")
        text =""
        for operate in self.operateList:
            text += operate[0]+','+operate[1]+'\n'
        fo.writelines(text)
        fo.close()
        print "Finish save operateLog: "+ self.filepath











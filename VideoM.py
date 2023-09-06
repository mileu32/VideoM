#-*- coding:utf-8 -*-
from tkinter import *
from tkinter.filedialog import askopenfilename
import os

file_url = "test"
pfile_url = ""

def file_selector():
	file_url = askopenfilename()
	commandFileEntry.delete(0, END)
	commandFileEntry.insert(0, file_url)

def videoM(fu, sh, sm, ss, eh, em, es):
	new_file_url = os.path.join(os.path.dirname(fu), "[C]" + os.path.basename(fu))
	commandMessage = 'ffmpeg.exe -i \"' + fu + '\" -ss ' + sh.zfill(2) + ":" + sm.zfill(2) + ":" + ss.zfill(2) + ' -to ' + eh.zfill(2) + ":" + em.zfill(2) + ":" + es.zfill(2) + ' -c:v copy -c:a copy ' + '\"' + new_file_url + '\"'
	print(commandMessage)
	if os.path.exists(new_file_url):
		messageLabel2['text'] = "저장할 디렉토리에 이미 파일이 있습니다. 해당 파일 삭제후 다시 시도해주세요."
		messageLabel2['background'] = 'red'
		return
	messageLabel2['background'] = 'deepskyblue'
	commandMessage = 'ffmpeg -i \"' + fu + '\" -ss ' + sh.zfill(2) + ":" + sm.zfill(2) + ":" + ss.zfill(2) + ' -to ' + eh.zfill(2) + ":" + em.zfill(2) + ":" + es.zfill(2) + ' -c:v copy -c:a copy ' + '\"' + new_file_url + '\"'
	messageLabel2['text'] = "동영상 변환이 완료되었습니다. 변환된 동영상 이름은 원본 동영상 이름 앞에 [C]가 추가됩니다."
	print(commandMessage)
	os.system(commandMessage)
	return

#gui

tk = Tk()

tk.title("VideoM")
tk.configure(background='royalblue')

width = 600
height = 300
display_width  = tk.winfo_screenwidth()
display_height = tk.winfo_screenheight()
screen_x = display_width / 2 - width / 2
screen_y = display_height / 2 - height / 2

tk.geometry("%dx%d+%d+%d" % (width, height, screen_x, screen_y))

messageFrame = Frame(tk)
messageFrame.configure(background = 'deepskyblue')
messageFrame.pack(padx = 20, pady = 20)
messageLabel = Label(messageFrame, text = "VideoM 2021", background = 'deepskyblue')
messageLabel.pack()

commandFrame = Frame(tk)
commandFrame.configure(background = 'deepskyblue')
commandFrame.pack(padx = 10, pady = 10)

commandFileFrame = Frame(commandFrame)
commandFileFrame.configure(background = 'deepskyblue')
commandFileFrame.pack(padx = 10, pady = 10)

commandFileButton = Button(commandFileFrame, text = "동영상 선택", command = lambda: file_selector(), background = 'deepskyblue')
commandFileButton.grid(row = 0, column = 0)
commandFileEntry = Entry(commandFileFrame, width = 30)
commandFileEntry.grid(row = 1, column = 0)

commandStartLabel = Label(commandFileFrame, text = "시작", background = 'deepskyblue')
commandStartLabel.grid(row = 0, column = 1)
commandStartLabelH = Label(commandFileFrame, text = "H", background = 'deepskyblue')
commandStartLabelH.grid(row = 0, column = 2)
commandStartEntryH = Entry(commandFileFrame, width = 4)
commandStartEntryH.grid(row = 0, column = 3)
commandStartLabelM = Label(commandFileFrame, text = "M", background = 'deepskyblue')
commandStartLabelM.grid(row = 0, column = 4)
commandStartEntryM = Entry(commandFileFrame, width = 4)
commandStartEntryM.grid(row = 0, column = 5)
commandStartLabelS = Label(commandFileFrame, text = "S", background = 'deepskyblue')
commandStartLabelS.grid(row = 0, column = 6)
commandStartEntryS = Entry(commandFileFrame, width = 4)
commandStartEntryS.grid(row = 0, column = 7)

commandEndLabel = Label(commandFileFrame, text = "종료", background = 'deepskyblue')
commandEndLabel.grid(row = 1, column = 1)
commandEndLabelH = Label(commandFileFrame, text = "H", background = 'deepskyblue')
commandEndLabelH.grid(row = 1, column = 2)
commandEndEntryH = Entry(commandFileFrame, width = 4)
commandEndEntryH.grid(row = 1, column = 3)
commandEndLabelM = Label(commandFileFrame, text = "M", background = 'deepskyblue')
commandEndLabelM.grid(row = 1, column = 4)
commandEndEntryM = Entry(commandFileFrame, width = 4)
commandEndEntryM.grid(row = 1, column = 5)
commandEndLabelS = Label(commandFileFrame, text = "S", background = 'deepskyblue')
commandEndLabelS.grid(row = 1, column = 6)
commandEndEntryS = Entry(commandFileFrame, width = 4)
commandEndEntryS.grid(row = 1, column = 7)

commandButton = Button(commandFrame, text = "동영상 자르기", command = lambda: videoM(commandFileEntry.get(), commandStartEntryH.get(), commandStartEntryM.get(), commandStartEntryS.get(), commandEndEntryH.get(), commandEndEntryM.get(), commandEndEntryS.get()), background = 'white')
commandButton.pack(padx = 10, pady = 10)

messageFrame2 = Frame(tk)
messageFrame2.configure(background = 'deepskyblue')
messageFrame2.pack(padx = 20, pady = 20)
messageLabel2 = Label(messageFrame2, text = "변환된 동영상 이름은 원본 동영상 이름 앞에 [C]가 추가됩니다.", background = 'deepskyblue')
messageLabel2.pack()

tk.mainloop()
#!/usr/bin/env python3
# Tic Tac Toe using TKinter
# importing stuff
import tkinter as tk
from tkinter import ttk
from random import randrange
# defining variables
gamecompleted = 0
turn = 'X'
Board = {'TL':' ','TM':' ','TR':' ',
	'ML':' ','MM':' ','MR':' ',
	'BL':' ','BM':' ','BR':' '}
Boardscore = [0,0,0,0,0,0,0,0,0]
think = 0
# click functions
def TLclick():
	global gamecompleted
	global turn
	if Board['TL'] == ' ' and gamecompleted !=1:
		Board['TL'] = turn
		TL.config(text=Board['TL'])
		check()
def TMclick():
	global gamecompleted
	global turn
	if Board['TM'] == ' ' and gamecompleted !=1:
		Board['TM'] = turn
		TM.config(text=Board['TM'])
		check()
def TRclick():
	global gamecompleted
	global turn
	if Board['TR'] == ' ' and gamecompleted !=1:
		Board['TR'] = turn
		TR.config(text=Board['TR'])
		check()
def MLclick():
	global gamecompleted
	global turn
	if Board['ML'] == ' ' and gamecompleted !=1:
		Board['ML'] = turn
		ML.config(text=Board['ML'])
		check()
def MMclick():
	global gamecompleted
	global turn
	if Board['MM'] == ' ' and gamecompleted !=1:
		Board['MM'] = turn
		MM.config(text=Board['MM'])
		check()
def MRclick():
	global gamecompleted
	global turn
	if Board['MR'] == ' ' and gamecompleted !=1:
		Board['MR'] = turn
		MR.config(text=Board['MR'])
		check()
def BLclick():
	global gamecompleted
	global turn
	if Board['BL'] == ' ' and gamecompleted !=1:
		Board['BL'] = turn
		BL.config(text=Board['BL'])
		check()
def BMclick():
	global gamecompleted
	global turn
	if Board['BM'] == ' ' and gamecompleted !=1:
		Board['BM'] = turn
		BM.config(text=Board['BM'])
		check()
def BRclick():
	global gamecompleted
	global turn
	if Board['BR'] == ' ' and gamecompleted !=1:
		Board['BR'] = turn
		BR.config(text=Board['BR'])
		check()
# making the TKinter window
window = tk.Tk()
window.geometry('768x700')
window.title('Tic Tac Toe.py')
frame = tk.Frame(window) # the frame for the grid/board
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
Bar = ttk.Progressbar(window, orient='horizontal', length=500, mode='determinate', maximum=360880)
name = tk.Label(window, text='Tic Tac Toe Game', font=('Times New Roman', 30)) # the name on the top of the board
# The buttons & things + neccesary functions
TL = tk.Button(frame, text=Board['TL'], font=('Times New Roman', 80), width=2, command=TLclick)
TM = tk.Button(frame, text=Board['TM'], font=('Times New Roman', 80), width=2, command=TMclick)
TR = tk.Button(frame, text=Board['TR'], font=('Times New Roman', 80), width=2, command=TRclick)
ML = tk.Button(frame, text=Board['ML'], font=('Times New Roman', 80), width=2, command=MLclick)
MM = tk.Button(frame, text=Board['MM'], font=('Times New Roman', 80), width=2, command=MMclick)
MR = tk.Button(frame, text=Board['MR'], font=('Times New Roman', 80), width=2, command=MRclick)
BL = tk.Button(frame, text=Board['BL'], font=('Times New Roman', 80), width=2, command=BLclick)
BM = tk.Button(frame, text=Board['BM'], font=('Times New Roman', 80), width=2, command=BMclick)
BR = tk.Button(frame, text=Board['BR'], font=('Times New Roman', 80), width=2, command=BRclick)
def updatebtn(): # function to update all of the buttons (It has to be placed after the buttons are defined)
	TL.config(text=Board['TL'])
	TM.config(text=Board['TM'])
	TR.config(text=Board['TR'])
	ML.config(text=Board['ML'])
	MM.config(text=Board['MM'])
	MR.config(text=Board['MR'])
	BL.config(text=Board['BL'])
	BM.config(text=Board['BM'])
	BR.config(text=Board['BR'])
def reset(): # resets the board
	global Board
	global turn
	global gamecompleted
	Board = {'TL':' ','TM':' ','TR':' ',
		'ML':' ','MM':' ','MR':' ',
		'BL':' ','BM':' ','BR':' '}
	turn = 'X'
	gamecompleted = 0
	updatebtn()
	resetbtn.config(text='[RESET?]')
def wincheck(change): # checks if a player has won
	global gamecompleted
	global Board
	updatebtn()
	if Board['TL'] == Board['MM'] and Board['BR'] == Board ['TL'] and Board['MM'] != ' ':
		win = Board["MM"]
	elif Board['TR'] == Board['MM'] and Board['BL'] == Board['TR'] and Board['MM'] != ' ':
		win = Board["MM"]
	elif Board['TL'] == Board['TM'] and Board['TR'] == Board['TL'] and Board['TM'] != ' ':
		win = Board["TM"]
	elif Board['TL'] == Board['ML'] and Board['BL'] == Board['TL'] and Board['ML'] != ' ':
		win = Board["ML"]
	elif Board['ML'] == Board['MM'] and Board['MR'] == Board['ML'] and Board['MM'] != ' ':
		win = Board["MM"]
	elif Board['TM'] == Board['MM'] and Board['BM'] == Board['TM'] and Board['MM'] != ' ':
		win = Board["MM"]
	elif Board['BL'] == Board['BM'] and Board['BR'] == Board['BL'] and Board['BM'] != ' ':
		win = Board["BM"]
	elif Board['TR'] == Board['MR'] and Board['BR'] == Board['TR'] and Board['MR'] != ' ':
		win = Board["MR"]
	elif ' ' not in list(Board.values()):
		win = 'Tie'
	else:
		win = ' '
	if win == 'X':
		if change == 1:
			resetbtn.configure(text='X wins! [Reset?]')
			gamecompleted = 1
		else:
			return(1)
	elif win == 'O':
		if change == 1:
			resetbtn.configure(text='O wins! [Reset?]')
			gamecompleted = 1
		else:
			return(-1)
	elif win == 'Tie':
		if change == 1:
			resetbtn.configure(text='It\'s a Tie! [Reset?]')
			gamecompleted = 1
		else:
			return(0)
	else:
		return(0)
def easybot(): # defines an easy bot
	global turn
	global Board
	if gamemode[0] == 'E' and gamecompleted != 1:
		number = randrange(0,9)
		Boardlist = [Board['TL'], Board['TM'], Board['TR'],
			Board['ML'], Board['MM'], Board['MR'],
			Board['BL'], Board['BM'], Board['BR']]
		while True:
			number = randrange(0,9)
			if Boardlist[number] == ' ':
				break
			if ' ' not in Boardlist:
				break
		if ' ' in Boardlist:
			if number == 0:
				Board['TL'] = turn
			elif number == 1:
				Board['TM'] = turn
			elif number == 2:
				Board['TR']= turn
			elif number == 3:
				Board['ML'] = turn
			elif number == 4:
				Board['MM'] = turn
			elif number == 5:
				Board['MR'] = turn
			elif number == 6:
				Board['BL'] = turn
			elif number == 7:
				Board['BM'] = turn
			elif number == 8:
				Board['BR'] = turn
		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'
		updatebtn()
		wincheck(1)
def Hardbot(nBoard, place, scor, tun, orig, tree, tu): # creates a function for a hard bot (it's unfinished)
	if gamemode[0] == 'H':
		global Boardscore
		global turn
		global Board
		global think
		think += 1
		if orig == 1:
			Boardscore = [0,0,0,0,0,0,0,0,0]
			think = 0
			Bar.pack(padx=10, pady=20)
		Bar['value'] = think
		window.update_idletasks()
		tBoardlist = [nBoard['TL'], nBoard['TM'], nBoard['TR'], nBoard['ML'], nBoard['MM'], nBoard['MR'], nBoard['BL'], nBoard['BM'], nBoard['BR']]
		tBoard = {'TL':nBoard['TL'], 'TM':nBoard['TM'], 'TR':nBoard['TR'], 'ML':nBoard['ML'], 'MM':nBoard['MM'], 'MR':nBoard['MR'], 'BL':nBoard['BL'], 'BM':nBoard['BM'], 'BR':nBoard['BR']}
		ik = {
    		0: 'TL', 1: 'TM', 2: 'TR',
    		3: 'ML', 4: 'MM', 5: 'MR',
    		6: 'BL', 7: 'BM', 8: 'BR'}
		if tree != 69:
			tBoard[ik[tree]] = tu
			tBoardlist[tree] = tu
		Boardscore[place] = scor
		for i in range(9):
			if ' ' not in tBoardlist:
				Boardscore[i] = (Boardscore[i] + wincheck(0)) / 2
			elif tBoardlist[i] == ' ':
				if tun == 'X':
					tur = 'O'
				else:
					tur = 'X'
				Hardbot(tBoard, i, Boardscore[i], tur, 0, i, tun)
		if orig == 1:
			if tun == 'X':
				bestscore = [-2,0]
				for i in range(9):
					if Boardscore[i] > bestscore[0]:
						bestscore[0] = Boardscore[i]
						bestscore[1] = i
			else:
				bestscore = [2, 0]
				for i in range(9):
					if Boardscore[i] < bestscore[0]:
						bestscore[0] = Boardscore[i]
						bestscore[1] = i
			if bestscore[1] == 0:
				Board['TL'] = turn
			elif bestscore[1] == 1:
				Board['TM'] = turn
			elif bestscore[1] == 2:
				Board['TR']= turn
			elif bestscore[1] == 3:
				Board['ML'] = turn
			elif bestscore[1] == 4:
				Board['MM'] = turn
			elif bestscore[1] == 5:
				Board['MR'] = turn
			elif bestscore[1] == 6:
				Board['BL'] = turn
			elif bestscore[1] == 7:
				Board['BM'] = turn
			elif bestscore[1] == 8:
				Board['BR'] = turn
			updatebtn()
			wincheck(1)
def check(): # function to change X to O & vice versa & start other functions
	global Board
	global turn
	global gamecompleted
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
	wincheck(1)
	easybot()
	Hardbot(Board, 0, 0, turn, 1, 69, 0)
resetbtn = tk.Button(window, text='Reset the board', font=('Times New Roman', 18), command=reset) # the button to reset the board
# placing all the widgets
def game_start():
	name.pack(padx=5, pady=5)
	frame.pack(padx=12, pady=40)
	TL.grid(row=0,column=0, sticky=tk.W+tk.E)
	TM.grid(row=0,column=1, sticky=tk.W+tk.E)
	TR.grid(row=0,column=2, sticky=tk.W+tk.E)
	ML.grid(row=1,column=0, sticky=tk.W+tk.E)
	MM.grid(row=1,column=1, sticky=tk.W+tk.E)
	MR.grid(row=1,column=2, sticky=tk.W+tk.E)
	BL.grid(row=2,column=0, sticky=tk.W+tk.E)
	BM.grid(row=2,column=1, sticky=tk.W+tk.E)
	BR.grid(row=2,column=2, sticky=tk.W+tk.E)
	resetbtn.pack(padx=5, pady=10)
def Introfin():
	Intro.pack_forget()
	Introbtnl.grid_forget()
	Introbtne.grid_forget()
	Introbtnh.grid_forget()
	frame.pack_forget()
def Introfin2():
	Intro2.pack_forget()
	IntrobtnX.grid_forget()
	IntrobtnO.grid_forget()
	game_start()
def X():
	global turn
	turn = 'X'
	Introfin2()
def O():
	global turn
	turn = 'O'
	Introfin2()
def local(): # function to go from intro to the next part of the intro
	global turn
	turn = 'X'
	Introfin()
	game_start()
Intro2 = tk.Label(window, text='Would you like to be X or O?', font=('Times New Roman', 18))
IntrobtnX = tk.Button(frame, text='X', font=('Times New Roman', 18), command=X)
IntrobtnO = tk.Button(frame, text='O', font=('Times New Roman', 18), command=O)
def easy():
	global turn
	global gamemode
	gamemode = 'Easy Bot'
	Introfin()
	Intro2.pack(padx = 20, pady = 10)
	frame.pack(padx=12, pady=40)
	IntrobtnX.grid(row=0, column=0, sticky=tk.W+tk.E)
	IntrobtnO.grid(row=0, column=3, sticky=tk.W+tk.E)
def hard():
	global turn
	global gamemode
	gamemode = 'Hard Bot'
	Introfin()
	Intro2.pack(padx = 20, pady = 10)
	frame.pack(padx=12, pady=40)
	IntrobtnX.grid(row=0, column=0, sticky=tk.W+tk.E)
	IntrobtnO.grid(row=0, column=3, sticky=tk.W+tk.E)
Intro = tk.Label(window, text='Welcome to Tic Tac Toe.py\nWhat gamemode would you like to play?', font=('Times New Roman', 18))
Introbtnl = tk.Button(frame, text='Local 1v1', font=('Times New Roman', 18), command=local)
Introbtne = tk.Button(frame, text='Easy Bot', font=('Times New Roman', 18), command=easy)
Introbtnh = tk.Button(frame, text='Hard Bot', font=('Times New Roman', 18), command=hard)
Intro.pack(padx = 20, pady = 10)
frame.pack(padx=12, pady=40)
Introbtnl.grid(row=0, column=0, sticky=tk.W+tk.E)
Introbtne.grid(row=0, column=1, sticky=tk.W+tk.E)
Introbtnh.grid(row=0, column=2, sticky=tk.W+tk.E)
window.mainloop()

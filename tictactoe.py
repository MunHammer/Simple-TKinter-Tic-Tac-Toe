#!/usr/bin/env python3
# Tic Tac Toe using TKinter
import tkinter as tk
from random import randrange
gamecompleted = 0
Board = {'TL':' ','TM':' ','TR':' ',
	'ML':' ','MM':' ','MR':' ',
	'BL':' ','BM':' ','BR':' '}
gamemode = input('You are now playing tic tac toe.\nWhat gamemode would you like to play an \n- local 1v1\n- easy bot\nI\'d like to play an ').upper()
turn = 'X'
window = tk.Tk()
window.geometry('768x700')
window.title('Tic Tac Toe.py')
frame = tk.Frame(window)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
def TLclick():
	global gamecompleted
	if Board['TL'] == ' ' and gamecompleted !=1:
		global turn
		Board['TL'] = turn
		TL.config(text=Board['TL'])
		check()
def TMclick():
	global gamecompleted
	if Board['TM'] == ' ' and gamecompleted !=1:
		global turn
		Board['TM'] = turn
		TM.config(text=Board['TM'])
		check()
def TRclick():
	global gamecompleted
	if Board['TR'] == ' ' and gamecompleted !=1:
		global turn
		Board['TR'] = turn
		TR.config(text=Board['TR'])
		check()
def MLclick():
	global gamecompleted
	if Board['ML'] == ' ' and gamecompleted !=1:
		global turn
		Board['ML'] = turn
		ML.config(text=Board['ML'])
		check()
def MMclick():
	global gamecompleted
	if Board['MM'] == ' ' and gamecompleted !=1:
		global turn
		Board['MM'] = turn
		MM.config(text=Board['MM'])
		check()
def MRclick():
	global gamecompleted
	if Board['MR'] == ' ' and gamecompleted !=1:
		global turn
		Board['MR'] = turn
		MR.config(text=Board['MR'])
		check()
def BLclick():
	global gamecompleted
	if Board['BL'] == ' ' and gamecompleted !=1:
		global turn
		Board['BL'] = turn
		BL.config(text=Board['BL'])
		check()
def BMclick():
	global gamecompleted
	if Board['BM'] == ' ' and gamecompleted !=1:
		global turn
		Board['BM'] = turn
		BM.config(text=Board['BM'])
		check()
def BRclick():
	global gamecompleted
	if Board['BR'] == ' ' and gamecompleted !=1:
		global turn
		Board['BR'] = turn
		BR.config(text=Board['BR'])
		check()
TL = tk.Button(frame, text=Board['TL'], font=('Times New Roman', 80), width=2, command=TLclick)
TL.grid(row=0,column=0, sticky=tk.W+tk.E)
TM = tk.Button(frame, text=Board['TM'], font=('Times New Roman', 80), width=2, command=TMclick)
TM.grid(row=0,column=1, sticky=tk.W+tk.E)
TR = tk.Button(frame, text=Board['TR'], font=('Times New Roman', 80), width=2, command=TRclick)
TR.grid(row=0,column=2, sticky=tk.W+tk.E)
ML = tk.Button(frame, text=Board['ML'], font=('Times New Roman', 80), width=2, command=MLclick)
ML.grid(row=1,column=0, sticky=tk.W+tk.E)
MM = tk.Button(frame, text=Board['MM'], font=('Times New Roman', 80), width=2, command=MMclick)
MM.grid(row=1,column=1, sticky=tk.W+tk.E)
MR = tk.Button(frame, text=Board['MR'], font=('Times New Roman', 80), width=2, command=MRclick)
MR.grid(row=1,column=2, sticky=tk.W+tk.E)
BL = tk.Button(frame, text=Board['BL'], font=('Times New Roman', 80), width=2, command=BLclick)
BL.grid(row=2,column=0, sticky=tk.W+tk.E)
BM = tk.Button(frame, text=Board['BM'], font=('Times New Roman', 80), width=2, command=BMclick)
BM.grid(row=2,column=1, sticky=tk.W+tk.E)
BR = tk.Button(frame, text=Board['BR'], font=('Times New Roman', 80), width=2, command=BRclick)
BR.grid(row=2,column=2, sticky=tk.W+tk.E)
def updatebtn():
	TL.config(text=Board['TL'])
	TM.config(text=Board['TM'])
	TR.config(text=Board['TR'])
	ML.config(text=Board['ML'])
	MM.config(text=Board['MM'])
	MR.config(text=Board['MR'])
	BL.config(text=Board['BL'])
	BM.config(text=Board['BM'])
	BR.config(text=Board['BR'])
def reset():
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
resetbtn = tk.Button(window, text='Reset the board', font=('Times New Roman', 18), command=reset)
def wincheck():
	global gamecompleted
	global Board
	updatebtn()
	if Board['TL'] == Board['MM'] and Board['BR'] == Board ['TL'] and Board['MM'] != ' ':
		resetbtn.config(text=Board["MM"] + ' wins!, [RESET?]')
		gamecompleted = 1
	elif Board['TR'] == Board['MM'] and Board['BL'] == Board['TR'] and Board['MM'] != ' ':
		resetbtn.config(text=Board["MM"] + ' wins!, [RESET?]')
		gamecompleted = 1
	elif Board['TL'] == Board['TM'] and Board['TR'] == Board['TL'] and Board['TM'] != ' ':
		resetbtn.config(text=f'{Board["TM"]} wins!, [RESET?]')
		gamecompleted = 1
	elif Board['TL'] == Board['ML'] and Board['BL'] == Board['TL'] and Board['ML'] != ' ':
		resetbtn.config(text=f'{Board["TL"]} wins!, [RESET?]')
		gamecompleted = 1
	elif Board['ML'] == Board['MM'] and Board['MR'] == Board['ML'] and Board['MM'] != ' ':
		resetbtn.config(text=f'{Board["MM"]} wins!, [RESET?]')
		gamecompleted = 1
	elif Board['TM'] == Board['MM'] and Board['BM'] == Board['TM'] and Board['MM'] != ' ':
		resetbtn.config(text=f'{Board["MM"]} wins!, [RESET?]')
		gamecompleted = 1
	elif Board['BL'] == Board['BM'] and Board['BR'] == Board['BL'] and Board['BM'] != ' ':
		resetbtn.config(text=f'{Board["BM"]} wins!, [RESET?]')
		gamecompleted = 1
	elif Board['TR'] == Board['MR'] and Board['BR'] == Board['TR'] and Board['MR'] != ' ':
		resetbtn.config(text=f'{Board["MR"]} wins!, [RESET?]')
		gamecompleted = 1
	elif ' ' not in list(Board.values()):
		resetbtn.config(text='It\'s a tie!, [RESET?]')
		gamecompleted = 1
def check():
	global Board
	global turn
	global gamecompleted
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
	wincheck()
	if gamemode[0] == 'E':
		number = randrange(0,9)
		continuew = 1
		Boardlist = [Board['TL'], Board['TM'], Board['TR'],
			Board['ML'], Board['MM'], Board['MR'],
			Board['BL'], Board['BM'], Board['BR']]
		while continuew == 1:
			number = randrange(0,9)
			if Boardlist[number] != ' ':
				continuew = 1
			else:
				continuew = 0
			if ' ' not in Boardlist:
				continuew = 0
		if ' ' in Boardlist:
			if number == 0:
				Board['TL'] = 'X'
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
		turn = 'X'
		updatebtn()
		wincheck()
name = tk.Label(window, text='Tic Tac Toe Game', font=('Times New Roman', 30))
name.pack(padx=5, pady=5)
frame.pack(padx=12, pady=40)
resetbtn.pack(padx=5, pady=10)
window.mainloop()

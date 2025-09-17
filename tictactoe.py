#!/usr/bin/env python3
# Tic Tac Toe using TKinter
# importing stuff
import tkinter as tk
from random import randrange
# defining variables
gamecompleted = 0
Board = {'TL':' ','TM':' ','TR':' ',
	'ML':' ','MM':' ','MR':' ',
	'BL':' ','BM':' ','BR':' '}
# defining functions
def wincheck(): # checks if a player has won
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
def check(): # function to change X to O & vice versa & start other functions
	global Board
	global turn
	global gamecompleted
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
	wincheck()
	if gamemode[0] == 'E': # start of the easy bot code
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
		wincheck()
	elif gamemode == 'H': # start of hard bot code & end of easy bot code
		tboard = [Board['TL'], Board['TM'], Board['TR'],
			Board['ML'], Board['MM'], Board['MR'],
			Board['BL'], Board['BM'], Board['BR']] # theoretical board
		if tboard['TL'] == ' ':
			pass
def updatebtn(): # function to update all of the buttons
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
# text to talk to the player
gamemode = input('You are now playing tic tac toe.\nWhat gamemode would you like to play an \n- local 1v1\n- easy bot\nI\'d like to play an ').upper()
if gamemode[0] == 'E':
	turn = input('would you like to be X or O?\n')
	if turn[0] == 'X':
		turn = 'X'
	else:
		turn = 'O'
		check()
# making the TKinter window
window = tk.Tk()
window.geometry('768x700')
window.title('Tic Tac Toe.py')
frame = tk.Frame(window) # the frame for the grid/board
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
name = tk.Label(window, text='Tic Tac Toe Game', font=('Times New Roman', 30)) # the name on the top of the board
# The buttons inside the grid
TL = tk.Button(frame, text=Board['TL'], font=('Times New Roman', 80), width=2, command=TLclick)
TM = tk.Button(frame, text=Board['TM'], font=('Times New Roman', 80), width=2, command=TMclick)
TR = tk.Button(frame, text=Board['TR'], font=('Times New Roman', 80), width=2, command=TRclick)
ML = tk.Button(frame, text=Board['ML'], font=('Times New Roman', 80), width=2, command=MLclick)
MM = tk.Button(frame, text=Board['MM'], font=('Times New Roman', 80), width=2, command=MMclick)
MR = tk.Button(frame, text=Board['MR'], font=('Times New Roman', 80), width=2, command=MRclick)
BL = tk.Button(frame, text=Board['BL'], font=('Times New Roman', 80), width=2, command=BLclick)
BM = tk.Button(frame, text=Board['BM'], font=('Times New Roman', 80), width=2, command=BMclick)
BR = tk.Button(frame, text=Board['BR'], font=('Times New Roman', 80), width=2, command=BRclick)
resetbtn = tk.Button(window, text='Reset the board', font=('Times New Roman', 18), command=reset) # the button to reset the board
# placing all the widgets
TL.grid(row=0,column=0, sticky=tk.W+tk.E)
TM.grid(row=0,column=1, sticky=tk.W+tk.E)
TR.grid(row=0,column=2, sticky=tk.W+tk.E)
ML.grid(row=1,column=0, sticky=tk.W+tk.E)
MM.grid(row=1,column=1, sticky=tk.W+tk.E)
MR.grid(row=1,column=2, sticky=tk.W+tk.E)
BL.grid(row=2,column=0, sticky=tk.W+tk.E)
BM.grid(row=2,column=1, sticky=tk.W+tk.E)
BR.grid(row=2,column=2, sticky=tk.W+tk.E)
name.pack(padx=5, pady=5)
frame.pack(padx=12, pady=40)
resetbtn.pack(padx=5, pady=10)
window.mainloop()

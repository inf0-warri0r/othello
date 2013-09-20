#! /usr/bin/env python

"""
Author : tharindra galahena (inf0_warri0r)
Project: Othello game AI using tempreal difference learning
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 20/09/2013
License:

     Copyright 2013 Tharindra Galahena

This is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
this. If not, see http://www.gnu.org/licenses/.
"""


from Tkinter import *
import random
import copy


class state:
    def __init__(self):
        self.grid = list()
        self.reset()

    def reset(self):
        self.grid = list()
        for i in range(0, 8):
            tmp = list()
            for j in range(0, 8):
                tmp.append('0')
            self.grid.append(tmp)
        self.grid[3][3] = '2'
        self.grid[3][4] = '1'
        self.grid[4][3] = '1'
        self.grid[4][4] = '2'

    def get_cross_moves_1(self, a, b):

        moves = list()
        y = 0
        for i in range(0, 8):
            f = False
            y = 0
            x = i
            while x < 8 and y < 8:
                if not f and self.grid[y][x] == a:
                    f = True
                elif f and self.grid[y][x] == '0':
                    if x > 0 and y > 0 and self.grid[y - 1][x - 1] == b:
                        moves.append((x, y))
                    f = False
                x = x + 1
                y = y + 1

            f = False
            y = 7
            x = i
            while x >= 0 and y >= 0:
                if not f and self.grid[y][x] == a:
                    f = True
                elif f and self.grid[y][x] == '0':
                    if x < 7 and y < 7 and self.grid[y + 1][x + 1] == b:
                        moves.append((x, y))
                    f = False
                x = x - 1
                y = y - 1

        x = 0
        for i in range(0, 8):
            f = False
            x = 0
            y = i
            while x < 8 and y < 8:
                if not f and self.grid[y][x] == a:
                    f = True
                elif f and self.grid[y][x] == '0':
                    if x > 0 and y > 0 and self.grid[y - 1][x - 1] == b:
                        moves.append((x, y))
                    f = False
                x = x + 1
                y = y + 1

            f = False
            x = 7
            y = i
            while x >= 0 and y >= 0:
                if not f and self.grid[y][x] == a:
                    f = True
                elif f and self.grid[y][x] == '0':
                    if x < 7 and y < 7 and self.grid[y + 1][x + 1] == b:
                        moves.append((x, y))
                    f = False
                x = x - 1
                y = y - 1
        return moves

    def get_cross_moves_2(self, a, b):
        moves = list()
        y = 0
        for i in range(0, 8):
            f = False
            y = 0
            x = i
            while x >= 0 and y < 8:
                if not f and self.grid[y][x] == a:
                    f = True
                elif f and self.grid[y][x] == '0':
                    if x < 7 and y > 0 and self.grid[y - 1][x + 1] == b:
                        moves.append((x, y))
                    f = False
                x = x - 1
                y = y + 1

            f = False
            y = 7
            x = i
            while x < 8 and y >= 0:
                if not f and self.grid[y][x] == a:
                    f = True
                elif f and self.grid[y][x] == '0':
                    if x > 0 and y < 7 and self.grid[y + 1][x - 1] == b:
                        moves.append((x, y))
                    f = False
                x = x + 1
                y = y - 1

        x = 0
        for i in range(0, 8):
            f = False
            x = 7
            y = i
            while x >= 0 and y < 8:
                if not f and self.grid[y][x] == a:
                    f = True
                elif f and self.grid[y][x] == '0':
                    if x < 7 and y > 0 and self.grid[y - 1][x + 1] == b:
                        moves.append((x, y))
                    f = False
                x = x - 1
                y = y + 1

            f = False
            x = 0
            y = i
            while x < 8 and y >= 0:
                if not f and self.grid[y][x] == a:
                    f = True
                elif f and self.grid[y][x] == '0':
                    if x > 0 and y < 7 and self.grid[y + 1][x - 1] == b:
                        moves.append((x, y))
                    f = False
                x = x + 1
                y = y - 1
        return moves

    def get_strate_moves(self, a, b):

        moves = list()
        for y in range(0, 8):
            f = False
            for x in range(0, 8):
                if not f and self.grid[y][x] == a:
                    f = True
                elif f and self.grid[y][x] == '0':
                    if x > 0 and self.grid[y][x - 1] == b:
                        moves.append((x, y))
                    f = False
            f = False
            for x in range(7, -1, -1):
                if not f and self.grid[y][x] == a:
                    f = True
                elif f and self.grid[y][x] == '0':
                    if x < 7 and self.grid[y][x + 1] == b:
                        moves.append((x, y))
                    f = False

        for x in range(0, 8):
            f = False
            for y in range(0, 8):
                if not f and self.grid[y][x] == a:
                    f = True
                elif f and self.grid[y][x] == '0':
                    if y > 0 and self.grid[y - 1][x] == b:
                        moves.append((x, y))
                    f = False
            f = False
            for y in range(7, -1, -1):
                if not f and self.grid[y][x] == a:
                    f = True
                elif f and self.grid[y][x] == '0':
                    if y < 7 and self.grid[y + 1][x] == b:
                        moves.append((x, y))
                    f = False

        return moves

    def get_black_moves(self):
        m1 = self.get_cross_moves_1('2', '1')
        m2 = self.get_cross_moves_2('2', '1')
        m3 = self.get_strate_moves('2', '1')

        return list(set(m1 + m2 + m3))

    def get_white_moves(self):
        m1 = self.get_cross_moves_1('1', '2')
        m2 = self.get_cross_moves_2('1', '2')
        m3 = self.get_strate_moves('1', '2')

        return list(set(m1 + m2 + m3))

    def get_white_score(self):
        score = 0
        for y in range(0, 8):
            for x in range(0, 8):
                if self.grid[y][x] == '1':
                    score = score + 1

        return score

    def get_black_score(self):
        score = 0
        for y in range(0, 8):
            for x in range(0, 8):
                if self.grid[y][x] == '2':
                    score = score + 1

        return score

    def next_state(self, move, a, b):
        new = list()
        mx, my = move
        mx = mx + 1
        sc = list()
        while mx < 8 and self.grid[my][mx] == a:
            sc.append((mx, my))
            mx = mx + 1

        if my < 8 and my > -1 and mx < 8 and mx > -1:
            if self.grid[my][mx] == b:
                new = new + sc

        mx, my = move
        mx = mx - 1
        sc = list()
        while mx > -1 and self.grid[my][mx] == a:
            sc.append((mx, my))
            mx = mx - 1

        if my < 8 and my > -1 and mx < 8 and mx > -1:
            if self.grid[my][mx] == b:
                new = new + sc

        mx, my = move
        my = my + 1
        sc = list()
        while my < 8 and self.grid[my][mx] == a:
            sc.append((mx, my))
            my = my + 1

        if my < 8 and my > -1 and mx < 8 and mx > -1:
            if self.grid[my][mx] == b:
                new = new + sc

        mx, my = move
        my = my - 1
        sc = list()
        while my > -1 and self.grid[my][mx] == a:
            sc.append((mx, my))
            my = my - 1

        if my < 8 and my > -1 and mx < 8 and mx > -1:
            if self.grid[my][mx] == b:
                new = new + sc

        mx, my = move
        mx = mx + 1
        my = my + 1
        sc = list()
        while mx < 8 and my < 8 and self.grid[my][mx] == a:
            sc.append((mx, my))
            mx = mx + 1
            my = my + 1

        if my < 8 and my > -1 and mx < 8 and mx > -1:
            if self.grid[my][mx] == b:
                new = new + sc

        mx, my = move
        mx = mx - 1
        my = my - 1
        sc = list()
        while mx > -1 and my > -1 and self.grid[my][mx] == a:
            sc.append((mx, my))
            mx = mx - 1
            my = my - 1

        if my < 8 and my > -1 and mx < 8 and mx > -1:
            if self.grid[my][mx] == b:
                new = new + sc

        mx, my = move
        mx = mx - 1
        my = my + 1
        sc = list()
        while mx > -1 and my < 8 and self.grid[my][mx] == a:
            sc.append((mx, my))
            mx = mx - 1
            my = my + 1

        if my < 8 and my > -1 and mx < 8 and mx > -1:
            if self.grid[my][mx] == b:
                new = new + sc

        mx, my = move
        mx = mx + 1
        my = my - 1
        sc = list()
        while mx < 8 and my > -1 and self.grid[my][mx] == a:
            sc.append((mx, my))
            mx = mx + 1
            my = my - 1

        if my < 8 and my > -1 and mx < 8 and mx > -1:
            if self.grid[my][mx] == b:
                new = new + sc

        for m in new:
            self.grid[m[1]][m[0]] = b

        self.grid[move[1]][move[0]] = b

    def is_final(self):
        for y in range(0, 8):
            for x in range(0, 8):
                if self.grid[y][x] == '0':
                    return False
        return True


class game:

    def __init__(self):
        self.a = random.uniform(-1.0, 1.0)
        self.b = random.uniform(-1.0, 1.0)
        self.c = random.uniform(-1.0, 1.0)
        self.r = 0.9
        self.learnng_rate = 0.2
        self.current_state = state()

    def find_input_a(self, state1, state2):
        moves = state2.get_white_moves()
        score = state2.get_white_score()
        mx = 0
        for move in moves:
            tmp = copy.deepcopy(state2)
            tmp.next_state(move, '1', '2')
            score = tmp.get_white_score() - score
            if mx < score:
                mx = score

        return (64.0 - mx) / 64.0

    def find_input_b(self, state):
        moves = state.get_black_moves()
        score = state.get_black_score()
        mx = 0
        for move in moves:
            tmp = copy.deepcopy(state)
            tmp.next_state(move, '1', '2')
            score = tmp.get_black_score() - score
            if mx < score:
                mx = score

        return (64.0 - mx) / 64.0

    def find_input_c(self, state):
        moves_b = state.get_black_moves()
        moves_w = state.get_white_moves()

        if len(moves_b) == 0:
            return 100.0

        return float(len(moves_w)) / len(moves_b)

    def find_v(self, tmp):
        ia = self.find_input_a(self.current_state, tmp)
        ib = self.find_input_b(tmp)

        v = self.a * ia + self.b * ib + self.c * ic

        return v, ia, ib, ic

    def find_move(self):
        moves = self.current_state.get_white_moves()
        max_v = -10000000
        mv = self.current_state, (-1, -1)
        mia = 0
        mib = 0
        mic = 0

        if len(moves) == 0:
            print "oops!"
            return -1

        lst = list()
        for move in moves:
            tmp = copy.deepcopy(self.current_state)
            tmp.next_state(move, '2', '1')
            v, ia, ib, ic = self.find_v(tmp)

            v = self.r * v
            lst.append((v, (tmp, move), ia, ib, ic))
        lst = sorted(lst)
        max_v, mv, mia, mib, mic = lst[len(lst) - 1]
        print "ia = ", mia, " ib = ", mib, " ic = ", mic, " move = ", mv[1]
        return mv[0], max_v, mia, mib, mic

    def learn(self, state, v, ia, ib, ic):
        v2, mia, mib, mic = self.find_v(state)
        v2 = self.r * v2
        ws = state.get_white_score()
        bs = state.get_black_score()
        if state.is_final():
            if ws > bs:
                v2 = v2 + 100
            elif ws < bs:
                v2 = v2 - 100
        #else:
            #v2 = v2 + ws - bs

        print "lia = ", ia, " lib = ", ib, " lic = ", ic
        print "v = ", v, " v2 = ", v2
        self.a = self.a + self.learnng_rate * (v2 - v) * ia
        self.b = self.b + self.learnng_rate * (v2 - v) * ib
        self.c = self.c + self.learnng_rate * (v2 - v) * ic
        print "a = ", self.a, " b = ", self.b, " c = ", self.c

g = game()
f = False
v = 0

ia = 0
ib = 0
ic = 0

root = Tk()
root.title("othello")

cw = 400
ch = 500

chart_1 = Canvas(root, width=cw, height=ch, background="black")
chart_1.grid(row=0, column=0)


next_x = -1
next_y = -1
moved = False


def callback(event):
    global next_x, next_y, moved
    next_x = int(event.x / 50)
    next_y = int(event.y / 50)
    moved = True

chart_1.bind("<Button-1>", callback)

ww = 0
bb = 0

while 1:

    for i in range(0, 9):
        chart_1.create_line(i * 50, 0, i * 50, 400,
                        fill='red')
        chart_1.create_line(0, i * 50, 400, i * 50,
                        fill='red')

    for y in range(0, 8):
        for x in range(0, 8):
            if g.current_state.grid[y][x] == '2':
                chart_1.create_oval(x * 50, y * 50,
                                    (x + 1) * 50, (y + 1) * 50,
                                    fill='green')
            elif g.current_state.grid[y][x] == '1':
                chart_1.create_oval(x * 50, y * 50,
                                    (x + 1) * 50, (y + 1) * 50,
                                    fill='yellow')

    if moved:
        print g.a, " ", g.b, " ", g.c
        print "-----------------> ", next_x, " ", next_y
        moved = False
        moves = g.current_state.get_black_moves()
        if (next_x, next_y) in moves:
            moved = False
            g.current_state.next_state((next_x, next_y), '1', '2')

            if f:
                g.learn(g.current_state, v, ia, ib, ic)
            else:
                f = True

            ff = True
            mov = g.find_move()
            if mov != -1:
                stat, v, ia, ib, ic = mov
                g.current_state = stat
            else:
                if len(g.current_state.get_black_moves()) == 0:
                    w = g.current_state.get_white_score()
                    b = g.current_state.get_black_score()
                    print "w = ", w, " b = ", b
                    if b > w:
                        bb = bb + 1
                    elif b < w:
                        ww = ww + 1
                    g.current_state.reset()
                    ff = False
                    f = False

            if ff:
                while len(g.current_state.get_black_moves()) == 0:
                    mov = g.find_move()
                    if mov != -1:
                        stat, v, ia, ib, ic = mov
                        g.current_state = stat
                    else:
                        if len(g.current_state.get_black_moves()) == 0:
                            w = g.current_state.get_white_score()
                            b = g.current_state.get_black_score()
                            print "w = ", w, " b = ", b
                            if b > w:
                                bb = bb + 1
                            elif b < w:
                                ww = ww + 1
                            g.current_state.reset()
                            f = False
                            break
            else:
                ff = False

        else:
            print "wrong move"

        if g.current_state.is_final():
            w = g.current_state.get_white_score()
            b = g.current_state.get_black_score()
            g.current_state.reset()

    w = g.current_state.get_white_score()
    b = g.current_state.get_black_score()

    txt = 'squears : AI = ' + str(w) + ' Human = ' + str(b)
    chart_1.create_text(150, 450, text=txt, fill='white')
    txt = 'total score : AI = ' + str(ww) + ' Human = ' + str(bb)
    chart_1.create_text(150, 470, text=txt, fill='white')

    chart_1.update()
    chart_1.after(20)

    chart_1.delete(ALL)
root.mainloop()

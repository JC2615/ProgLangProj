
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CARAT MINUS NUMBER PLUS SIGN VARIABLEexpr : term2 term1 term0term2 : SIGN NUMBER VARIABLE CARAT NUMBERterm1a : CARAT NUMBER\n            | emptyterm1 : SIGN NUMBER VARIABLE term1aterm0a : VARIABLE CARAT NUMBER\n            | empty term0 : SIGN NUMBER term0aempty :'
    
_lr_action_items = {'SIGN':([0,2,4,12,17,19,20,22,],[3,5,8,-9,-5,-4,-2,-3,]),'$end':([1,7,11,14,16,23,],[0,-1,-9,-8,-7,-6,]),'NUMBER':([3,5,8,13,18,21,],[6,9,11,20,22,23,]),'VARIABLE':([6,9,11,],[10,12,15,]),'CARAT':([10,12,15,],[13,18,21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,],[1,]),'term2':([0,],[2,]),'term1':([2,],[4,]),'term0':([4,],[7,]),'term0a':([11,],[14,]),'empty':([11,12,],[16,19,]),'term1a':([12,],[17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> term2 term1 term0','expr',3,'p_expr','project.py',80),
  ('term2 -> SIGN NUMBER VARIABLE CARAT NUMBER','term2',5,'p_expr_term2','project.py',85),
  ('term1a -> CARAT NUMBER','term1a',2,'p_expr_term1a','project.py',97),
  ('term1a -> empty','term1a',1,'p_expr_term1a','project.py',98),
  ('term1 -> SIGN NUMBER VARIABLE term1a','term1',4,'p_expr_term1','project.py',109),
  ('term0a -> VARIABLE CARAT NUMBER','term0a',3,'p_expr_term0a','project.py',122),
  ('term0a -> empty','term0a',1,'p_expr_term0a','project.py',123),
  ('term0 -> SIGN NUMBER term0a','term0',3,'p_expr_term0','project.py',134),
  ('empty -> <empty>','empty',0,'p_empty','project.py',158),
]

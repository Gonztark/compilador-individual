
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEnonassocLTLTEGTGTENErightUMINUSASSIGN CALL COMMA COMMENT DIVIDE DO DOT ELSE EQ FOR FUNCTION GT GTE ID IF LBRACE LPARENT LT LTE MINUS NE NUMBER PLUS PRINT RBRACE READ RETURN RPARENT SEMICOLON STRING TIMES VAR WHILEprogram : program statement\n               | statementstatement : expression SEMICOLONstatement : VAR ID ASSIGN expression SEMICOLON\n                 | ID ASSIGN expression SEMICOLONstatement : FUNCTION ID LPARENT RPARENT block\n                 | FUNCTION ID LPARENT param_list RPARENT blockparam_list : param_list COMMA VAR ID\n                  | VAR IDstatement : IF LPARENT expression RPARENT block\n                 | IF LPARENT expression RPARENT block ELSE blockstatement : WHILE LPARENT expression RPARENT blockstatement : FOR LPARENT statement expression SEMICOLON statement RPARENT blockstatement : RETURN expression SEMICOLONblock : LBRACE statements RBRACE\n             | LBRACE RBRACEstatements : statements statement\n                  | statementexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : MINUS expression %prec UMINUSexpression : CALL ID LPARENT arguments RPARENTexpression : LPARENT expression RPARENTexpression : NUMBERexpression : IDexpression : expression LT expression\n                  | expression LTE expression\n                  | expression GT expression\n                  | expression GTE expression\n                  | expression NE expression\n                  | expression EQ expressionexpression : STRINGstatement : PRINT LPARENT print_arguments RPARENT SEMICOLONprint_arguments : print_arguments COMMA print_argument\n                       | print_argumentprint_argument : expression\n                      | STRINGstatement : CALL ID LPARENT arguments RPARENT SEMICOLONarguments : arguments COMMA expression\n                 | expression\n                 | emptyempty :'
    
_lr_action_items = {'VAR':([0,1,2,17,18,37,54,60,67,80,81,82,84,87,88,89,90,94,95,96,97,102,104,105,107,109,],[4,4,-2,-1,-3,4,70,-14,-5,-4,-6,4,98,-10,-12,4,-35,4,-16,-18,-7,-40,-15,-17,-11,-13,]),'ID':([0,1,2,4,6,7,11,13,14,17,18,19,20,21,22,23,24,25,26,27,28,30,33,35,36,37,39,52,59,60,65,67,70,71,76,80,81,82,87,88,89,90,93,94,95,96,97,98,102,104,105,107,109,],[5,5,-2,29,31,34,34,40,34,-1,-3,34,34,34,34,34,34,34,34,34,34,34,56,34,34,5,34,34,34,-14,34,-5,85,34,34,-4,-6,5,-10,-12,5,-35,34,5,-16,-18,-7,106,-40,-15,-17,-11,-13,]),'FUNCTION':([0,1,2,17,18,37,60,67,80,81,82,87,88,89,90,94,95,96,97,102,104,105,107,109,],[6,6,-2,-1,-3,6,-14,-5,-4,-6,6,-10,-12,6,-35,6,-16,-18,-7,-40,-15,-17,-11,-13,]),'IF':([0,1,2,17,18,37,60,67,80,81,82,87,88,89,90,94,95,96,97,102,104,105,107,109,],[8,8,-2,-1,-3,8,-14,-5,-4,-6,8,-10,-12,8,-35,8,-16,-18,-7,-40,-15,-17,-11,-13,]),'WHILE':([0,1,2,17,18,37,60,67,80,81,82,87,88,89,90,94,95,96,97,102,104,105,107,109,],[9,9,-2,-1,-3,9,-14,-5,-4,-6,9,-10,-12,9,-35,9,-16,-18,-7,-40,-15,-17,-11,-13,]),'FOR':([0,1,2,17,18,37,60,67,80,81,82,87,88,89,90,94,95,96,97,102,104,105,107,109,],[10,10,-2,-1,-3,10,-14,-5,-4,-6,10,-10,-12,10,-35,10,-16,-18,-7,-40,-15,-17,-11,-13,]),'RETURN':([0,1,2,17,18,37,60,67,80,81,82,87,88,89,90,94,95,96,97,102,104,105,107,109,],[11,11,-2,-1,-3,11,-14,-5,-4,-6,11,-10,-12,11,-35,11,-16,-18,-7,-40,-15,-17,-11,-13,]),'PRINT':([0,1,2,17,18,37,60,67,80,81,82,87,88,89,90,94,95,96,97,102,104,105,107,109,],[12,12,-2,-1,-3,12,-14,-5,-4,-6,12,-10,-12,12,-35,12,-16,-18,-7,-40,-15,-17,-11,-13,]),'CALL':([0,1,2,7,11,14,17,18,19,20,21,22,23,24,25,26,27,28,30,35,36,37,39,52,59,60,65,67,71,76,80,81,82,87,88,89,90,93,94,95,96,97,102,104,105,107,109,],[13,13,-2,33,33,33,-1,-3,33,33,33,33,33,33,33,33,33,33,33,33,33,13,33,33,33,-14,33,-5,33,33,-4,-6,13,-10,-12,13,-35,33,13,-16,-18,-7,-40,-15,-17,-11,-13,]),'MINUS':([0,1,2,3,5,7,11,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,32,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,55,57,58,59,60,63,64,65,66,67,71,74,76,78,80,81,82,87,88,89,90,92,93,94,95,96,97,99,102,103,104,105,107,109,],[14,14,-2,20,-27,14,14,14,-26,-34,-1,-3,14,14,14,14,14,14,14,14,14,14,14,20,-27,14,14,14,20,14,-23,-19,-20,-21,-22,-28,-29,-30,-31,-32,20,14,20,-25,20,20,14,-14,20,-34,14,20,-5,14,20,14,20,-4,-6,14,-10,-12,14,-35,-24,14,14,-16,-18,-7,-24,-40,20,-15,-17,-11,-13,]),'LPARENT':([0,1,2,7,8,9,10,11,12,14,17,18,19,20,21,22,23,24,25,26,27,28,30,31,35,36,37,39,40,52,56,59,60,65,67,71,76,80,81,82,87,88,89,90,93,94,95,96,97,102,104,105,107,109,],[7,7,-2,7,35,36,37,7,39,7,-1,-3,7,7,7,7,7,7,7,7,7,7,7,54,7,7,7,7,65,7,71,7,-14,7,-5,7,7,-4,-6,7,-10,-12,7,-35,7,7,-16,-18,-7,-40,-15,-17,-11,-13,]),'NUMBER':([0,1,2,7,11,14,17,18,19,20,21,22,23,24,25,26,27,28,30,35,36,37,39,52,59,60,65,67,71,76,80,81,82,87,88,89,90,93,94,95,96,97,102,104,105,107,109,],[15,15,-2,15,15,15,-1,-3,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-14,15,-5,15,15,-4,-6,15,-10,-12,15,-35,15,15,-16,-18,-7,-40,-15,-17,-11,-13,]),'STRING':([0,1,2,7,11,14,17,18,19,20,21,22,23,24,25,26,27,28,30,35,36,37,39,52,59,60,65,67,71,76,80,81,82,87,88,89,90,93,94,95,96,97,102,104,105,107,109,],[16,16,-2,16,16,16,-1,-3,16,16,16,16,16,16,16,16,16,16,16,16,16,16,64,16,16,-14,16,-5,16,64,-4,-6,16,-10,-12,16,-35,16,16,-16,-18,-7,-40,-15,-17,-11,-13,]),'$end':([1,2,17,18,60,67,80,81,87,88,90,95,97,102,104,107,109,],[0,-2,-1,-3,-14,-5,-4,-6,-10,-12,-35,-16,-7,-40,-15,-11,-13,]),'SEMICOLON':([3,5,15,16,34,38,41,42,43,44,45,46,47,48,49,50,51,53,55,66,74,75,92,99,],[18,-27,-26,-34,-27,60,-23,-19,-20,-21,-22,-28,-29,-30,-31,-32,-33,67,-25,80,89,90,102,-24,]),'PLUS':([3,5,15,16,32,34,38,41,42,43,44,45,46,47,48,49,50,51,53,55,57,58,63,64,66,74,78,92,99,103,],[19,-27,-26,-34,19,-27,19,-23,-19,-20,-21,-22,-28,-29,-30,-31,-32,19,19,-25,19,19,19,-34,19,19,19,-24,-24,19,]),'TIMES':([3,5,15,16,32,34,38,41,42,43,44,45,46,47,48,49,50,51,53,55,57,58,63,64,66,74,78,92,99,103,],[21,-27,-26,-34,21,-27,21,-23,21,21,-21,-22,-28,-29,-30,-31,-32,21,21,-25,21,21,21,-34,21,21,21,-24,-24,21,]),'DIVIDE':([3,5,15,16,32,34,38,41,42,43,44,45,46,47,48,49,50,51,53,55,57,58,63,64,66,74,78,92,99,103,],[22,-27,-26,-34,22,-27,22,-23,22,22,-21,-22,-28,-29,-30,-31,-32,22,22,-25,22,22,22,-34,22,22,22,-24,-24,22,]),'LT':([3,5,15,16,32,34,38,41,42,43,44,45,46,47,48,49,50,51,53,55,57,58,63,64,66,74,78,92,99,103,],[23,-27,-26,-34,23,-27,23,-23,23,23,23,23,None,None,None,None,None,23,23,-25,23,23,23,-34,23,23,23,-24,-24,23,]),'LTE':([3,5,15,16,32,34,38,41,42,43,44,45,46,47,48,49,50,51,53,55,57,58,63,64,66,74,78,92,99,103,],[24,-27,-26,-34,24,-27,24,-23,24,24,24,24,None,None,None,None,None,24,24,-25,24,24,24,-34,24,24,24,-24,-24,24,]),'GT':([3,5,15,16,32,34,38,41,42,43,44,45,46,47,48,49,50,51,53,55,57,58,63,64,66,74,78,92,99,103,],[25,-27,-26,-34,25,-27,25,-23,25,25,25,25,None,None,None,None,None,25,25,-25,25,25,25,-34,25,25,25,-24,-24,25,]),'GTE':([3,5,15,16,32,34,38,41,42,43,44,45,46,47,48,49,50,51,53,55,57,58,63,64,66,74,78,92,99,103,],[26,-27,-26,-34,26,-27,26,-23,26,26,26,26,None,None,None,None,None,26,26,-25,26,26,26,-34,26,26,26,-24,-24,26,]),'NE':([3,5,15,16,32,34,38,41,42,43,44,45,46,47,48,49,50,51,53,55,57,58,63,64,66,74,78,92,99,103,],[27,-27,-26,-34,27,-27,27,-23,27,27,27,27,None,None,None,None,None,27,27,-25,27,27,27,-34,27,27,27,-24,-24,27,]),'EQ':([3,5,15,16,32,34,38,41,42,43,44,45,46,47,48,49,50,51,53,55,57,58,63,64,66,74,78,92,99,103,],[28,-27,-26,-34,28,-27,28,-23,-19,-20,-21,-22,-28,-29,-30,-31,-32,28,28,-25,28,28,28,-34,28,28,28,-24,-24,28,]),'ASSIGN':([5,29,],[30,52,]),'RPARENT':([15,16,18,32,34,41,42,43,44,45,46,47,48,49,50,51,54,55,57,58,60,61,62,63,64,65,67,69,71,77,78,79,80,81,85,86,87,88,90,91,95,97,99,101,102,103,104,106,107,109,],[-26,-34,-3,55,-27,-23,-19,-20,-21,-22,-28,-29,-30,-31,-32,-33,68,-25,72,73,-14,75,-37,-38,-34,-44,-5,83,-44,92,-42,-43,-4,-6,-9,99,-10,-12,-35,-36,-16,-7,-24,108,-40,-41,-15,-8,-11,-13,]),'COMMA':([15,16,34,41,42,43,44,45,46,47,48,49,50,51,55,61,62,63,64,65,69,71,77,78,79,85,86,91,99,103,106,],[-26,-34,-27,-23,-19,-20,-21,-22,-28,-29,-30,-31,-32,-33,-25,76,-37,-38,-34,-44,84,-44,93,-42,-43,-9,93,-36,-24,-41,-8,]),'RBRACE':([18,60,67,80,81,82,87,88,90,94,95,96,97,102,104,105,107,109,],[-3,-14,-5,-4,-6,95,-10,-12,-35,104,-16,-18,-7,-40,-15,-17,-11,-13,]),'LBRACE':([68,72,73,83,100,108,],[82,82,82,82,82,82,]),'ELSE':([87,95,104,],[100,-16,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,1,37,82,89,94,],[2,17,59,96,101,105,]),'expression':([0,1,7,11,14,19,20,21,22,23,24,25,26,27,28,30,35,36,37,39,52,59,65,71,76,82,89,93,94,],[3,3,32,38,41,42,43,44,45,46,47,48,49,50,51,53,57,58,3,63,66,74,78,78,63,3,3,103,3,]),'print_arguments':([39,],[61,]),'print_argument':([39,76,],[62,91,]),'param_list':([54,],[69,]),'arguments':([65,71,],[77,86,]),'empty':([65,71,],[79,79,]),'block':([68,72,73,83,100,108,],[81,87,88,97,107,109,]),'statements':([82,],[94,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program statement','program',2,'p_program','sintactico.py',20),
  ('program -> statement','program',1,'p_program','sintactico.py',21),
  ('statement -> expression SEMICOLON','statement',2,'p_statement_expr','sintactico.py',28),
  ('statement -> VAR ID ASSIGN expression SEMICOLON','statement',5,'p_statement_assign','sintactico.py',32),
  ('statement -> ID ASSIGN expression SEMICOLON','statement',4,'p_statement_assign','sintactico.py',33),
  ('statement -> FUNCTION ID LPARENT RPARENT block','statement',5,'p_statement_function','sintactico.py',49),
  ('statement -> FUNCTION ID LPARENT param_list RPARENT block','statement',6,'p_statement_function','sintactico.py',50),
  ('param_list -> param_list COMMA VAR ID','param_list',4,'p_param_list','sintactico.py',65),
  ('param_list -> VAR ID','param_list',2,'p_param_list','sintactico.py',66),
  ('statement -> IF LPARENT expression RPARENT block','statement',5,'p_statement_if','sintactico.py',73),
  ('statement -> IF LPARENT expression RPARENT block ELSE block','statement',7,'p_statement_if','sintactico.py',74),
  ('statement -> WHILE LPARENT expression RPARENT block','statement',5,'p_statement_while','sintactico.py',81),
  ('statement -> FOR LPARENT statement expression SEMICOLON statement RPARENT block','statement',8,'p_statement_for','sintactico.py',85),
  ('statement -> RETURN expression SEMICOLON','statement',3,'p_statement_return','sintactico.py',89),
  ('block -> LBRACE statements RBRACE','block',3,'p_block','sintactico.py',93),
  ('block -> LBRACE RBRACE','block',2,'p_block','sintactico.py',94),
  ('statements -> statements statement','statements',2,'p_statements','sintactico.py',101),
  ('statements -> statement','statements',1,'p_statements','sintactico.py',102),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','sintactico.py',109),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','sintactico.py',110),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','sintactico.py',111),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','sintactico.py',112),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','sintactico.py',154),
  ('expression -> CALL ID LPARENT arguments RPARENT','expression',5,'p_expression_function_call','sintactico.py',158),
  ('expression -> LPARENT expression RPARENT','expression',3,'p_expression_group','sintactico.py',184),
  ('expression -> NUMBER','expression',1,'p_expression_number','sintactico.py',188),
  ('expression -> ID','expression',1,'p_expression_name','sintactico.py',192),
  ('expression -> expression LT expression','expression',3,'p_expression_comparison','sintactico.py',206),
  ('expression -> expression LTE expression','expression',3,'p_expression_comparison','sintactico.py',207),
  ('expression -> expression GT expression','expression',3,'p_expression_comparison','sintactico.py',208),
  ('expression -> expression GTE expression','expression',3,'p_expression_comparison','sintactico.py',209),
  ('expression -> expression NE expression','expression',3,'p_expression_comparison','sintactico.py',210),
  ('expression -> expression EQ expression','expression',3,'p_expression_comparison','sintactico.py',211),
  ('expression -> STRING','expression',1,'p_expression_string','sintactico.py',233),
  ('statement -> PRINT LPARENT print_arguments RPARENT SEMICOLON','statement',5,'p_statement_print','sintactico.py',237),
  ('print_arguments -> print_arguments COMMA print_argument','print_arguments',3,'p_print_arguments','sintactico.py',241),
  ('print_arguments -> print_argument','print_arguments',1,'p_print_arguments','sintactico.py',242),
  ('print_argument -> expression','print_argument',1,'p_print_argument','sintactico.py',249),
  ('print_argument -> STRING','print_argument',1,'p_print_argument','sintactico.py',250),
  ('statement -> CALL ID LPARENT arguments RPARENT SEMICOLON','statement',6,'p_statement_summon','sintactico.py',254),
  ('arguments -> arguments COMMA expression','arguments',3,'p_arguments','sintactico.py',277),
  ('arguments -> expression','arguments',1,'p_arguments','sintactico.py',278),
  ('arguments -> empty','arguments',1,'p_arguments','sintactico.py',279),
  ('empty -> <empty>','empty',0,'p_empty','sintactico.py',290),
]

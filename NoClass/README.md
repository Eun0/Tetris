# TETRIS

A simple tetris

you can set the size of board by changing cols and rows in tetris.py


[Reference url](https://gamedevelopment.tutsplus.com/tutorials/implementing-tetris-collision-detection--gamedev-852)

[한국어 버전](https://m.blog.naver.com/PostView.nhn?blogId=prt1004dms&logNo=221330860116&navType=tl)

function
 - Random tetromino
 - Falling tetromino
 - moving tetromino by key
 - rotate tetromino
 - Check line
 - Gameover
 - Different color (falling and landed)
 
## Basic concept

- Board is 2-D arrray
- board's element: '1' means occupied, '0' means unoccupied
- falling tetromino don't occupy parts of board 
 
  (it takes parts of board only if it landed)

## Composition

**1. Shape class**

   **attribute : num, leftTop, potLeftTop, rotation**
  
   - num : it will decied shape of tetromino
   
   - leftTop : tetromino's left and top coordinates
   
   - pot_leftTop : potential left and top coordinates, we use it when tetromino is falling
   
   - rotation : decide whether rotate or not
   
   - pot_shape : potential shape, we use it when tetromino rotates
    
    
   **method : rotate()**
    
   - rotate() : rotate tetromino! return pot_shape
    
    
**2. Tetris.py**

   **(1) Variables**
  
   &nbsp; \* means necessary; otherwise optional 
  
   &nbsp; \* cols : board's width (not length, but just size!)
  
   &nbsp; \* rows : board's height (not length, but jus size!)
  
   &nbsp; \* side : one block's side
    
   &nbsp;&nbsp;&nbsp;&nbsp; \- it is related to size of the image whose name is outside.png
  
   &nbsp; \* board : playing board
  
   &nbsp; shapes : array for holding tetrominos (set empty at first)
  
   &nbsp; i : index of shapes (set -1 at first)
   &nbsp;&nbsp;&nbsp;&nbsp; \- if tetromino is created then i++)
  
   &nbsp; \* gamestate : if gamestate is False, display 'gameover' (set True at first)
  
   &nbsp; \* collision: determine whether tetromino is landed or not (set True at first)
      
   &nbsp;&nbsp;&nbsp;&nbsp; \- if True, then create a new next tetromino)
      
   &nbsp; where : decide from which row to land (just before gameover)
   ![image](https://user-images.githubusercontent.com/33515697/43517974-73f15366-95c5-11e8-91f5-91929b2cee82.png)
      
   we need to slice! Use 'where' variable
      
      
   **(2) Functions**
   
   &nbsp; \* draw(x, y, color) : draw a block on (x,y) with color
      
   &nbsp; \* draw_tet(tetromino) : draw a tetromino
      
   &nbsp; \* draw_board(board) : draw the playing board
      
   &nbsp; \* line_check(board) : check board's row 
      
   &nbsp;&nbsp;&nbsp;&nbsp; \- if all elements are occupied, clear the line
      
   &nbsp; \* taken_check(tetromino,board) : check whether board's element is taken or not before moving
      
   &nbsp; \* falling(tet,board,where)-->safe : falling a tetromino
      
   &nbsp;&nbsp;&nbsp;&nbsp; \- if safe is False, land tetromino!
      
   &nbsp; \* land(tetromino,board) : land tetromino on board
      
 
## Sample

![sample](https://user-images.githubusercontent.com/33515697/43639939-e771f4b4-9758-11e8-8af0-a8fba4a358a3.gif)


      
      
      
      
    
  
  



import pygame
import firstShape
import random
import copy


# 경계 있는 정사각형 그리기 (block)
def draw(x,y,color):
	# outside.png 크기 20*20 
	solid=pygame.image.load("outside.png").convert()
	solid.fill(color,(1,1,18,18))
	screen.blit(solid,(x,y))


# 가로 줄 체크
# 다 찼으면 그 줄 지운다
def line_check(board):

	for row in range(len(board)):
		checker=0
		for col in range(len(board[row])):
			checker+=board[row][col]
			
			# 칸이 채워져있으면 1이다. 
			# 한 줄 다 채워져 있으면
			# => checker == cols
			if checker==len(board[0]):
				
				# 그 줄 없애고
				board.pop(row)

				# 맨 위에 새로 빈 row 삽입
				board.insert(0,[0 for col in range(len(board[0]))])


# (키 눌렀을 때) 움직일 칸 채워져 있는 지 '체크' 
# 채워졌으면 움직일 수 없다(taken=True). taken 리턴 
# 경계 넘어가는 것도 채워졌다고 하겠다.
# 움직이기 전 미리 확인하는 것이므로, pot_(potential) 이용
def taken(tetromino,board):

	taken=False

	for row in range(len(tetromino.pot_shape)):
		for col in range(len(tetromino.pot_shape[row])):
			if tetromino.pot_shape[row][col]!=0:
				# 왼쪽 경계 넘어가는 경우
				if col+tetromino.pot_leftTop[1]<0:
					taken=True
					break
				# 오른쪽 경계 넘어가는 경우
				elif col+tetromino.pot_leftTop[1]>=len(board[0]):
					taken=True
					break
				# 바닥 경계
				elif row+tetromino.pot_leftTop[0]>=len(board):
					taken=True
					break
				# 게임판 이미 채워진 경우
				elif board[row+tetromino.pot_leftTop[0]][col+tetromino.pot_leftTop[1]]:
					taken=True
					break

	return taken


# tet 떨어뜨리기
# safe가 False면 안착. 땅에 닿은 경우도 safe=False
# where은 안착할 위치,즉 닿은 곳 세로 어디까지 찼는 지 알려주는 변수 
# safe,where 리턴
def falling(tet,board,where):

	safe=True	

	# potential 움직일 위치
	tet.pot_leftTop[0]=tet.leftTop[0]+1
	tet.pot_leftTop[1]=tet.leftTop[1]
	
	# 땅에 닿았을 때
	if len(tet.shape)+tet.leftTop[0]>=len(board):
		safe=False
	else:
		for row in range(len(tet.shape)):
			for col in range(len(tet.shape[row])):
				if tet.shape[row][col]!=0:
					if board[row+tet.pot_leftTop[0]][col+tet.pot_leftTop[1]]!=0:
						# 안착 할 위치
						if where!=0:
							where=row+tet.pot_leftTop[0]-1
							
						safe=False

		
	return safe,where


# tetromino 그리기
def draw_tet(tetromino):

	color=(30,80,10)	

	for row in range(len(tetromino.shape)):
		for col in range(len(tetromino.shape[row])):
			if tetromino.shape[row][col]!=0:
				# block 한 변의 길이 * block 위치 + 시작 위치
				x=20*(col+tetromino.leftTop[1])+50
				y=20*(row+tetromino.leftTop[0])+50
				# block 그리기
				draw(x,y,color)


# 게임판 그리기
def draw_board(board):
	solid_color=(70,70,70)

	# 경계선 그리기 (시작 위치 (50,50) 으로 함)
	pygame.draw.rect(screen,color,(50,50,side*len(board[0]),side*len(board)),1)

	# 게임판 채워진 거 그리기
	for row in range(len(board)):
		for col in range(len(board[row])):
			if board[row][col]!=0:
				x=20*col+50
				y=20*row+50
				draw(x,y,solid_color)


# tetromino board에 안착하기
def land(tetromino,board):

	for row in range(len(tetromino.shape)):
		for col in range(len(tetromino.shape[row])):
			if tetromino.shape[row][col]!=0:
				board[row+tetromino.leftTop[0]][col+tetromino.leftTop[1]]=tetromino.shape[row][col]

																			

# 가로
cols=10
# 세로
rows=16
# 한 변의 길이(outside.png)
side=20


# 게임판 0으로 초기화 (0: 비었다, 1: 채워졌다)
board=[[0 for col in range(cols)] for row in range(rows)]


# tetromino(테트리스 모양) 담아둘 배열
shapes=[]
# shapes 인덱스 용
i=-1

# 기본 세팅
finish=False
color=(255,255,200)
clock=pygame.time.Clock()
gamestate=True
collision=True
# tetromino가 안착할 y 위치
where=1


#스크린 초기화
width=300
height=400

pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('TETRIS')


# 이벤트 루프
while not finish:
	screen.fill(0)


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			finish=True


	# 게임 진행중
	if gamestate:

		# 게임판 그리기
		draw_board(board)

		# 줄 체크
		line_check(board)

		# collision이 True인 경우 (1. 첫 시작,2. land해서 다음 tetromino 필요)
		if collision:
			# tetromino 생성
			tetromino=firstShape.Shape(random.randint(1,5),[0,5])
			shapes.append(tetromino)
			#인덱스 증가
			i+=1
			# 새로 만들었으니 collision 다시 False로
			collision=False

			

			
		if not collision:

			# 키 눌렀을 때
			pressed=pygame.key.get_pressed()
			
			# 윗 방향키 => 회전
			if pressed[pygame.K_UP]: 

				# 회전했다고 가정
				pot_tet=shapes[i].rotate()

				# 회전한 모양이 경계 넘어갈 수도 있음
				# kick 변수로 확인
				# kick = 현재 가로 위치+ 회전한 모양의 가로 길이
				kick=shapes[i].leftTop[1]+len(pot_tet[0])

				# kick이 게임판 가로보다 길다.
				# => 경계 넘어감
				if kick>cols:


					# out = 얼만큼 넘어갔는 지
					out=kick-cols

					# 넘어간 만큼 현재 위치에서 빼준 것을 pot_leftTop에 넣는다.
					# 객체 생성 시 pot_leftTop leftTop으로 초기화되므로
					# pot_leftTop에서 out 바로 빼도 된다.
					shapes[i].pot_leftTop[1]-=out

				# potential 위치에 차지하고 있는 칸이 없다면
				if not taken(shapes[i],board):

					# 현재 모양 회전한 모양으로 바꾼다.				
					shapes[i].shape=pot_tet
					shapes[i].leftTop=copy.deepcopy(shapes[i].pot_leftTop)
				
				

			if pressed[pygame.K_DOWN]: 
				# potential 설정
				shapes[i].pot_leftTop[0]=shapes[i].leftTop[0]+1
				shapes[i].pot_leftTop[1]=shapes[i].leftTop[1]
				# potential 위치에 차지하고 있는 칸이 없다면
				if not taken(shapes[i],board):
					shapes[i].leftTop=copy.deepcopy(shapes[i].pot_leftTop)
				
			if pressed[pygame.K_LEFT]:
				# potential 설정
				shapes[i].pot_leftTop[0]=shapes[i].leftTop[0]
				shapes[i].pot_leftTop[1]=shapes[i].leftTop[1]-1
				# potential 위치에 차지하고 있는 칸이 없다면
				if not taken(shapes[i],board):
					shapes[i].leftTop=copy.deepcopy(shapes[i].pot_leftTop)

			if pressed[pygame.K_RIGHT]:
				# potential 설정 
				shapes[i].pot_leftTop[0]=shapes[i].leftTop[0]
				shapes[i].pot_leftTop[1]=shapes[i].leftTop[1]+1
				# potential 위치에 차지하고 있는 칸이 없다면
				if not taken(shapes[i],board):
					shapes[i].leftTop=copy.deepcopy(shapes[i].pot_leftTop)

			# 매 루프마다 tetromino 한 칸씩 떨어진다. 
			# 떨어질 수 없다면 safe=False,where=그 때의 y위치 
			safe,where=falling(shapes[i],board,where)

								
							
		# 떨어질 수 있다면 
		if safe:
			# potential이 실제 leftTop이 된다.
			shapes[i].leftTop[0]=shapes[i].pot_leftTop[0]


		# 떨어질 수 없다면
		if not safe:

			# 경계를 넘어서 떨어질 수 없는 경우 
			# => 원래 tetromino 경계에 맞게 짜르고 land한 후 gameover  
			if shapes[i].leftTop[0]==0:
			
				where=len(shapes[i].shape)-where-1
			
				shapes[i].shape=shapes[i].shape[where:]

				land(shapes[i],board)
				gamestate=False
		
			# 경계 넘지 않는 경우 바로 land
			# => 새로운 tetromino 필요하므로 collision=True
			else:
				land(shapes[i],board)
				
				collision=True
		
		# tetromino 그리기
		draw_tet(shapes[i])	
	

				
	# 게임 끝나면			
	if not gamestate:

		font=pygame.font.Font(None,50)
		text=font.render("GAME OVER",1,color)
		text_rect=text.get_rect()
		text_rect.center=(150,150)
		screen.blit(text,text_rect)



	pygame.display.flip()
	clock.tick(7)	

		
		

		




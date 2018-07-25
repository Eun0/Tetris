class Shape:

	def __init__(self,num,leftTop):

		# 정사각형 
		if num==1:
			self.shape=[[1,1]
					   ,[1,1]]
		# 'L' 			   
		elif num==2:
			self.shape=[[1,1]
			           ,[0,1]
			           ,[0,1]]
		# 'l'
		elif num==3:
			self.shape=[[1]
					   ,[1]
					   ,[1]
					   ,[1]]
		# 'Z' 			   
		elif num==4:
			self.shape=[[1,1,0]
			           ,[0,1,1]]
		# 'ㅗ' 			   
		elif num==5:
			self.shape=[[0,1,0]
			           ,[1,1,1]]

		#위치
		self.leftTop=leftTop
		self.potLeftTop=[self.leftTop[0],self.leftTop[1]]

	
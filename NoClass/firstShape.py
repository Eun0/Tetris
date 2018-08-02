class Shape:

	def __init__(self,num,leftTop):

		self.rotation=0

		self.num=num

		# 정사각형 
		if self.num==1:

			self.shape=[[1,1]
					   ,[1,1]]
		# 'L' 			   
		elif self.num==2:

			self.shape=[[1,1]
			           ,[0,1]
			           ,[0,1]]

		# 'l'
		elif self.num==3:

			self.shape=[[1]
					   ,[1]
					   ,[1]
					   ,[1]]



		# 'Z' 			   
		elif self.num==4:

			self.shape=[[1,1,0]
			           ,[0,1,1]]

	

		# 'ㅗ' 			   
		elif self.num==5:
			
			self.shape=[[0,1,0]
			           ,[1,1,1]]
			
						   
		#위치
		self.leftTop=leftTop
		self.potLeftTop=[self.leftTop[0],self.leftTop[1]]



	def rotate(self):

		self.rotation+=1
		# 정사각형 
		if self.num==1:

			self.shape=[[1,1]
					   ,[1,1]]
		# 'L' 			   
		elif self.num==2:

			if self.rotation%3==0:
				self.shape=[[1,1]
				           ,[0,1]
				           ,[0,1]]

			elif self.rotation%3==1:
				self.shape=[[0,0,1]
						   ,[1,1,1]]

			elif self.rotation%3==2:
				self.shape=[[1,0]
						   ,[1,0]
						   ,[1,1]]
		# 'l'
		elif self.num==3:

			if self.rotation%2==0:
				self.shape=[[1]
						   ,[1]
						   ,[1]
						   ,[1]]

			elif self.rotation%2==1:
				self.shape=[[1,1,1,1]]

		# 'Z' 			   
		elif self.num==4:

			if self.rotation%2==0:
				self.shape=[[1,1,0]
				           ,[0,1,1]]

			elif self.rotation%2==1:
				self.shape=[[0,1]
				           ,[1,1]
				           ,[1,0]]

		# 'ㅗ' 			   
		elif self.num==5:
			if self.rotation%4==0:
				self.shape=[[0,1,0]
				           ,[1,1,1]]
			elif self.rotation%4==1:
				self.shape=[[1,0]
						   ,[1,1]
						   ,[1,0]]
			elif self.rotation%4==2:
				self.shape=[[1,1,1]
						   ,[0,1,0]]
			elif self.rotation%4==3:
				self.shape=[[0,1]
				           ,[1,1]
				           ,[0,1]]


	
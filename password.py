#密碼重試程式
x = 0
while x < 3:
	x = x + 1
	password = input('請輸入密碼:')
	if password == 'a123456':
		print('登入成功!') 
		break
	elif password != 'a123456' and x < 3:
		print('密碼錯誤！還有', 3-x, '次機會')
	elif x == 3 :
		print('登入失敗!!')
		break

	
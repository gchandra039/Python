# 
e=4

def click(to_print):
	old=e
	e.delete(0, END)
	e.insert(0, old+to_print)
	return

click('3')
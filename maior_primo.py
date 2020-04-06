def maior_primo (x):
	while (x > 0):	
		if (verifica_primo(x) == x):
			return x
		x = x - 1


def verifica_primo(x):
	cont = 0
	y = x
	while (x != 0):
		if(y % x == 0):
			cont = cont + 1
		x = x - 1
	if (cont == 2):
		return y
	cont = 0	
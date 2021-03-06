#-*- encoding: utf-8 -*-
__author__ = "Eduardo Orige"
__credits__ = ["Eduardo Orige"]
__version__ = "0.01 beta"
__maintainer__ = "Eduardo Orige"
__email__ = "eduardo.orige@gmail.com"
__status__ = "Em Producao"

class Operadora:
	"""
	Classe com todos os métodos utilizados para validar um ddd, verificar um número de celular
	e verificar a operadora.
	"""
	def __init__(self):

		"""
		Initializer da Classe Operadora. Aqui uma lista de todos os regexp para
		verificação de ddd's.
		"""
		self.tests = [
			'(11)|((1)[1-9]$)', #11 a 19 - SP
			'(21)|((2)[1-8]$)', #21 a 28 - RJ, ES
			'(31)|((3)[1-8]$)', #31 a 38 - MG
			'(41)|((4)[1-9]$)', #41 a 49 - PR, SC
			'(51)|((5)[1-5]$)', #51 a 55 - RS
			'(61)|((6)[1-9]$)', #61 a 69 - Centro Oeste
			'(71)|((7)[1-9]$)', #71 a 79 - BA,SE
			'(81)|((8)[1-9]$)', #81 a 89 - Nordeste
			'(91)|((9)[1-9]$)', #91 a 99 - AM
		]
		
	def operadoras(self):
		"""
		Mostra as operadoras que estão disponiveis para analise no sistema.
		"""
		operadoras_disponiveis = ['Claro','CTBC','Oi','Sercomtel','TIM','Vivo',]
									
		return sorted(operadoras_disponiveis)

	def re_ddd(self,ddd):
		"""
		Função que monta todos os regexp da lista self.tests e verifica se o ddd
		passado por parametro é um ddd valido.
		"""
		import re
		for test in self.tests:
			if re.compile(str(test)).match(str(ddd)):
				return True


	def re_celular(self,celular):
		"""
		Função que verifica se o celular passado corresponde ao padrão solicitado
		e se o número tambem é valido.
		Ex: 99 9999-9999
		"""
		import re
		test = re.compile('([1-9][1-9]\s[6-9]\d{3}\-\d{4}$)')
		if test.match(celular):
			return True
		else:
			return False

	def operadora(self,celular):
		"""
		Os calculos e o modelo de calculo usados estao em http://www.simmtelecom.com.br/telecom/comeco-dos-numeros-dos-celulares-no-estados-por-operadora/
		Prints tambem no diretorio img do repositorio.
		
		Verifica corretamente seguindo o padrao anterior de numero de celular: 99 9999-9999
		Se padrão nao for seguido, função retorna False.
		
		Primeiro verifica-se as exceções dos prefixos com 4 digitos depois então verifica-se 
		os numeros "padroes".
		"""		
		ddd = int(celular[:2])
		cel = int(celular[3:5])
		pre_cel = int(celular[3:7])
		#---- SP -----#
		if 11 <= ddd <= 19:
			if 6340 <= pre_cel <= 6369:
				return "TIM"
			
			elif (	6310 <= pre_cel <= 6339 or
					6589 <= pre_cel <= 6599 or
					7052 <= pre_cel <= 7062 or
					cel == 76 			or
					8800 <= pre_cel <= 8899 or
					cel == 89			):
				return "CLARO"
			
			elif ( 	6057 <= pre_cel <= 6060 or
					6193 <= pre_cel <= 6199 or
					6370 <= pre_cel <= 6499 or
					pre_cel == 7099 or
					71 <= cel <= 75 or
					cel == 95 ):
				return "VIVO"
			
			elif (	6100 <= pre_cel <= 6193	or
					pre_cel == 6299 or
					cel == 65 or
					6651 <= pre_cel <= 6799 or
					cel == 68 or
					pre_cel == 6999 or
					7971 <= pre_cel <= 7999 or
					cel == 80 or
					8814 <= pre_cel <= 8899 ):
				return "OI"
				
			#elif cel == 99 onde a vivo nao esta: return CTBC
		
			else:	
				if 96 <= cel <= 99:
					return "VIVO"

				elif 91 <= cel <= 94:
					return "CLARO"

				elif 81 <= cel <= 87:
					return "TIM"

				#elif int(cel[0]) == 8 and int(cel[1]) != 1 or int(cel[1]) != 7:
				#TODO
				#Verificar isso. Tirar Novos Prints
				elif cel == 80 or cel == 88 or cel == 89:
					return "OI"
				else:
					return None

		#---- RJ, ES ----#
		elif 21 <= ddd <= 28:
			if 74 <= cel <= 76:
				return "CLARO"
			
			elif cel == 71 or cel == 72 or cel == 95:
				return "VIVO"			
			
			elif 84 <= cel <= 86 or 87 <= cel == 89:
				return "OI"
			
			elif 96 <= cel <= 99:
				return "VIVO"

			elif 91 <= cel <= 94:
				return "CLARO"


			elif 80 <= cel <= 83:
				return "TIM"

			else:
				return None

		#---- MG ----#
		elif 31 <= ddd <= 38:
			
			if cel == 85 or cel == 86 or cel == 89:
				return "OI"
			
			#elif cel == 96:
			#	return "CTBC"
			
			elif ( 	9960 <= pre_cel <= 9979 or 
					9991 <= pre_cel <= 9999 ):
				return "CTBC"
				
			elif 96 <= cel <= 99:
				print "VIVO"

			elif 91 <= cel <= 94:
				return "TIM"

			elif 87 <= cel <= 88:
				return "OI"

			elif 81 <= cel <= 84:
				return "CLARO"

			else:
				return None	

		#---- SC, PR ----#
		elif 41 <= ddd <= 49:
			if ddd == 43 and cel == 81:
				return "TIM"

			#TODO
			# Londrina e TAMARANA , PR
			#elif 9941 <= pre_cel <= 9998:
			#	return "SERCOMTEL"

			else:
				if 96 <= cel <= 99:
					return "TIM"

				elif 91 <= cel <= 94:
					return "VIVO"

				elif 87 <= cel <= 88:
					return "CLARO"

				elif 84 <= cel <= 85:
					return "OI"

				else:
					return None

		#---------- RS --------------#
		elif 51 <= ddd <= 55:
			
			#TODO
			#if 9911 <= pre_cel <= 9939: #SE FOR DE PELOTAS E REGIAO
			#	return "TIM"

			if 81 <= cel <= 82:
				return "TIM"

			elif 84 <= cel <= 85:
				return "OI"
				
			elif 91 <= cel <= 94:
				return "CLARO"
			
			elif 95 <= cel <= 99:
				return "VIVO"
		
			else:
				return None	 

		#---- Centro Oeste ---------#
		elif 61 <= ddd <= 69:
			if 9551 <= pre_cel <= 9559:
				return "CLARO"
			
			elif cel == 86:
				return "OI"
			
			#elif cel == 99 : onde nao existe vivo
			#return "CTBC"
			
			else:
				if 96 <= cel <= 99:
					return "VIVO"

				elif 91 <= cel <= 94:
					return "CLARO"

				elif 81 <= cel <= 82:
					return "TIM"

				elif 84 <= cel <= 85:
					return "OI"

				else:
					return None	

		#---------- BA, SE ----------#
		elif 71 <= ddd <= 79:
			if 81 <= cel <= 83:
				return "CLARO"

			elif 86 <= cel <= 88:
				return "OI"
			
			elif 91 <= cel <= 94:
				return "TIM"
					
			elif 96 <= cel <= 99:
				return "VIVO"

			else:
				return None
				
		#---------- Nordeste --------------#
		elif 81 <= ddd <= 89:
			
			if 8719 <= pre_cel <= 8721 or cel == 88:
				return "TIM"
			
			elif 8100 <= pre_cel <= 8200:
				return "VIVO"
			
			elif 84 <= cel <= 86:
				return "OI"
				
 			else:
				if 96 <= cel <= 99:
					return "TIM"

				elif 91 <= cel <= 94:
					return "CLARO"

				elif 87 <= cel <= 88:
					return "OI"

				elif 81 <= cel <= 83:
					return "VIVO"

				else:
					return None

		#---------- Norte --------------#
		elif 91 <= ddd <= 99:
			if 80 <= cel <= 83:
				return "OI"

			elif cel == 84:
				return "CLARO"

			elif 87 <= cel <= 88:
				return "OI"

			elif 91 <= cel <= 94:
				return "VIVO"

			elif 96 <= cel <= 99:
				return "AMAZONIA CELULAR"

			else:
				return None
		else:
			return False

	def ui(self):
		"""
		Parte grafica para teste em terminal.
		"""
		print "*****************************"
		print "*                           *"
		print "*   Qual é a Operadora ?    *"
		print "*                           *"
		print "*****************************"
		print
		print "Exemplo de numero: 99 9999-9999"
		celular = raw_input("Celular:")
		if self.re_celular(celular):
			if self.re_ddd(celular[:2]):
				operadora = self.operadora(celular)
				
				if operadora == None: 
					print "! Operadora não encontrada !"
				else: 
					print "Operadora: ", operadora
			else:
				print "! DDD Invalido !"
		else:
			print "! Número de Celular Inválido !"
				

if __name__ == '__main__':
	o = Operadora()
	o.ui()
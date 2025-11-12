#!/usr/bin/env python3
"""Verifica se um número inteiro positivo possui dois dígitos consecutivos iguais.

Entrada: um inteiro (pode ter sinal, mas consideramos apenas os dígitos).
Saída: "sim" se houver dois dígitos iguais consecutivos, caso contrário "não".

Exemplos:
  1223 -> sim
  1234 -> não
  11   -> sim
  5    -> não
"""

def possui_digitos_consecutivos_iguais(s: str) -> bool:
	"""Retorna True se a string de dígitos s contiver dois dígitos iguais consecutivos."""
	# percorre verificando pares adjacentes
	for i in range(len(s) - 1):
		if s[i] == s[i + 1]:
			return True
	return False


def main() -> None:
	try:
		raw = input().strip()
	except EOFError:
		# sem entrada
		return

	if not raw:
		# linha vazia -> sem saída
		return

	# remover sinal inicial caso exista
	if raw[0] in '+-':
		raw = raw[1:]

	# garantir que restaram apenas dígitos; se não, considerar apenas a parte inicial de dígitos
	# isto torna o programa mais tolerante a entradas como '00123' ou espaços extras
	digits = ''
	for ch in raw:
		if ch.isdigit():
			digits += ch
		else:
			break

	if len(digits) < 2:
		print("não")
		return

	if possui_digitos_consecutivos_iguais(digits):
		print("sim")
	else:
		print("não")


if __name__ == '__main__':
	main()


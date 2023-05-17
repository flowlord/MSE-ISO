#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	I) Bloc A
		Serie d'opération sur une chaine de caractère
		servant à modifier le text entré.
"""

from subdiv_mini import palm_2,palm_2_rev

def complexifier(plain_text):
	"""
		example:
			hello word ---> lrowd lleho
	"""

	plain_text =  plain_text[::-1]
	plain_text = palm_2(plain_text)
	plain_text = palm_2(plain_text)
	plain_text = palm_2(plain_text)

	return plain_text


def complexifier_inv(coded_text):
	""" 
		Remet le text dans le bon sens
		example:
			rowdl lehol ---> hello world
	"""

	coded_text = palm_2_rev(coded_text)
	coded_text = palm_2_rev(coded_text)
	coded_text = palm_2_rev(coded_text)
	coded_text =  coded_text[::-1]

	return coded_text


t = """
La Terre à très chaud. Les saisons ont changé, l’hiver est
devenu le printemps, le printemps est devenu l’été. L’été il fait encore plus
chaud, l’automne est comme le printemps mais avec du vent. Le niveau de la
mer a augmenter, grignotent petit à petit le littoral. Autrefois, petite je pouvais
courir sur des kilomètres de littoral, maintenant j’ai les pieds dans l’eau alors
que j’ai fait a peine quelques mètres, quel que sois la marrée.
La mer, avant était le premier lieu qui avait donner la vie, maintenant elle est
devenu un cimetière d’animaux marin rare, mort ou disparut. Les déchets les
remplacent. Les poissons devient rare, à tel point que leurs prix en flambées.
Manger du poisson est devenu un mets de luxe.
"""

e = """
Pour les pêcheurs le métier est
devenue difficile car pêcher du poisson est devenu de la loterie on peut passer
une journée sans rien avoir et si on en trouve on gagne le gros lot.
Certains pêcheur, sont reconverti en collecteur de déchets. Des bateaux parfois
d’ancien chalutier, transformé en collecteur de déchets. Les grand filet de de
poisson, ramassent maintenant des déchets. Une grue installé sur le bateau
ramasse les encombrants. Des déchets qui seront recyclés. Un nouveau marché
à été ouvert , celui des viandes artificielles. La viande de bœuf et de poisson
sont les plus populaires. Mais elle restent, parfois chère et avec un goût moyen.
Certains entreprise, n’hésitent pas à écrire « vraie viande de poisson », alors
que c’est de la viande artificielle, ce qui est interdit
"""


def cipher(text):
	phrases = complexifier(text)
	return phrases


print(cipher(t))







































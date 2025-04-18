##########################################
# BCODE - LICENSED UNDER THE MIT LICENSE #
##########################################
# Copyright (c) 2024 BubuCode
# See LICENSE file in root folder for full details.
##########################################

#####################################
# START THIS FILE TO USE BCODE 
#####################################
# TO RUN BCODE: RUN("example.bcode")
#####################################
# READ README.md for more information!
#####################################

import bcode

while True:
	text = input('bcode > ')
	if text.strip() == "": continue
	result, error = bcode.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
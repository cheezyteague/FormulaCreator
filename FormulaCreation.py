#! /usr/bin/env python3

# FILE: FormulaCreation.py
# AUTHOR: Canyon Bishop
# DATE: 05/05/2022
# DESCRIPTION: User defines number of charges needed, program creates a formula for use in caspio

hddict = {'1':'01','2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09','10':'0A','11':'0B','12':'0C','13':'0D','14':'0E','15':'0F','16':'10','17':'11','18':'12','19':'13','20':'14','21':'15','22':'16','23':'17','24':'18','25':'19','26':'1A','27':'1B','28':'1C','29':'1D','30':'1E','31':'1F','32':'20','33':'21','34':'22','35':'23','36':'24','37':'25','38':'26','39':'27','40':'28','41':'29','42':'2A','43':'2B','44':'2C','45':'2D','46':'2E','47':'2F','48':'30','49':'31','50':'32','51':'33','52':'34','53':'35','54':'36','55':'37','56':'38','57':'39','58':'3A','59':'3B','60':'3C','61':'3D','62':'3E','63':'3F','64':'40','65':'41','66':'42','67':'43','68':'44','69':'45','70':'46','71':'47','72':'48','73':'49','74':'4A','75':'4B','76':'4C','77':'4D','78':'4E','79':'4F'}

def createformula(formula):
	chargeslst = []
	while True:
		try:
			userNum = int(input("\n> Enter the Number of Charges in Decimal: "))
		except:
			print ("\nERROR: Invalid Input.\nPlease be sure to check your input.\n")
			exit()
		for i in hddict.keys():
			if int(userNum) < int(i):
				break
			elif int(userNum) > 79:
				print("\nThat number is too high, please choose a number below 80.\n")
				exit()
			else:
				hexn = hddict[i]
				fieldTemplate = ('[@field:Charge_%s]'% (hexn))
				chargeslst.append(fieldTemplate)
		formula = '+'.join(chargeslst)
		print ('\n'+formula+'\n')
		return formula
		chargeslst = []
		return False


def main():
	formula = ''
	createformula(formula)
	formula = ''
	quit()

if __name__ == "__main__":
	main()




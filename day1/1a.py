#This solution assumes that the list of calories is provided in a txt-file with the specified formatting. It presumes a default filename calorie_list.txt
#It can also handle a list containing the names of the elves, using the default filename "elf_names.txt". The progam conditionally outputs either the index
#																										 or name of the elf, depending on whether the provided
#																										 filename exists in the directory where the program is
#																										 called
#fname="calorie_list.txt"
import os

#
def findMaxElf(fname='calorie_list.txt',namefile = 'elf_names.txt'):
	intCalList = [0]
	f=open(fname)
	strCalList = f.readlines()
	N = len(strCalList)
	cwdir = os.getcwd()
	if os.path.exists(cwdir+'/'+namefile):
		f2 = open(cwdir+'/'+namefile)
		elf_names = [l.strip() for l in f2.readlines()]
	else:
		n=strCalList.count('\n')+1
		if n==1:
			totalcal = sum([int(l) for l in strCalList])
			return ['first elf',totalcal]
		elif n==2:
			elf_names = ['1st elf','2nd elf']
		else:
			elf_names = ['1st elf','2nd elf','3rd elf'] + ['{}th elf'.format(i) for i in range(4,n)]
	maxInd=0
	for l in strCalList:
		if l=='\n':
			if (len(intCalList) > 1 and intCalList[-1]>intCalList[maxInd]):
				maxInd = len(intCalList) -1
			intCalList += [0]
		else:
			intCalList[-1] += int(l)
	return [elf_names[maxInd],intCalList[maxInd]]

if __name__ == "__main__":
	print(findMaxElf())#enter alternative file names here, if applicable


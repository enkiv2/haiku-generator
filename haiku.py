#!/usr/bin/env python

import re, sys, random

r=random.Random()

vowel='[aeiouAEIOU]'
consonant='[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]'
syllable='('+consonant+'+'+vowel+'+'+consonant+'+|\s'+vowel+'+'+consonant+'+|'+consonant+'+'+vowel+'+\s|\s'+vowel+'+\s)'

syllableR = re.compile(syllable)

candidates=[]

for line in sys.stdin.readlines():
	x=re.findall(syllableR, line)
	if not (None == x) and len(x) > 0:
		if(len(x)==17):
			words=line.split()
			fine=True
			part=""
			for lc in [5, 6]:
				if(fine):
					for i in range(1, len(words)):
						chunk=" ".join(words[:i])
						count=len(re.findall(syllableR, chunk))
						if(count==lc):
							part=part+chunk+"\n"
							words=words[i:]
							break
						if(count>lc):
							fine=False
							break
			if(fine):
				candidates.append(part+(" ".join(words)))
if(len(candidates)<1):
	sys.exit(1)
print(r.choice(candidates))

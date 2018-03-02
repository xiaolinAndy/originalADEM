from models import *
from preprocess import Preprocessor
import sys
import time

saved_model = './weights/adem_model.pkl'
if __name__ == '__main__':
	time_start = time.time()
	pp = Preprocessor()
	adem = ADEM(pp, None, saved_model)

	contexts = ['</s> <first_speaker> hello . how are yours today ? </s>']
				#'</s> <first_speaker> i love starbucks coffee </s>',
				#'</s> <first_speaker> photo to see my television debut go to - some. some on- hehe! </s> <second_speaker> it really was you? i thought ppl were recognizing someone who looked like you! were the oysters worth the wait? </s>']
	true = ['</s> <second_speaker> i am fine . thanks </s>']
			#'</s> <second_speaker> i like their latte </s>',
			#"</s> <first_speaker> yeah it was me . haha i'd kinda forgotten about it it was filmed a while ago </s>"]
	model = ['</s> <second_speaker> i am fine . thanks </s>']
			#'</s> <second_speaker> I want to play golf . </s>',
			#"</s> <first_speaker> i'm not sure. i just don't know what to do with it. </s>"]

	print 'Model Loaded!'
	print adem.get_scores(contexts, true, model)

	time_end = time.time()
	print time_end - time_start



#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

try:
	from PIL import Image, ImageDraw, ImageOps
except ImportError:
	print 'Sisteminizde PIL yuklu degil lutfen yukleyiniz\npip install PIL'
	sys.exit()

class Banner:
	"""
	Sigarayi biraktiginiz tarihi ve ictiginiz sigara miktarini ogrenerek
	Her gun ne kadar kar ettiginizi gosteren uygulama...
	"""
	def __init__(self, days=0, cost=0, quantity=0, email=''):
		'''Sinifin alacagi parametreleri burada tanimliyoruz.'''
		self.days = days
		self.cost = cost
		self.quantity = quantity
		self.email = email

	def get_gravatar(self, email):
		'''
		Verilen email'e ait gravatar varsa onu getiriyoruz yoksa default bir resim getiriyoruz
		'''
		import urllib, hashlib
		# buraya duzgun bir resim koymali
		default = "http://www.gravatar.com/avatar/010f05028416c1402231e453d79433ba.png"
		size = 60
		gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(self.email.lower()).hexdigest() + "?"
		gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
		gravatar_image = urllib.urlretrieve(gravatar_url)
		gravatar_image = Image.open(gravatar_image[0])
		#burada gelen resmin arkaplani siyah, yani (0,0,0) donuyor. bunlari alip beyaza ceviriyoruz.
		datas = gravatar_image.getdata()
		newData = []
		for item in datas:
		    if item[0] == 0 and item[1] == 0 and item[2] == 0:
		        newData.append((255, 255, 255, 0))
		    else:
		        newData.append(item)
		gravatar_image.putdata(newData)
		return gravatar_image

	def banner(self):
		size = (400,60)
		color = (255,250,250)
		im = Image.new('RGB', size, color)
		draw = ImageDraw.Draw(im)
		blue = (135,206,250)
		black = (0,0,0)
		row1_pos = (70,5)
		#buraya duzgun bir metin koymali
		row1 = '%d gundur sigara icmiyorum..' %(self.days)
		row2_pos = (70,15)
		row2 = '%d sigara icmedim & %d TL kardayim' %(self.quantity, self.cost)
		footer = ''
		draw.text(row1_pos, row1, fill=blue)
		draw.text(row2_pos, row2, fill=blue)
		#umuthanin katkilariyla nosomike.png :D
		icon = Image.open("nosmoke.png")
		im.paste(icon, (0,0))
		gravatar = self.get_gravatar(self.email)
		im.paste(gravatar, (340,0))
		border = ImageOps.expand(im,border=2,fill=black)
		border.save('deneme.png')

if __name__ == '__main__':
	banner = Banner(email='rkirmizi@gmail.com')
	banner.banner()

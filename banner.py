from PIL import Image, ImageDraw, ImageOps

class Banner:
	"""Sigarayi biraktim banneri"""
	def __init__(self, days=0, cost=0, quantity=0, email=''):
		self.days = days
		self.cost = cost
		self.quantity = quantity
		self.email = email

	def get_gravatar(self, email):
		import urllib, hashlib
		# email = self.email
		default = "http://www.gravatar.com/avatar/010f05028416c1402231e453d79433ba.png"
		size = 40
		gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(self.email.lower()).hexdigest() + "?"
		gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
		gravatar_image = urllib.urlretrieve(gravatar_url)
		return gravatar_image[0]

	def banner(self):
		size = (400,60)
		color = (255,250,250)
		im = Image.new('RGB', size, color)
		draw = ImageDraw.Draw(im)
		blue = (135,206,250)
		black = (0,0,0)
		row1_pos = (70,5)
		row1 = "%d gundur sigara icmiyorum.." %(self.days)
		row2_pos = (70,15)
		row2 = "%d sigara icmedim & %d TL kardayim" %(self.quantity, self.cost)
		draw.text(row1_pos, row1, fill=blue)
		draw.text(row2_pos, row2, fill=blue)
		icon = Image.open("nosmoke.png")
		im.paste(icon, (0,0))
		gravatar = Image.open(self.get_gravatar(self.email))
		im.paste(gravatar, (320,0))
		border = ImageOps.expand(im,border=2,fill=black)

		border.show()


banner = Banner()
banner.banner()

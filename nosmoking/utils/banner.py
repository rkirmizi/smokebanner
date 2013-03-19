#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

try:
    from PIL import Image, ImageDraw, ImageOps
except ImportError:
    print 'Sisteminizde PIL yuklu degil lutfen yukleyiniz\npip install PIL'
    sys.exit()


class Banner:
    from datetime import datetime
    """
    Sigarayi biraktiginiz tarihi ve ictiginiz sigara miktarini ogrenerek
    Her gun ne kadar kar ettiginizi gosteren uygulama...
    """

    def __init__(self, first_name='', last_name='', email='',
                 quit_date=datetime.now(),
                 cost_per_package=0,
                 daily_quantity=0, first_row='',
                 second_row='', footer='',
                 output_dir='', output_file='', nosmoke_image=''):
        '''Sinifin alacagi parametreleri burada tanimliyoruz.'''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.quit_date = quit_date
        self.cost_per_package = cost_per_package
        self.daily_quantity = daily_quantity
        self.first_row = first_row
        self.second_row = second_row
        self.footer = footer
        self.output_dir = output_dir
        self.output_file = output_file
        self.nosmoke_image = nosmoke_image

    def get_gravatar(self, email):
        '''
        Verilen email'e ait gravatar varsa onu getiriyoruz yoksa default bir resim getiriyoruz
        '''
        import urllib
        import hashlib
        # buraya duzgun bir resim koymali
        default = "http://www.gravatar.com/avatar/010f05028416c1402231e453d79433ba.png"
        size = 60
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(self.email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'d': default, 's': str(size)})
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
        size = (400, 60)
        color = (255, 250, 250)
        im = Image.new('RGB', size, color)
        draw = ImageDraw.Draw(im)
        blue = (135, 206, 250)
        black = (0, 0, 0)
        row1_pos = (70, 5)
        #buraya duzgun bir metin koymali
        row1 = '%s %s' % (self.quit_date, self.first_row)
        row2_pos = (70, 15)
        row2 = '%d %s' % (self.daily_quantity, self.second_row)
        footer = self.footer
        draw.text(row1_pos, row1, fill=blue)
        draw.text(row2_pos, row2, fill=blue)
        #umuthanin katkilariyla nosomike.png :D
        icon = Image.open(self.nosmoke_image)
        im.paste(icon, (0, 0))
        gravatar = self.get_gravatar(self.email)
        im.paste(gravatar, (340, 0))
        border = ImageOps.expand(im, border=2, fill=black)
        return border.save('%s/%s' % (self.output_dir, self.output_file))

#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#    num2pinyin.py (c) 2012 Kasper Souren <kasper@guaka.org>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.



def num2pinyin(s):
    # Inspired by http://en.wikipedia.org/wiki/Pinyin
    # "the tone mark should always be placed by the
    # order--'a','o','e','i','u','ü', with the only exception being
    # 'iu', where the tone mark is placed on the 'u' instead."
    d = { 1: u'ā ō ē ī ū ǖ Ā Ē Ī Ō Ū Ǖ',
          2: u'á ó é í ú ǘ Á É Í Ó Ú Ǘ',
          3: u'ǎ ǒ ě ǐ ǔ ǚ Ǎ Ě Ǐ Ǒ Ǔ Ǚ',
          4: u'à ò è ì ù ǜ À È Ì Ò Ù Ǜ',
          5: u'a o e i u ü A E I O U Ü'}
    d5 = d[5]
 
    def num2diacritic(phon):
        tone = int(phon[-1])
        phon = phon[0 : -1]
        # to do: add exception for iu
        vowels = filter(lambda c: c in d5, phon)[0]
        # print phon, tone, vowels
        return phon.replace(vowels, d[tone][d5.find(vowels)])

    return ' '.join(map(num2diacritic, s.split(' ')))


test = 'wo3 men5 qu4 xiang1 gang3'

print num2pinyin(test)

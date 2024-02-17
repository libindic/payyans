#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Payyans Ascii to Unicode Convertor
# Copyright 2008-2009 Santhosh Thottingal <santhosh.thottingal@gmail.com>,
# Nishan Naseer <nishan.naseer@gmail.com>, Manu S Madhav <manusmad@gmail.com>,
# Rajeesh K Nambiar <rajeeshknambiar@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email:
# santhosh.thottingal@gmail.com
# URL: http://www.smc.org.in
from __future__ import print_function

'''
പയ്യന്‍ ആളു തരികിടയാകുന്നു. ആസ്കി വേറൊരു തരികിടയും.
തരികിടയെ തരികിടകൊണ്ടു നേരിടുന്നതാണു് ബുദ്ധി.
അമേരിക്കാ-ഇറാഖ് യുദ്ധം താഴെപ്പറയും വിധമാകുന്നു.
'''

# ആവശ്യത്തിനുള്ള കോപ്പുകള്‍ കൂട്ടുക
import codecs  # കൊടച്ചക്രം
import os  # ശീലക്കുട
from libindic.normalizer import Normalizer
from libindic.unicode_conversion_maps import maps
from .reader import Reader


'''
പയ്യന്റെ ക്ലാസ് ഉന്നതകുലമാകുന്നു. ച്ചാല്‍ ആഢ്യന്‍ തന്നെ.
ഏ ക്ലാസ് പയ്യന്‍...!
'''

prebase_letters = ["േ", "ൈ", "്ര", "െ"]
postbase_letters = ["ാ", "ി", "ീ", "ു", "ൂ", "ൃ", "ൗ", "ം", "ഃ", "്യ", "്വ"]


class Payyans():

    def __init__(self):
        self.input_filename = ""
        self.output_filename = ""
        self.mapping_filename = ""
        self.rulesDict = None
        self.pdf = 0
        self.data = {"fonts": maps.keys()}
        self.normalizer = Normalizer()

    def Unicode2ASCII(self, unicode_text, font):
        unicode_text = self.normalizer.normalize(unicode_text)
        index = 0
        ascii_text = ""
        rulesReverse = self.getRules(font)
        self.rulesDict = {v: k for k, v in rulesReverse.items()}
        while index < len(unicode_text):
            '''കൂട്ടക്ഷരങ്ങള്‍ക്കൊരു കുറുക്കുവഴി'''
            for charNo in [3, 2, 1]:
                letter = unicode_text[index:index + charNo]
                if letter in self.rulesDict:
                    ascii_letter = self.rulesDict[letter]
                    letter = letter.encode('utf-8')
                    '''
                    കിട്ടിയ അക്ഷരങ്ങളുടെ അപ്പുറത്തും ഇപ്പുറത്തും
                    സ്വരചിഹ്നങ്ങള്‍ ഫിറ്റ് ചെയ്യാനുള്ള ബദ്ധപ്പാട്
                    '''
                    if letter == 'ൈ':  # പിറകില്‍ രണ്ടു സാധനം പിടിപ്പിക്കുക
                        ascii_text = ascii_text[:-1] + ascii_letter + \
                            ascii_text[-1:]
                    elif (letter == 'ോ') | (letter == 'ൊ') \
                            | (letter == 'ൌ'):  # മുമ്പിലൊന്നും പിറകിലൊന്നും
                        ascii_text = ascii_text[:-1] + ascii_letter[0] + \
                            ascii_text[-1:] + ascii_letter[1]
                    elif (letter == 'െ') | (letter == 'േ') | \
                            (letter == '്ര'):  # പിറകിലൊന്നുമാത്രം
                        ascii_text = ascii_text[:-1] + ascii_letter + \
                            ascii_text[-1:]
                    else:
                        ascii_text = ascii_text + ascii_letter
                    index = index + charNo
                    break
                else:
                    if(charNo == 1):
                        index = index + 1
                        ascii_text = ascii_text + letter
                        break
                    '''നോക്കിയിട്ടു കിട്ടുന്നില്ല ബായി'''
                    ascii_letter = letter
                    # ascii_text = ascii_text + ascii_letter
                    # index = index+1

        return ascii_text

    def ASCII2Unicode(self, ascii_text, font):
        self.rulesDict = self.getRules(font)

        prebase_ascii_letters = [k for k, v in self.rulesDict.items() if v in prebase_letters]
        postbase_ascii_letters = [k for k, v in self.rulesDict.items() if v in postbase_letters]
        
        # ആദ്യത്തെ ഓട്ടം: മുമ്പേ ഗമിക്കും പ്രീബേസിനെ പിടിച്ച് തോളില്‍ കയറ്റുക
        ascii_text = Reader(ascii_text)
        transposed_text = ""
        prebase = ""
        while ascii_text.has_more_char():
            letter = ascii_text.next_char()
            if letter in prebase_ascii_letters:
                prebase = letter + prebase
            elif letter in postbase_ascii_letters:
                transposed_text += letter + prebase
                prebase = ""
            else:
                transposed_text += letter + prebase
                prebase = ""
        if prebase != "":
            transposed_text += prebase
        
        # രണ്ടാമത്തെ ഓട്ടം: പച്ച മലയാളം
        translator = str.maketrans({k: v for k, v in self.rulesDict.items() if len(k) == 1})
        unicode_text = transposed_text.translate(translator)

        # മൂന്നാമത്തെ ഓട്ടം: ചേരുംപടി ചേര്‍ക്കുക
        unicode_text = self.normalizer.normalize(unicode_text, keep_punctuations=True)

        return unicode_text  # മതം മാറ്റി തിരിച്ചു കൊടുക്ക്വാ !

    def listAvailableMaps(self):
        for key in maps.keys():
            print(key, end=", ")

    def printMap(self, font):
        rules = self.getRules(font)

        print("{:<3} {:<6}".format('Key', 'Target'))

        for key, val in rules.items():
            print("{:<2} : {:<3}".format(key, val), end="\n")

    def getVowelSign(self, vowel_letter, vowel_sign_letter):
        vowel = vowel_letter.encode('utf-8')
        vowel_sign = vowel_sign_letter.encode('utf-8')
        if vowel == "എ":
            if vowel_sign == "െ":
                return "ഐ"
        if vowel == "ഒ":
            if vowel_sign == "ാ":
                return "ഓ"
            if vowel_sign == "ൗ":
                return "ഔ"
        return (vowel_letter + vowel_sign_letter)

    def isPrebase(self, letter):
        '''
         ഇതെന്തിനാന്നു ചോദിച്ചാ, ഈ അക്ഷരങ്ങളുടെ ഇടതു വശത്തെഴുതുന്ന
         സ്വര ചിഹ്നങ്ങളുണ്ടല്ലോ? അവ ആസ്കി തരികിടയില്‍ എഴുതുന്നതു് ഇടതു വശത്തു
         തന്നെയാ. യൂണിക്കോഡില്‍ അക്ഷരത്തിനു ശേഷവും അപ്പൊ ആ വക സംഭവങ്ങളെ
         തിരിച്ചറിയാനാണു് ഈ സംഭവം.
        "തരികിട തരികിടോ ധീംതരികിട" (തരികിട തരികിടയാല്‍)
         എന്നു പയ്യന്റെ ഗുരു പയ്യഗുരു പയ്യെ മൊഴിഞ്ഞിട്ടുണ്ടു്.
        '''
        return letter in prebase_letters

    def isPostbase(self, letter):
        '''
        "ക്യ" എന്നതിലെ "്യ", "ക്വ" എന്നതിലെ "്വ" എന്നിവ പോസ്റ്റ്-ബേസ് ആണ്.
        "ത്യേ" എന്നത് ആസ്കിയില്‍ "ഏ+ത+്യ" എന്നാണ് എഴുതുന്നത്.
        അപ്പോള്‍ വ്യഞ്ജനം കഴിഞ്ഞ് പോസ്റ്റ്-ബേസ് ഉണ്ടെങ്കില്‍
        വ്യഞ്ജനം+പോസ്റ്റ്-ബേസ് കഴിഞ്ഞേ പ്രീ-ബേസ് ചേര്‍ക്കാവൂ!
        ഹൊ, പയ്യന്‍ പാണിനീശിഷ്യനാണ്!!
        '''
        return letter in postbase_letters

    def getRules(self, font):
        if font in maps.keys():
            return maps[font]

        old_maps = {
            'haritha': 'Haritha',
            'ambili': 'ML-TTAmbili',
            'karthika': 'ML-TTKarthika',
            'nandini': 'ML-TTNandini',
            'revathi': 'ML-TTRevathi',
            'indulekha': 'MLB-TTIndulekha',
            'manorama': 'Manorama',
            'matweb': 'Matweb',
            'valluvar': 'TM-TTValluvar'
            }

        if font in old_maps.keys():
            return maps[old_maps[font]];

        raise AttributeError(f"No such map found: {font}")

    def get_module_name(self):
        return "Payyans Unicode-ASCII Converter"

    def get_info(self):
        return "ASCII data - Unicode Convertor based on font maps"


def getInstance():
    return Payyans()
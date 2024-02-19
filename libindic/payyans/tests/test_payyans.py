#! /usr/bin/python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Payyans


class PayyansTest(TestCase):

    def setUp(self):
        super(PayyansTest, self).setUp()
        self.payyans = Payyans()

    def test_ascii2unicode(self):
        self.assertEqual(self.payyans.ASCII2Unicode("aebmfw", "ML-TTAmbili"), "മലയാളം")

    def test_unicode2ascii(self):
        self.assertEqual(self.payyans.Unicode2ASCII("മലയാളം", "ML-TTAmbili"), "aebmfw")

    def test_double_swaras(self):
        inputs = [
            ",",
            "ss{U",
            "t{]aw",
            "kvss{XWX",
            "{ZpXKXnbnÂ",
            r"\nt¡mf sSkv‌e",
            r"{][m\ambpw C´y³ kwØm\§fmb lnamNÂ {]tZiv, P½p ImivaoÀ F¶nhnS§fnÂ Xmakn¡p¶ Hcp AÀ²þCt´mþBcy³ hwiobþ`mjm]camb tKm{XamWv KÍn",
            r"Hcp hÀj¯nÂ s^{_phcn amk¯n\p 29 Znhkw Ds­¦nÂ B hÀjs¯ A[nhÀjw F¶p ]dbp¶p. Hcp hÀjw A[nhÀjamtWm F¶v IW¡m¡p¶ AÂsKmcnXamWv Nn{X¯nÂ.",
        ]
        expected = [
            ",",
            "ഡ്രൈ",
            "പ്രേമം",
            "സ്ത്രൈണത",
            "ദ്രുതഗതിയിൽ",
            "നിക്കോള ടെസ്‌ല",
            "പ്രധാനമായും ഇന്ത്യൻ സംസ്ഥാനങ്ങളായ ഹിമാചൽ പ്രദേശ്, ജമ്മു കാശ്മീർ എന്നിവിടങ്ങളിൽ താമസിക്കുന്ന ഒരു അർദ്ധ-ഇന്തോ-ആര്യൻ വംശീയ-ഭാഷാപരമായ ഗോത്രമാണ് ഗഡ്ഡി",
            "ഒരു വർഷത്തിൽ ഫെബ്രുവരി മാസത്തിനു 29 ദിവസം ഉണ്ടെങ്കിൽ ആ വർഷത്തെ അധിവർഷം എന്നു പറയുന്നു. ഒരു വർഷം അധിവർഷമാണോ എന്ന് കണക്കാക്കുന്ന അൽഗൊരിതമാണ് ചിത്രത്തിൽ.",
        ]
        for i in range(len(inputs)):
            actual = self.payyans.ASCII2Unicode(inputs[i], "ML-TTKarthika")
            self.assertEqual(actual, expected[i])

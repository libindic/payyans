#! /usr/bin/python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Payyans


class PayyansTest(TestCase):

    def setUp(self):
        super(PayyansTest, self).setUp()
        self.payyans = Payyans()

    def test_ascii2unicode(self):
        self.assertEqual(
            self.payyans.ASCII2Unicode(
                "aebmfw", "ambili"), u"മലയാളം")

    def test_unicode2ascii(self):
        self.assertEqual(
            self.payyans.Unicode2ASCII(
                u"മലയാളം", "ambili"), u"aebmfw")

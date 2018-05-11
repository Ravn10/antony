# -*- coding: utf-8 -*-
# Copyright (c) 2018, crisco and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class EngineInfo(Document):
	pass
def set_indicator(self):
		"""Set indicator for portal"""
		if self.status == "In":
			self.indicator_color = "green"
			#self.indicator_title = _("In")
		else:
			self.indicator_color = "red"
			#self.indicator_title = _("Out")

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from . import CONST
from odoo.exceptions import ValidationError
import logging


class IrSequence(models.Model):
    _inherit = "ir.sequence"

    def view_next_by_code(self, sequence_code):
        """Not search by company"""

        sequence = self.search([("code", "=", sequence_code)], limit=1)
        return f"{sequence.prefix}{sequence.number_next_actual}"

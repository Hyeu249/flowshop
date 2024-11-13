# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from . import CONST
from odoo.exceptions import ValidationError
import logging


class Table(models.Model):
    _name = "flowshop.table"
    _description = "Table records"
    _inherit = ["mail.thread"]

    def _get_default_model_name(self):
        return self.env["ir.sequence"].view_next_by_code(self._name)

    model = fields.Char(
        "Model name",
        default=_get_default_model_name,
        required=True,
        readonly=True,
        tracking=True,
    )
    name = fields.Char("Name", required=True, tracking=True)
    description = fields.Text("Description", tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            model = self.env["ir.sequence"].next_by_code(self._name)
            vals["model"] = model

        result = super(Table, self).create(vals_list)

        return result

    def write(self, vals):
        self.ensure_one()
        result = super(Table, self).write(vals)

        return result

    def unlink(self):
        return super(Table, self).unlink()

    def name_get(self):
        result = []
        for report in self:
            name = report.name or _("New")
            result.append((report.id, name))
        return result

# -*- coding: utf-8 -*-
import json

from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError

class ProductExpense(models.Model):
    _inherit = 'product.expense'

    @api.onchange('warehouse')
    def change_product_domain(self):
        aa = self.env['product.product'].search([('categ_id', 'not in', [11])])
        # self.expense_line.expense_line
        pass

    serial_number = fields.Char('Сериал №')
    ed_number = fields.Char('Эдийн №')

    @api.onchange('is_technic_expense')
    def get_kk(self):
        self.product_domain = "[('type', '=', 'service')]"
        # is_technic_expense = self.is_technic_expense
        # if is_technic_expense:
        #     return [('type', '=', 'service')]           # , ('categ_id','not in', [11, 114])]             #
        # return [('type', '=', 'service')]


    # product = fields.Many2one('product.product', 'Product', required=True, domain=get_kk, index=True)
    product = fields.Many2one('product.product', 'Product', required=True, index=True)


    # product_domain = fields.Char(compte="_calc_domain", readonly=True, store=False)
    product_domain = fields.Char(readonly=True, store=False)

    # @api.multi
    # @api.depends('is_technic_expense')
    # def _calc_domain(self):
    #     for rec in self:
    #         rec.product_domain = json.dump([('type', '=', 'service')])

    # @api.depends('is_technic_expense')
    # def get_lone_values(self):
    #     line.product = self.env.context.get('is_technic_expense')
    #     is_technic_expense = self.env.context.get('is_technic_expense')
    #     if is_technic_expense:
    #         return [('type', '=', 'service')]           # , ('categ_id','not in', [11, 114])]             #
    #     # return [('type', '=', 'service')]


class ExpenseLine(models.Model):
    _inherit = 'product.expense.line'

    def _get_prods(self):
        is_technic_expense = self.expense.is_technic_expense
        if is_technic_expense:
            # aa = self.env['product.product'].search([('categ_id', 'not in', [11])])
            aa = self.env['product.product'].search([('type', '=', 'service')])
            return aa
        pass        #@api.depends('expense')



    def get_kk(self):
        is_technic_expense = self.env.context.get('is_technic_expense')
        if is_technic_expense is None:
            return [('type', '=', 'service')]
        if is_technic_expense:
            return [('type', '!=', 'service')]           # , ('categ_id','not in', [11, 114])]             #
        # return [('type', '=', 'service')]


    # def get_aa():
    #     return fields.Many2one('product.product', 'Product', required=True, domain=lambda self:self.get_kk(), index=True)


    # product = fields.Many2one('product.product', 'Product', required=True, index=True, domain=[('type', '!=', 'service')])
    # product = fields.Many2one('product.product', 'Product', required=True, index=True, domain=[])
    product = fields.Many2one('product.product', 'Product', required=True, domain=get_kk, index=True)
    # product = fields.Many2one('product.product', 'Product', required=True, domain=get_kk, index=True)        #get_aa()
    # product = fields.Many2one('product.product', 'Product', required=True, domain=get_kk, index=True)

    # is_technic_expense = fields.Boolean(related='expense.is_technic_expense', readonly=True, relation="res.currency")

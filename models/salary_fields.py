from odoo import models, fields, api, _


class AddFieldsForEmployeeContract(models.Model):
    _inherit = 'hr.contract'

    logic_hra = fields.Float(string='HRA')
    special_allowance = fields.Float(string='Special Allowance')
    statutory_bonus = fields.Float(string='Statutory Bonus')
    incentive = fields.Float(string='Incentive')
    other_earnings = fields.Float(string='Other Earnings')
    pf_employer_contribution = fields.Float(string='PF Employer Contribution')
    esi_employer_contribution = fields.Float(string='ESI Employer Contribution')

    ded_pf_employee_contribution = fields.Float(string='PF Employee Contribution')
    ded_esi_employee_contribution = fields.Float(string='ESI Employee Contribution')
    professional_tax = fields.Float(string='Professional Tax')
    work_from_home = fields.Float(string='Work From Home Deductions')
    loan_amount = fields.Float(string='Loan Amount')
    income_tax = fields.Float(string='Income Tax')
    leave_salary_deduction = fields.Float(string='Leave Salary Deduction')
    salary_advance = fields.Float(string='Salary Advance')


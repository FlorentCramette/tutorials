from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postal Code")
    # La date de disponibilité ne sera pas copiée et par défaut dans 3 mois
    date_availability = fields.Date(
        string="Availability Date",
        copy=False,
        default=lambda self: date.today() + relativedelta(months=+3)
    )
    expected_price = fields.Float(string="Expected Price", required=True)
    # Le prix de vente est en lecture seule et non copiable
    selling_price = fields.Float(
        string="Selling Price",
        readonly=True,
        copy=False
    )
    # Le nombre de chambres par défaut est 2
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        [
            ('north', 'Nord'),
            ('south', 'Sud'),
            ('east', 'Est'),
            ('west', 'Ouest')
        ],
        string="Garden Orientation"
    )
    # Champ actif pour contrôler l'affichage (True par défaut)
    active = fields.Boolean(string="Active", default=True)
    # Champ d'état avec les valeurs possibles, obligatoire, non copiable et par défaut "Nouveau"
    state = fields.Selection(
        [
            ('new', 'Nouveau'),
            ('offer_received', 'Offre reçue'),
            ('offer_accepted', 'Offre acceptée'),
            ('sold', 'Vendu'),
            ('cancelled', 'Annulé')
        ],
        string="Status",
        required=True,
        copy=False,
        default='new'
    )

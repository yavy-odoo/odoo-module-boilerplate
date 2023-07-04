{
    "name": "Module Name",

    "summary": "Module Summary",

    "description": """
    Module Name
====================
description
    """,

    "version": "0.1",

    "category": "MainCategory/SubCategory",

    "license": "LGPL-3",

    "depends": ["stock", "website"],

    "data": [
        "security/module_name_groups.xml",
        "security/ir.model.access.csv",
        'data/registry_data.xml',
        "views/module_name_menuitems.xml",
        "views/module_name_views.xml",
        "views/product_template_inherit.xml",
        "views/module_name_templates.xml",
    ],

    "demo": [
        "demo/module_name_demo.xml",
        "demo/product_demo.xml",
    ],

    "author": "Odoo",

    "website": "www.odoo.com",

    "application": True,

}
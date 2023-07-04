# Boilerplate/Template for Odoo Modules

Boilerplate/Template Code to bootstrap your custom Odoo module

Find and Replace:

- [ ] ModuleName
- [ ] module.name
- [ ] Any occurences of module
- [ ] Any occurences of motorcycle
- [ ] Any occurences of feature
- [ ] demo (data) files


## File Structure

```
module_name/
|-- __init__.py
|-- __manifest__.py
|-- controllers/
|   |-- __init__.py
|   |-- module_name_controllers.py
|-- data/
|   |-- feature_data.xml
|-- models/
|   |-- __init__.py
|   |-- module_name.py
|   |-- product.py        <- Inherited Model Name
|-- security/
|   |-- ir.model.access.csv
|   |-- module_name_groups.xml
|-- static/
|   |-- description/
|   |   |-- icon.jpg
|-- views/
|   |-- module_name_menuitems.xml
|   |-- module_name_views.xml
|   |-- module_name_templates.xml
|   |-- product_template_inherit.xml    <- Inherited View Name + _inherit.xml
```

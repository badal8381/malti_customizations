import frappe


def change_display_depends_on(doctype, fieldname, depends_on_condition):
    docfield = frappe.get_doc("DocField", {"parent": doctype, "fieldname": fieldname})
    if docfield:
        docfield.depends_on = depends_on_condition
        docfield.save()


def execute():
    change_display_depends_on("Selling Settings", "maintain_same_rate_action", "eval: (doc.validate_selling_price || doc.maintain_same_sales_rate)")
    change_display_depends_on("Selling Settings", "role_to_override_stop_action", "eval: ((doc.validate_selling_price || doc.maintain_same_sales_rate) && doc.maintain_same_rate_action == 'Stop')")

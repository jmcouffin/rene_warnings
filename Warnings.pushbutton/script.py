# utf-
from pyrevit import revit, script
output = script.get_output()
output.close_others()
output.print_md("# Rene's warnings in the document")

doc = revit.doc
warns = doc.GetWarnings()
for warn in warns:
    output.print_md("### {}".format(warn.GetDescriptionText()))
    try:
        failing_elems = warn.GetFailingElements()
        for elem in failing_elems:
            output.print_md(output.linkify(elem))
    except:
        pass
    try:
        additionnal_elements = warn.GetAdditionalElements()
        for elem in additionnal_elements:
            output.print_md(output.linkify(elem))
    except:
        pass
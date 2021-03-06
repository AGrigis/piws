##########################################################################
# NSAp - Copyright (C) CEA, 2013
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

# Cubicweb import
from cubicweb.predicates import is_instance
from cubicweb.web.action import Action
from cubicweb.web.views.wdoc import HelpAction, AboutAction
from cubicweb.web.views.actions import PoweredByAction
from logilab.common.registry import yes


###############################################################################
# ACTIONS
###############################################################################

class PoweredByPIWSAction(Action):
    __regid__ = "poweredby"
    __select__ = yes()

    category = "footer"
    order = 3
    title = _("Powered by PIWS")

    def url(self):
        return self._cw.build_url("piws")


def registration_callback(vreg):

    # Update the footer
    vreg.register(PoweredByPIWSAction)
    vreg.unregister(HelpAction)
    vreg.unregister(AboutAction)
    vreg.unregister(PoweredByAction)

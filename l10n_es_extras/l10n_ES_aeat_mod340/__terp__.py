# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2009 Alejandro Sanchez (http://www.asr-oss.com) All Rights Reserved.
#                    Alejandro Sanchez <alejandro@asr-oss.com>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################
{
    "name" : "Generación de fichero modelo 340",
    "version" : "1.0",
    "author" : "Alejandro Sanchez",
    "description" : """Módulo para la presentación del Modelo 340
********************* Esta Versión se encuetra en Desarrollo ************************
Fin
""",
    "website" : "www.asr-oss.com",
    "license" : "GPL-2",
    "depends" : ["account"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : ["mod340_view.xml","mod340_wizard.xml","security/ir.model.access.csv",],
    "installable" : True,
    "active" : False,
}

# -*- coding: utf-8 -*-
"""
    sphinx.builders.latex.nodes
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    docutils nodes for LaTeX builder.

    :copyright: Copyright 2007-2018 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes


class footnotemark(nodes.Inline, nodes.Referential, nodes.TextElement):
    """A node represents ``\footnotemark``."""
    pass


class footnotetext(nodes.General, nodes.BackLinkable, nodes.Element,
                   nodes.Labeled, nodes.Targetable):
    """A node represents ``\footnotetext``."""
    pass

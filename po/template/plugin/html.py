#
#  The Template-Python distribution is Copyright (C) Sean McAfee 2007-2008,
#  derived from the Perl Template Toolkit Copyright (C) 1996-2007 Andy
#  Wardley.  All Rights Reserved.
#
#  The file "LICENSE" at the top level of this source distribution describes
#  the terms under which this file may be distributed.
#

import re

from template.plugin import Plugin


"""
template.plugin.html - Plugin to create HTML elements


SYNOPSIS

    [% USE HTML %]

    [% HTML.escape("if (a < b && c > d) ..." %]

    [% HTML.element(table => { border => 1, cellpadding => 2 }) %]

    [% HTML.attributes(border => 1, cellpadding => 2) %]


DESCRIPTION

The HTML plugin is very new and very basic, implementing a few useful
methods for generating HTML.  It is likely to be extended in the
future or integrated with a larger project to generate HTML elements
in a generic way (as discussed recently on the mod_perl mailing list).


METHODS

escape(text)

Returns the source text with any HTML reserved characters such as
'<', '>', etc., correctly esacped to their entity equivalents.

attributes(dictionary)

Returns the elements of the dictionary correctly formatted
(e.g. values quoted and correctly escaped) as attributes for an HTML
element.

element(type, attributes)

Generates an HTML element of the specified type and with the
attributes provided as an optional dictionary as the second argument
or as named arguments.

    [% HTML.element(table => { border => 1, cellpadding => 2 }) %]
    [% HTML.element('table', border=1, cellpadding=2) %]
    [% HTML.element(table => attribs) %]


DEBUGGING

The HTML plugin accepts a 'sorted' option as a constructor argument
which, when set to any true value, causes the attributes generated by
the attributes() method (either directly or via element()) to be
returned in sorted order.  Order of attributes isn't important in
HTML, but this is provided mainly for the purposes of debugging where
it is useful to have attributes generated in a deterministic order
rather than whatever order the dictionary happened to feel like
returning the keys in.

    [% USE HTML(sorted=1) %]
    [% HTML.element( foo => { charlie => 1, bravo => 2, alpha => 3 } ) %]

generates:

    <foo alpha="3" bravo="2" charlie="1">

"""


class Html(Plugin):
  """Template Toolkit plugin providing useful functionality for generating
  HTML.
  """
  def __init__(self, context, args=None):
    Plugin.__init__(self)
    self.__sorted = bool(args and args.get("sorted"))

  def element(self, name, attr=None):
    if isinstance(name, dict):
      name, attr = name.items()[0]
    if name is None or len(str(name)) == 0:
      return ""
    attr = self.attributes(attr)
    return "<%s%s%s>" % (name, attr and " " or "", attr)

  def attributes(self, hash):
    if not isinstance(hash, dict):
      return ""
    items = hash.items()
    if self.__sorted:
      items.sort()
    return " ".join('%s="%s"' % (k, self.escape(v)) for k, v in items)

  def escape(self, text=""):
    return str(text) \
           .replace("&", "&amp;") \
           .replace("<", "&lt;") \
           .replace(">", "&gt;") \
           .replace('"', "&quot;")

  def url(self, text=None):
    if text is None:
      return None
    else:
      return re.sub(r"[^a-zA-Z0-9_.-]",
                    lambda match: "%%%02x" % ord(match.group()),
                    text)
